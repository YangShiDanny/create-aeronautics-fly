# Compile report - Minecraft 26.1.2 port

- commit: `10ff8a088055948136aac90ce9cc22e05b6febc6`
- ref: `port/26.1.2`
- date: 2026-10-01T07:00:08Z

## Result: BUILD FAILED

Total `error:` lines: 300
Total `error:` (unique): 194

### Top error sources
```
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:48: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:44: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:3: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:19: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:18: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:5: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelRenderData.java:3: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:6: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:427: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:3: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:6: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:22: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:77: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:72: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:474: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:457: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:20: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:19: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:18: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:188: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:181: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:17: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:141: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:116: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:95: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:6: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:61: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:5: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:52: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:32: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:314: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:299: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:224: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:184: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:95: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:81: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:3: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:31: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:27: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:24: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:137: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:103: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:90: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:5: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:507: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:284: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:247: error:
```

### Errors grouped by package
```
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:15: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:14: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:13: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:48: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:44: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:19: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:18: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelRenderData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:427: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:10: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:4: error: package dev.ryanhcode.sable.companion does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:22: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:77: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:72: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:474: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:457: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:20: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:19: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:18: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:188: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:181: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:17: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:141: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:116: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:95: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:61: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:5: error: package dev.ryanhcode.sable.companion does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:52: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:32: error: cannot find symbol
```

### Unique errors (first 800)
```
  sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:132: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/physics/force/ForceTotal.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/physics/handle/RigidBodyHandle.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:98: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MergedMassTracker.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:43: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:18: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:150: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:232: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:247: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:284: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:507: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:90: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:103: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:137: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:24: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:27: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:31: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:81: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:95: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:184: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:224: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:299: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:314: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:32: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:52: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:5: error: package dev.ryanhcode.sable.companion does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:61: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:95: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:116: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:141: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:17: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:181: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:188: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:18: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:19: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:20: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:457: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:474: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:72: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:77: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:22: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:4: error: package dev.ryanhcode.sable.companion does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:10: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:427: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelRenderData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:18: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:19: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:44: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:48: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:13: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:14: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:15: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:132: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/physics/force/ForceTotal.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/physics/handle/RigidBodyHandle.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:98: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MergedMassTracker.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:43: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:18: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:150: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:232: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:247: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:284: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:507: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:90: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:103: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:137: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:24: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:27: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:31: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:81: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:95: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:184: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:224: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:299: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:314: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:32: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:52: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:5: error: package dev.ryanhcode.sable.companion does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:61: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:95: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:116: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:141: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:17: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:181: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:188: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:18: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:19: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:20: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:457: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:474: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:72: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:77: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:22: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:4: error: package dev.ryanhcode.sable.companion does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:10: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:427: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelRenderData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:18: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:19: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:44: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:48: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:13: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:14: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:15: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
```

### Missing symbols (top 120)
```
```

