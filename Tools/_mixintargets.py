"""Validate @Mixin injection targets against the local jars.

javac never checks `@Inject(method = "...")` strings, so a method renamed or
deleted in the 26.1 update compiles cleanly and then crashes the game at load
(the mixin config uses `defaultRequire: 1`). This walks every mixin source,
resolves its target class in the local jars, and reports injection targets that
do not exist on that class or any of its supertypes.

Usage:
    python _mixintargets.py [sable simulated offroad aeronautics]
"""
import io
import os
import re
import sys
import zipfile

import _dumpapi as D

ROOT = r"E:\TUAN2\MCMODS\create-aeronautics-fly"
JARS = [
    os.path.join(ROOT, "Tools", "_mc", "client-26.1.2.jar"),
    os.path.join(ROOT, "Tools", "_jars", "frapi.jar"),
]

MIXIN_RE = re.compile(r"@Mixin\s*\(([^)]*)\)", re.S)
CLASS_REF_RE = re.compile(r"([A-Za-z0-9_.$]+)\.class")
TARGETS_RE = re.compile(r"targets\s*=\s*\"([^\"]+)\"")
IMPORT_RE = re.compile(r"^\s*import\s+(?!static)([A-Za-z0-9_.$]+)\s*;", re.M)
INJECT_RE = re.compile(
    r"@(Inject|Redirect|ModifyVariable|ModifyArg|ModifyArgs|ModifyConstant|"
    r"WrapOperation|WrapWithCondition|ModifyExpressionValue|ModifyReturnValue|"
    r"ModifyReceiver|Accessor|Invoker)\s*\(",
    re.S,
)
METHOD_ATTR_RE = re.compile(r"method\s*=\s*(\{[^}]*\}|\"[^\"]*\")", re.S)
STRING_RE = re.compile(r"\"([^\"]*)\"")


def resolve_ref(ref, imports):
    """Turn a source-level class reference into a binary name.

    Mixins usually name their target by simple name and import it, so consult
    the file's import list before falling back to the reference as written.
    """
    head = ref.split(".")[0]
    fqn = imports.get(head)
    if fqn is None:
        return ref.replace(".", "/")
    rest = ref[len(head):]
    # Outer.Inner -> Outer$Inner
    return fqn.replace(".", "/") + rest.replace(".", "$")


class JarIndex:
    def __init__(self):
        self.zips = [zipfile.ZipFile(p) for p in JARS]
        self._cache = {}

    def read(self, internal):
        entry = internal + ".class"
        for z in self.zips:
            try:
                return z.read(entry)
            except KeyError:
                continue
        return None

    def info(self, internal):
        if internal not in self._cache:
            data = self.read(internal)
            self._cache[internal] = D.parse(data) if data else None
        return self._cache[internal]

    def method_names(self, internal):
        """All declared method names on the class and its supertypes."""
        names = set()
        seen = set()
        stack = [internal]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            info = self.info(cur)
            if info is None:
                continue
            for nm, _desc, _acc in info["methods"]:
                if nm:
                    names.add(nm)
            for parent in (info.get("super"),):
                if parent and parent != "java/lang/Object":
                    stack.append(parent)
            data = self.read(cur)
            if data:
                for parent in _interfaces(data):
                    stack.append(parent)
        return names


def _interfaces(data):
    """Parse the interfaces list of a class file."""
    import struct
    try:
        _cp, off = D.read_cp(data, 8)
    except Exception:
        return []
    off += 6
    count = struct.unpack_from(">H", data, off)[0]
    off += 2
    out = []
    for _ in range(count):
        idx = struct.unpack_from(">H", data, off)[0]
        off += 2
        out.append(idx)
    return []


def method_names_from_annotation(arg_text):
    """Extract the plain method names from an annotation's method= list."""
    match = METHOD_ATTR_RE.search(arg_text)
    if not match:
        return []
    out = []
    for raw in STRING_RE.findall(match.group(1)):
        name = raw.split("(")[0]           # drop descriptor if present
        if ";" in name:
            name = name.rsplit(";", 1)[-1]  # Lpkg/Class;name -> name
        if name.startswith("L") and "/" in name:
            name = name.rsplit("/", 1)[-1]
        out.append(name)
    return out


def main():
    modules = sys.argv[1:] or ["sable", "simulated", "offroad", "aeronautics"]
    index = JarIndex()

    unresolvable_targets = {}
    missing = []
    checked = 0
    skipped = 0

    for mod in modules:
        srcroot = os.path.join(ROOT, mod, "src", "main", "java")
        if not os.path.isdir(srcroot):
            continue
        for dirpath, _dirs, files in os.walk(srcroot):
            for fn in files:
                if not fn.endswith(".java"):
                    continue
                path = os.path.join(dirpath, fn)
                with io.open(path, "r", encoding="utf-8") as fh:
                    text = fh.read()

                mixin = MIXIN_RE.search(text)
                if not mixin:
                    continue
                args = mixin.group(1)
                if TARGETS_RE.search(args):
                    skipped += 1
                    continue
                refs = CLASS_REF_RE.findall(args)
                if not refs:
                    skipped += 1
                    continue

                imports = {}
                for fqn in IMPORT_RE.findall(text):
                    imports[fqn.rsplit(".", 1)[-1]] = fqn

                rel = os.path.relpath(path, ROOT)

                for ref in refs:
                    internal = resolve_ref(ref, imports)
                    if index.info(internal) is None:
                        unresolvable_targets[rel] = ref
                        continue

                    available = index.method_names(internal)

                    for match in INJECT_RE.finditer(text):
                        kind = match.group(1)
                        # Grab the balanced-ish argument text of the annotation.
                        tail = text[match.end():match.end() + 4000]
                        depth = 1
                        end = 0
                        for i, ch in enumerate(tail):
                            if ch == "(":
                                depth += 1
                            elif ch == ")":
                                depth -= 1
                                if depth == 0:
                                    end = i
                                    break
                        arg_text = tail[:end]

                        if kind in ("Accessor", "Invoker"):
                            continue

                        for name in method_names_from_annotation(arg_text):
                            checked += 1
                            if name and name not in available:
                                missing.append((rel, kind, ref, name))

    print("=== mixin targets that do not exist on the target class ===")
    for rel, kind, ref, name in missing:
        print("  %s\n      @%s -> %s#%s" % (rel, kind, ref, name))
    print("\n%d method target(s) checked; %d missing" % (checked, len(missing)))

    if unresolvable_targets:
        print("\n=== target classes not present in the local jars (not checked) ===")
        for rel, ref in sorted(unresolvable_targets.items()):
            print("  %s -> %s" % (rel, ref))
        print("  (%d skipped, %d targetless mixins)" % (len(unresolvable_targets), skipped))


if __name__ == "__main__":
    main()
