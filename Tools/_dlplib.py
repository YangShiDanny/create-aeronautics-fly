import os, urllib.request
UA={"User-Agent":"Mozilla/5.0"}
BR="1.21.1"
BASE="https://raw.githubusercontent.com/Fabricators-of-Create/Porting-Lib/%s/" % BR
OUT=r"E:/TUAN2/MCMODS/create-aeronautics-fly/Tools/_plib"
os.makedirs(OUT, exist_ok=True)
FILES=[
 "modules/data/src/main/java/io/github/fabricators_of_create/porting_lib/data/ExistingFileHelper.java",
 "modules/data/src/main/java/io/github/fabricators_of_create/porting_lib/data/LanguageProvider.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/BlockModelBuilder.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/BlockModelProvider.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/BlockStateProvider.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ConfiguredModel.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/IGeneratedBlockState.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ItemModelBuilder.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ItemModelProvider.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ModelBuilder.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ModelFile.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/ModelProvider.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/MultiPartBlockStateBuilder.java",
 "modules/models/src/main/java/io/github/fabricators_of_create/porting_lib/models/generators/VariantBlockStateBuilder.java",
 "modules/registry/src/main/java/io/github/fabricators_of_create/porting_lib/registry/DeferredHolder.java",
 "modules/resources/src/main/java/io/github/fabricators_of_create/porting_lib/resources/conditions/ICondition.java",
 "modules/resources/src/main/java/io/github/fabricators_of_create/porting_lib/resources/conditions/WithConditions.java",
 "modules/tags/src/main/java/io/github/fabricators_of_create/porting_lib/tags/Tags.java",
]
for f in FILES:
    dst=os.path.join(OUT, f.rsplit("/",1)[-1])
    try:
        data=urllib.request.urlopen(urllib.request.Request(BASE+f, headers=UA), timeout=90).read()
        open(dst,"wb").write(data)
        print("OK  %7d  %s" % (len(data), f.rsplit('/',1)[-1]))
    except Exception as e:
        print("ERR %s: %s" % (f, e))