### Gradle failure block
```
FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':sable:compileJava' (registered by plugin class 'org.gradle.api.plugins.JavaBasePlugin').
> Compilation failed; see the compiler output below.
  Note: Recompile with -Xlint:deprecation for details.
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error: cannot find symbol
      private final Pose3d pose;
                    ^
    symbol:   class Pose3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error: cannot find symbol
      protected final Pose3d lastPose;
                      ^
    symbol:   class Pose3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error: cannot find symbol
      protected final BoundingBox3d globalBounds = new BoundingBox3d(0, 0, 0, 0, 0, 0);
                      ^
    symbol:   class BoundingBox3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error: cannot find symbol
      protected final BoundingBox3d lastGlobalBounds = new BoundingBox3d(0, 0, 0, 0, 0, 0);
                      ^
    symbol:   class BoundingBox3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error: cannot find symbol
      protected SubLevel(final Level level, final int plotX, final int plotY, final Pose3d pose) {
                                                                                    ^
    symbol:   class Pose3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error: cannot find symbol
      public Pose3d logicalPose() {
             ^
    symbol:   class Pose3d
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error: cannot find symbol
      public Pose3dc lastPose() {
             ^
    symbol:   class Pose3dc
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error: cannot find symbol
      public BoundingBox3dc boundingBox() {
             ^
    symbol:   class BoundingBox3dc
    location: class SubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:232: error: cannot find symbol
      public SubLevel allocateNewSubLevel(final Pose3d pose) {
                                                ^
    symbol:   class Pose3d
    location: class SubLevelContainer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:247: error: cannot find symbol
      public SubLevel allocateSubLevel(final UUID uuid, final int x, final int z, final Pose3d pose) {
                                                                                        ^
    symbol:   class Pose3d
    location: class SubLevelContainer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:284: error: cannot find symbol
      protected abstract SubLevel createSubLevel(int globalPlotX, int globalPlotZ, Pose3d pose, UUID uuid);
                                                                                   ^
    symbol:   class Pose3d
    location: class SubLevelContainer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:507: error: cannot find symbol
      public Iterable<SubLevel> queryIntersecting(final BoundingBox3dc bounds) {
                                                        ^
    symbol:   class BoundingBox3dc
    location: class SubLevelContainer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error: cannot find symbol
      private @Nullable BoundingBox3i boundingBox;
                        ^
    symbol:   class BoundingBox3i
    location: class PlotChunkHolder
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error: cannot find symbol
      public BoundingBox3ic getBoundingBox() {
             ^
    symbol:   class BoundingBox3ic
    location: class PlotChunkHolder
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:43: error: cannot find symbol
      protected SubLevel createSubLevel(final int globalPlotX, final int globalPlotZ, final Pose3d pose, final UUID uuid) {
                                                                                            ^
    symbol:   class Pose3d
    location: class ClientSubLevelContainer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:52: error: cannot find symbol
      private final Pose3d renderPose = new Pose3d();
                    ^
    symbol:   class Pose3d
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:61: error: cannot find symbol
      private final BoundingBox3d sweptBounds = new BoundingBox3d();
                    ^
    symbol:   class BoundingBox3d
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:95: error: cannot find symbol
      public ClientSubLevel(final Level level, final int plotX, final int plotY, final Pose3d pose) {
                                                                                       ^
    symbol:   class Pose3d
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:184: error: cannot find symbol
      public int computeSubLevelSkyLight(final Pose3dc pose) {
                                               ^
    symbol:   class Pose3dc
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:224: error: cannot find symbol
      public BoundingBox3dc boundingBox() {
             ^
    symbol:   class BoundingBox3dc
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:299: error: cannot find symbol
      public Pose3dc renderPose() {
             ^
    symbol:   class Pose3dc
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:314: error: cannot find symbol
      public Pose3dc renderPose(final float pt) {
             ^
    symbol:   class Pose3dc
    location: class ClientSubLevel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error: cannot find symbol
      public void wasSplitFrom(final ClientSableInterpolationState state, @NotNull final ClientSubLevel splitFrom, @NotNull final Pose3dc pose) {
                                                                                                                                  ^
    symbol:   class Pose3dc
```

### What went wrong
```
```

