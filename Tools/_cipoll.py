"""Poll GitHub Actions check-runs for a commit until they finish.

Usage: python _cipoll.py <sha> [timeout_seconds]
"""
import json
import sys
import time
import urllib.request

REPO = "YangShiDanny/create-aeronautics-fly"
UA = {"User-Agent": "Mozilla/5.0", "Accept": "application/vnd.github+json"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    sha = sys.argv[1]
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 900
    deadline = time.time() + budget
    last = None
    while True:
        try:
            data = get(f"https://api.github.com/repos/{REPO}/commits/{sha}/check-runs")
        except Exception as e:
            print(f"  poll error: {e}")
            time.sleep(15)
            continue
        runs = data.get("check_runs", [])
        summary = tuple(
            (r["name"], r["status"], r.get("conclusion")) for r in runs
        )
        if summary != last:
            print(f"[{time.strftime('%H:%M:%S')}] runs={len(runs)}")
            for name, status, concl in summary:
                print(f"   {name:40s} {status:12s} {concl}")
            last = summary
        if runs and all(r["status"] == "completed" for r in runs):
            print("ALL COMPLETE")
            for r in runs:
                print(f"   {r['name']} -> {r.get('conclusion')}")
            return
        if not runs and time.time() > deadline - budget + 120:
            print("no check runs appeared yet; still waiting")
        if time.time() > deadline:
            print("TIMEOUT")
            return
        time.sleep(15)


if __name__ == "__main__":
    main()