### Raw log head (first 150 lines)
```
Fetching distribution.
Downloading https://services.gradle.org/distributions/gradle-9.7.1-bin.zip
..............10%..............20%...............30%..............40%...............50%..............60%...............70%..............80%..............90%...............100%

Welcome to Gradle 9.7.1!

Here are the highlights of this release:
 - Isolated Projects graduates to incubating
 - Broader Configuration Cache compatibility
 - Resilient Sync helps you fix broken builds
 - More source locations in problem reports

For more details see https://docs.gradle.org/9.7.1/release-notes.html

To honour the JVM settings for this build a single-use Daemon process will be forked. For more on this, please refer to https://docs.gradle.org/9.7.1/userguide/gradle_daemon.html#sec:disabling_the_daemon in the Gradle documentation.
Daemon will be stopped at the end of the build 

> Configure project :aeronautics
Fabric Loom: 1.18.2

> Configure project :sable
Fabric Loom: 1.18.2

> Configure project :simulated
Fabric Loom: 1.18.2

> Configure project :offroad
Fabric Loom: 1.18.2

> Task :sable:compileJava
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:4: error: package dev.ryanhcode.sable.companion does not exist
import dev.ryanhcode.sable.companion.SubLevelAccess;
                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:22: error: cannot find symbol
public abstract class SubLevel implements SubLevelAccess {
                                          ^
  symbol: class SubLevelAccess
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:32: error: cannot find symbol
    private final Pose3d pose;
                  ^
  symbol:   class Pose3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:37: error: cannot find symbol
    protected final Pose3d lastPose;
                    ^
  symbol:   class Pose3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:43: error: cannot find symbol
    protected final BoundingBox3d globalBounds = new BoundingBox3d(0, 0, 0, 0, 0, 0);
                    ^
  symbol:   class BoundingBox3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:48: error: cannot find symbol
    protected final BoundingBox3d lastGlobalBounds = new BoundingBox3d(0, 0, 0, 0, 0, 0);
                    ^
  symbol:   class BoundingBox3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:86: error: cannot find symbol
    protected SubLevel(final Level level, final int plotX, final int plotY, final Pose3d pose) {
                                                                                  ^
  symbol:   class Pose3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:149: error: cannot find symbol
    public Pose3d logicalPose() {
           ^
  symbol:   class Pose3d
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:157: error: cannot find symbol
    public Pose3dc lastPose() {
           ^
  symbol:   class Pose3dc
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:165: error: cannot find symbol
    public BoundingBox3dc boundingBox() {
           ^
  symbol:   class BoundingBox3dc
  location: class SubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:9: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:232: error: cannot find symbol
    public SubLevel allocateNewSubLevel(final Pose3d pose) {
                                              ^
  symbol:   class Pose3d
  location: class SubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:247: error: cannot find symbol
    public SubLevel allocateSubLevel(final UUID uuid, final int x, final int z, final Pose3d pose) {
                                                                                      ^
  symbol:   class Pose3d
  location: class SubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:284: error: cannot find symbol
    protected abstract SubLevel createSubLevel(int globalPlotX, int globalPlotZ, Pose3d pose, UUID uuid);
                                                                                 ^
  symbol:   class Pose3d
  location: class SubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:507: error: cannot find symbol
    public Iterable<SubLevel> queryIntersecting(final BoundingBox3dc bounds) {
                                                      ^
  symbol:   class BoundingBox3dc
  location: class SubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:30: error: cannot find symbol
    private @Nullable BoundingBox3i boundingBox;
                      ^
  symbol:   class BoundingBox3i
  location: class PlotChunkHolder
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/PlotChunkHolder.java:154: error: cannot find symbol
    public BoundingBox3ic getBoundingBox() {
           ^
  symbol:   class BoundingBox3ic
  location: class PlotChunkHolder
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ClientSubLevelContainer.java:43: error: cannot find symbol
    protected SubLevel createSubLevel(final int globalPlotX, final int globalPlotZ, final Pose3d pose, final UUID uuid) {
                                                                                          ^
  symbol:   class Pose3d
  location: class ClientSubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:5: error: package dev.ryanhcode.sable.companion does not exist
import dev.ryanhcode.sable.companion.ClientSubLevelAccess;
                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
```

### Raw log tail (last 400 lines)
```
  location: class ClientSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:299: error: cannot find symbol
    public Pose3dc renderPose() {
           ^
  symbol:   class Pose3dc
  location: class ClientSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:314: error: cannot find symbol
    public Pose3dc renderPose(final float pt) {
           ^
  symbol:   class Pose3dc
  location: class ClientSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ClientSubLevel.java:338: error: cannot find symbol
    public void wasSplitFrom(final ClientSableInterpolationState state, @NotNull final ClientSubLevel splitFrom, @NotNull final Pose3dc pose) {
                                                                                                                                ^
  symbol:   class Pose3dc
  location: class ClientSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:137: error: cannot find symbol
    public record Snapshot(int gameTick, Pose3dc pose) {
                                         ^
  symbol:   class Pose3dc
  location: class Snapshot
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:24: error: cannot find symbol
    private final Pose3d runningSnapshot = new Pose3d();
                  ^
  symbol:   class Pose3d
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:27: error: cannot find symbol
    public SubLevelSnapshotInterpolator(final Pose3d pose) {
                                              ^
  symbol:   class Pose3d
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:31: error: cannot find symbol
    public void getSampleAt(final double gameTick, final Pose3d dest) {
                                                         ^
  symbol:   class Pose3d
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:81: error: cannot find symbol
    public void receiveSnapshot(final int gameTick, final Pose3dc data) {
                                                          ^
  symbol:   class Pose3dc
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error: cannot find symbol
    public void setFirstPoses(final Pose3dc poseA, final Pose3dc poseB) {
                                    ^
  symbol:   class Pose3dc
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:90: error: cannot find symbol
    public void setFirstPoses(final Pose3dc poseA, final Pose3dc poseB) {
                                                         ^
  symbol:   class Pose3dc
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:95: error: cannot find symbol
    public Pose3dc getInterpolatedPose() {
           ^
  symbol:   class Pose3dc
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/SubLevelSnapshotInterpolator.java:103: error: cannot find symbol
    public void splitFrom(final SubLevelSnapshotInterpolator other, @NotNull final Pose3dc pose) {
                                                                                   ^
  symbol:   class Pose3dc
  location: class SubLevelSnapshotInterpolator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/client/ClientSableInterpolationState.java:90: error: cannot find symbol
    public void receiveSnapshot(final ClientSubLevel clientSubLevel, final int gameTick, final Pose3dc data, final PacketReceiveMode packetReceiveMode) {
                                                                                               ^
  symbol:   class Pose3dc
  location: class ClientSableInterpolationState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:13: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:14: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:15: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:8: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:17: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:18: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:19: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:20: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/ServerSubLevelContainer.java:150: error: cannot find symbol
    protected SubLevel createSubLevel(final int globalPlotX, final int globalPlotZ, final Pose3d pose, final UUID uuid) {
                                                                                          ^
  symbol:   class Pose3d
  location: class ServerSubLevelContainer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:72: error: cannot find symbol
    private final Pose3d lastNetworkedPose = new Pose3d();
                  ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:77: error: cannot find symbol
    private final BoundingBox3i lastNetworkedBoundingBox = new BoundingBox3i();
                  ^
  symbol:   class BoundingBox3i
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MergedMassTracker.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:116: error: cannot find symbol
    private Pose3d splitFromPose = null;
            ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:141: error: cannot find symbol
    public ServerSubLevel(final ServerLevel level, final int plotX, final int plotY, final Pose3d pose) {
                                                                                           ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:181: error: cannot find symbol
    public Pose3d lastNetworkedPose() {
           ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:188: error: cannot find symbol
    public BoundingBox3i lastNetworkedBoundingBox() {
           ^
  symbol:   class BoundingBox3i
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/handle/RigidBodyHandle.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.JOMLConversion;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:457: error: cannot find symbol
    public void setSplitFrom(final ServerSubLevel containingSubLevel, final Pose3d originalPose) {
                                                                            ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/ServerSubLevel.java:474: error: cannot find symbol
    public Pose3d getSplitFromPose() {
           ^
  symbol:   class Pose3d
  location: class ServerSubLevel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:10: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3ic;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.JOMLConversion;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/mass/MassTracker.java:98: error: cannot find symbol
    public static MassTracker build(final BlockGetter blockGetter, final BoundingBox3ic bounds) {
                                                                         ^
  symbol:   class BoundingBox3ic
  location: class MassTracker
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.JOMLConversion;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:7: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/block/BlockSubLevelLiftProvider.java:132: error: cannot find symbol
                                             @NotNull final Pose3d localPose, final double timeStep,
                                                            ^
  symbol:   class Pose3d
  location: interface BlockSubLevelLiftProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:18: error: cannot find symbol
    void sable$getLocalBounds(final BoundingBox3i bounds);
                                    ^
  symbol:   class BoundingBox3i
  location: interface KinematicContraption
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error: cannot find symbol
    default Pose3d sable$getLocalPose(final Pose3d dest, final double partialTick) {
                                            ^
  symbol:   class Pose3d
  location: interface KinematicContraption
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/KinematicContraption.java:38: error: cannot find symbol
    default Pose3d sable$getLocalPose(final Pose3d dest, final double partialTick) {
            ^
  symbol:   class Pose3d
  location: interface KinematicContraption
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/physics/force/ForceTotal.java:6: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.JOMLConversion;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/heat/SubLevelHeatMapManager.java:427: error: cannot find symbol
        void addBlocks(final Level level, final BoundingBox3ic assemblyBounds, final Collection<BlockPos> blocks);
                                                ^
  symbol:   class BoundingBox3ic
  location: interface SplitListener
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3dc;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunk.java:5: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3i;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:3: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.BoundingBox3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:4: error: package dev.ryanhcode.sable.companion.math does not exist
import dev.ryanhcode.sable.companion.math.Pose3d;
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:18: error: cannot find symbol
    private final @NotNull BoundingBox3d bounds;
                           ^
  symbol:   class BoundingBox3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:19: error: cannot find symbol
    private final @NotNull Pose3d pose;
                           ^
  symbol:   class Pose3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error: cannot find symbol
    public SubLevelData(@NotNull final UUID uuid, @NotNull final BoundingBox3d bounds, @NotNull final Pose3d pose, @NotNull final List<UUID> relations, @NotNull final CompoundTag fullTag) {
                                                                 ^
  symbol:   class BoundingBox3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:24: error: cannot find symbol
    public SubLevelData(@NotNull final UUID uuid, @NotNull final BoundingBox3d bounds, @NotNull final Pose3d pose, @NotNull final List<UUID> relations, @NotNull final CompoundTag fullTag) {
                                                                                                      ^
  symbol:   class Pose3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:44: error: cannot find symbol
    public @NotNull BoundingBox3d bounds() {
                    ^
  symbol:   class BoundingBox3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelData.java:48: error: cannot find symbol
    public @NotNull Pose3d pose() {
                    ^
  symbol:   class Pose3d
  location: class SubLevelData
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:48: warning: [removal] getLightEngine() in StarLightLightingProvider has been deprecated and marked for removal
        return provider.getLightEngine();
                       ^
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: Some input files use unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
100 errors
1 warning
	at org.gradle.api.internal.tasks.compile.JdkJavaCompiler.execute(JdkJavaCompiler.java:88)
	at org.gradle.api.internal.tasks.compile.JdkJavaCompiler.execute(JdkJavaCompiler.java:49)
	at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.delegateAndHandleErrors(NormalizingJavaCompiler.java:98)
	at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.execute(NormalizingJavaCompiler.java:52)
	at org.gradle.api.internal.tasks.compile.NormalizingJavaCompiler.execute(NormalizingJavaCompiler.java:38)
	at org.gradle.api.internal.tasks.compile.AnnotationProcessorDiscoveringCompiler.execute(AnnotationProcessorDiscoveringCompiler.java:52)
	at org.gradle.api.internal.tasks.compile.AnnotationProcessorDiscoveringCompiler.execute(AnnotationProcessorDiscoveringCompiler.java:38)
	at org.gradle.api.internal.tasks.compile.ModuleApplicationNameWritingCompiler.execute(ModuleApplicationNameWritingCompiler.java:46)
	at org.gradle.api.internal.tasks.compile.ModuleApplicationNameWritingCompiler.execute(ModuleApplicationNameWritingCompiler.java:36)
	at org.gradle.jvm.toolchain.internal.DefaultToolchainJavaCompiler.execute(DefaultToolchainJavaCompiler.java:57)
	at org.gradle.api.tasks.compile.JavaCompile.lambda$createToolchainCompiler$0(JavaCompile.java:207)
	at org.gradle.api.internal.tasks.compile.CleaningJavaCompiler.execute(CleaningJavaCompiler.java:53)
	at org.gradle.api.internal.tasks.compile.incremental.IncrementalCompilerFactory.lambda$createRebuildAllCompiler$0(IncrementalCompilerFactory.java:55)
	at org.gradle.api.internal.tasks.compile.incremental.SelectiveCompiler.execute(SelectiveCompiler.java:70)
	at org.gradle.api.internal.tasks.compile.incremental.SelectiveCompiler.execute(SelectiveCompiler.java:44)
	at org.gradle.api.internal.tasks.compile.incremental.IncrementalResultStoringCompiler.execute(IncrementalResultStoringCompiler.java:66)
	at org.gradle.api.internal.tasks.compile.incremental.IncrementalResultStoringCompiler.execute(IncrementalResultStoringCompiler.java:52)
	at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler$CompileOperation.call(CompileJavaBuildOperationReportingCompiler.java:78)
	at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler$CompileOperation.call(CompileJavaBuildOperationReportingCompiler.java:52)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:210)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:205)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:67)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:167)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:54)
	at org.gradle.api.internal.tasks.compile.CompileJavaBuildOperationReportingCompiler.execute(CompileJavaBuildOperationReportingCompiler.java:49)
	at org.gradle.api.tasks.compile.JavaCompile.performCompilation(JavaCompile.java:225)
	at org.gradle.api.tasks.compile.JavaCompile.performIncrementalCompilation(JavaCompile.java:166)
	at org.gradle.api.tasks.compile.JavaCompile.compile(JavaCompile.java:151)
	at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:125)
	at org.gradle.api.internal.project.taskfactory.IncrementalTaskAction.doExecute(IncrementalTaskAction.java:45)
	at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:51)
	at org.gradle.api.internal.project.taskfactory.IncrementalTaskAction.execute(IncrementalTaskAction.java:26)
	at org.gradle.api.internal.project.taskfactory.StandardTaskAction.execute(StandardTaskAction.java:29)
	at org.gradle.api.internal.tasks.execution.TaskExecution$3.run(TaskExecution.java:259)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:30)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$1.execute(DefaultBuildOperationRunner.java:27)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:67)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:167)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.run(DefaultBuildOperationRunner.java:48)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeAction(TaskExecution.java:244)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeActions(TaskExecution.java:227)
	at org.gradle.api.internal.tasks.execution.TaskExecution.executeWithPreviousOutputFiles(TaskExecution.java:210)
	at org.gradle.api.internal.tasks.execution.TaskExecution.execute(TaskExecution.java:176)
	at org.gradle.internal.execution.steps.ExecuteStep.executeInternal(ExecuteStep.java:167)
	at org.gradle.internal.execution.steps.ExecuteStep.access$000(ExecuteStep.java:47)
	at org.gradle.internal.execution.steps.ExecuteStep$1.call(ExecuteStep.java:137)
	at org.gradle.internal.execution.steps.ExecuteStep$1.call(ExecuteStep.java:134)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:210)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$CallableBuildOperationWorker.execute(DefaultBuildOperationRunner.java:205)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:67)
	at org.gradle.internal.operations.DefaultBuildOperationRunner$2.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:167)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.execute(DefaultBuildOperationRunner.java:60)
	at org.gradle.internal.operations.DefaultBuildOperationRunner.call(DefaultBuildOperationRunner.java:54)
	at org.gradle.internal.execution.steps.ExecuteStep.execute(ExecuteStep.java:134)
	at org.gradle.internal.execution.steps.ExecuteStep$Mutable.execute(ExecuteStep.java:80)
	at org.gradle.internal.execution.steps.CancelExecutionStep.execute(CancelExecutionStep.java:42)
	at org.gradle.internal.execution.steps.TimeoutStep.executeWithoutTimeout(TimeoutStep.java:75)
	at org.gradle.internal.execution.steps.TimeoutStep.execute(TimeoutStep.java:55)
	at org.gradle.internal.execution.steps.PreCreateOutputParentsStep.execute(PreCreateOutputParentsStep.java:51)
	at org.gradle.internal.execution.steps.PreCreateOutputParentsStep.execute(PreCreateOutputParentsStep.java:29)
	at org.gradle.internal.execution.steps.RemovePreviousOutputsStep.executeMutable(RemovePreviousOutputsStep.java:67)
	at org.gradle.internal.execution.steps.RemovePreviousOutputsStep.executeMutable(RemovePreviousOutputsStep.java:39)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.BroadcastChangingOutputsStep.execute(BroadcastChangingOutputsStep.java:42)
	at org.gradle.internal.execution.steps.BroadcastChangingOutputsStep.execute(BroadcastChangingOutputsStep.java:24)
	at org.gradle.internal.execution.steps.CaptureOutputsAfterExecutionStep.execute(CaptureOutputsAfterExecutionStep.java:69)
	at org.gradle.internal.execution.steps.CaptureOutputsAfterExecutionStep.execute(CaptureOutputsAfterExecutionStep.java:46)
	at org.gradle.internal.execution.steps.ResolveInputChangesStep.executeMutable(ResolveInputChangesStep.java:39)
	at org.gradle.internal.execution.steps.ResolveInputChangesStep.executeMutable(ResolveInputChangesStep.java:28)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.BuildCacheStep.executeWithoutCache(BuildCacheStep.java:189)
	at org.gradle.internal.execution.steps.BuildCacheStep.executeAndStoreInCache(BuildCacheStep.java:145)
	at org.gradle.internal.execution.steps.BuildCacheStep.lambda$executeWithCache$3(BuildCacheStep.java:104)
	at org.gradle.internal.execution.steps.BuildCacheStep.lambda$executeWithCache$1(BuildCacheStep.java:104)
	at org.gradle.internal.Try$Success.map(Try.java:170)
	at org.gradle.internal.execution.steps.BuildCacheStep.executeWithCache(BuildCacheStep.java:88)
	at org.gradle.internal.execution.steps.BuildCacheStep.lambda$execute$0(BuildCacheStep.java:75)
	at org.gradle.internal.Either$Left.fold(Either.java:116)
	at org.gradle.internal.execution.caching.CachingState.fold(CachingState.java:62)
	at org.gradle.internal.execution.steps.BuildCacheStep.execute(BuildCacheStep.java:74)
	at org.gradle.internal.execution.steps.BuildCacheStep.execute(BuildCacheStep.java:49)
	at org.gradle.internal.execution.steps.StoreExecutionStateStep.executeMutable(StoreExecutionStateStep.java:46)
	at org.gradle.internal.execution.steps.StoreExecutionStateStep.executeMutable(StoreExecutionStateStep.java:35)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.executeBecause(SkipUpToDateStep.java:75)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.lambda$execute$2(SkipUpToDateStep.java:53)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:53)
	at org.gradle.internal.execution.steps.SkipUpToDateStep.execute(SkipUpToDateStep.java:35)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:37)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsFinishedStep.execute(MarkSnapshottingInputsFinishedStep.java:27)
	at org.gradle.internal.execution.steps.ResolveMutableCachingStateStep.executeDelegate(ResolveMutableCachingStateStep.java:70)
	at org.gradle.internal.execution.steps.ResolveMutableCachingStateStep.executeDelegate(ResolveMutableCachingStateStep.java:32)
	at org.gradle.internal.execution.steps.AbstractResolveCachingStateStep.execute(AbstractResolveCachingStateStep.java:69)
	at org.gradle.internal.execution.steps.AbstractResolveCachingStateStep.execute(AbstractResolveCachingStateStep.java:37)
	at org.gradle.internal.execution.steps.ResolveChangesStep.executeMutable(ResolveChangesStep.java:63)
	at org.gradle.internal.execution.steps.ResolveChangesStep.executeMutable(ResolveChangesStep.java:34)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.ValidateStep$Mutable.executeDelegate(ValidateStep.java:79)
	at org.gradle.internal.execution.steps.ValidateStep$Mutable.executeDelegate(ValidateStep.java:65)
	at org.gradle.internal.execution.steps.ValidateStep.execute(ValidateStep.java:105)
	at org.gradle.internal.execution.steps.ValidateStep$Mutable.execute(ValidateStep.java:65)
	at org.gradle.internal.execution.steps.CaptureMutableStateBeforeExecutionStep.executeMutable(CaptureMutableStateBeforeExecutionStep.java:86)
	at org.gradle.internal.execution.steps.CaptureMutableStateBeforeExecutionStep.execute(CaptureMutableStateBeforeExecutionStep.java:65)
	at org.gradle.internal.execution.steps.CaptureMutableStateBeforeExecutionStep.execute(CaptureMutableStateBeforeExecutionStep.java:45)
	at org.gradle.internal.execution.steps.SkipEmptyMutableWorkStep.executeWithNonEmptySources(SkipEmptyMutableWorkStep.java:210)
	at org.gradle.internal.execution.steps.SkipEmptyMutableWorkStep.executeMutable(SkipEmptyMutableWorkStep.java:90)
	at org.gradle.internal.execution.steps.SkipEmptyMutableWorkStep.executeMutable(SkipEmptyMutableWorkStep.java:53)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.legacy.MarkSnapshottingInputsStartedStep.execute(MarkSnapshottingInputsStartedStep.java:38)
	at org.gradle.internal.execution.steps.LoadPreviousExecutionStateStep.executeMutable(LoadPreviousExecutionStateStep.java:36)
	at org.gradle.internal.execution.steps.LoadPreviousExecutionStateStep.executeMutable(LoadPreviousExecutionStateStep.java:23)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.HandleStaleOutputsStep.executeMutable(HandleStaleOutputsStep.java:77)
	at org.gradle.internal.execution.steps.HandleStaleOutputsStep.executeMutable(HandleStaleOutputsStep.java:43)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.AssignMutableWorkspaceStep.lambda$executeMutable$0(AssignMutableWorkspaceStep.java:34)
	at org.gradle.api.internal.tasks.execution.TaskExecution$4.withWorkspace(TaskExecution.java:305)
	at org.gradle.internal.execution.steps.AssignMutableWorkspaceStep.executeMutable(AssignMutableWorkspaceStep.java:30)
	at org.gradle.internal.execution.steps.AssignMutableWorkspaceStep.executeMutable(AssignMutableWorkspaceStep.java:21)
	at org.gradle.internal.execution.steps.MutableStep.execute(MutableStep.java:26)
	at org.gradle.internal.execution.steps.ChoosePipelineStep.execute(ChoosePipelineStep.java:40)
	at org.gradle.internal.execution.steps.ChoosePipelineStep.execute(ChoosePipelineStep.java:23)
	at org.gradle.internal.execution.steps.ExecuteWorkBuildOperationFiringStep.lambda$execute$2(ExecuteWorkBuildOperationFiringStep.java:67)
	at org.gradle.internal.execution.steps.ExecuteWorkBuildOperationFiringStep.execute(ExecuteWorkBuildOperationFiringStep.java:67)
	at org.gradle.internal.execution.steps.ExecuteWorkBuildOperationFiringStep.execute(ExecuteWorkBuildOperationFiringStep.java:39)
	at org.gradle.internal.execution.steps.IdentityCacheStep.execute(IdentityCacheStep.java:46)
	at org.gradle.internal.execution.steps.IdentityCacheStep.execute(IdentityCacheStep.java:34)
	at org.gradle.internal.execution.steps.IdentifyStep.execute(IdentifyStep.java:56)
	at org.gradle.internal.execution.steps.IdentifyStep.execute(IdentifyStep.java:38)
	at org.gradle.internal.execution.impl.DefaultExecutionEngine$1.execute(DefaultExecutionEngine.java:68)
	at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeIfValid(ExecuteActionsTaskExecuter.java:132)
	... 30 more


BUILD FAILED in 1m 7s
1 actionable task: 1 executed
```
