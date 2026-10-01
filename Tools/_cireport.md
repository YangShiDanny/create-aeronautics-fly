# Compile report - Minecraft 26.1.2 port

- commit: `5609caa6b85f4563f4e72816803f2067ab2b58f3`
- ref: `port/26.1.2`
- date: 2026-10-01T07:12:32Z

## Result: BUILD FAILED

Total `error:` lines: 300
Total `error:` (unique): 178

### Top error sources
```
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error:
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error:
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error:
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error:
      9 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:39: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:123: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:100: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:70: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:31: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:20: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:19: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:79: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:69: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:22: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:170: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:146: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:16: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/particle/ParticleMixin.java:20: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/explosion/ExplosionMixin.java:23: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:16: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:85: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:50: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rendering/EntityRendererMixin.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:65: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:41: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:30: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/debug_render/SubLevelBoundsRendererMixin.java:16: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:39: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:519: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:518: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:392: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:391: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:344: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:343: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:11: error:
```

### Errors grouped by package
```
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:39: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:123: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:100: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:70: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:31: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:20: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:19: error: package net.fabricmc.fabric.api.renderer.v1 does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:79: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:69: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:22: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:170: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:146: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:16: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/particle/ParticleMixin.java:20: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/explosion/ExplosionMixin.java:23: error: package net.minecraft.world.entity.projectile.windcharge does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:15: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error: cannot find symbol
```

### Unique errors (first 800)
```
  sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:11: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:12: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:343: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:344: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:391: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:392: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:518: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:519: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:12: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:39: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:11: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:12: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:39: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/debug_render/SubLevelBoundsRendererMixin.java:16: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:15: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:30: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:41: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:65: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rendering/EntityRendererMixin.java:11: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:13: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:50: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:85: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:16: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:9: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:14: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:15: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:15: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/explosion/ExplosionMixin.java:23: error: package net.minecraft.world.entity.projectile.windcharge does not exist
  sable/src/main/java/dev/ryanhcode/sable/mixin/particle/ParticleMixin.java:20: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:16: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:146: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:170: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:22: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:69: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:79: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:19: error: package net.fabricmc.fabric.api.renderer.v1 does not exist
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:20: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:31: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:70: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:100: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:123: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:11: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:12: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:343: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:344: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:391: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:392: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:518: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:519: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:12: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:39: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:11: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:12: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/block_decal_render/LevelRendererMixin.java:39: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/debug_render/SubLevelBoundsRendererMixin.java:16: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:15: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:30: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:41: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:65: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rendering/EntityRendererMixin.java:11: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:13: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:50: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:85: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:16: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:9: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:14: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:15: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:15: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/explosion/ExplosionMixin.java:23: error: package net.minecraft.world.entity.projectile.windcharge does not exist
sable/src/main/java/dev/ryanhcode/sable/mixin/particle/ParticleMixin.java:20: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:16: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:146: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:170: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:22: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:69: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:79: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:19: error: package net.fabricmc.fabric.api.renderer.v1 does not exist
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:20: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:31: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:70: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:100: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:123: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: z has private access in ChunkPos
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
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              final ChunkPos globalChunk = new ChunkPos(offsetPos);
                                           ^
    required: int,int
    found:    BlockPos
    reason: actual and formal argument lists differ in length
  Note: Recompile with -Xlint:deprecation for details.
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error: cannot find symbol
  import net.minecraft.client.renderer.state.LevelRenderState;
                                            ^
    symbol:   class LevelRenderState
    location: package net.minecraft.client.renderer.state
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error: cannot find symbol
              LevelRenderState levelRenderState
              ^
    symbol:   class LevelRenderState
    location: interface SubLevelBlockEntityRenderExtension
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:12: error: cannot find symbol
  import net.minecraft.client.renderer.state.BlockOutlineRenderState;
                                            ^
    symbol:   class BlockOutlineRenderState
    location: package net.minecraft.client.renderer.state
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:39: error: cannot find symbol
                                          final double camZ, final BlockOutlineRenderState outlineState,
                                                                   ^
    symbol:   class BlockOutlineRenderState
    location: class LevelRendererMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error: cannot find symbol
  import net.minecraft.client.renderer.LightTexture;
                                      ^
    symbol:   class LightTexture
    location: package net.minecraft.client.renderer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error: cannot find symbol
  import net.minecraft.client.renderer.RenderType;
                                      ^
    symbol:   class RenderType
    location: package net.minecraft.client.renderer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
      private final BlockMultiBufferSource blockDelegate;
                    ^
    symbol:   class BlockMultiBufferSource
    location: class SubLevelLightVertexConsumerProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
              final BlockMultiBufferSource blockDelegate,
                    ^
    symbol:   class BlockMultiBufferSource
    location: class SubLevelLightVertexConsumerProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error: cannot find symbol
      public VertexConsumer getBuffer(final RenderType renderType) {
                                            ^
    symbol:   class RenderType
    location: class SubLevelLightVertexConsumerProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:9: error: cannot find symbol
  import net.minecraft.world.entity.vehicle.AbstractMinecart;
                                           ^
    symbol:   class AbstractMinecart
    location: package net.minecraft.world.entity.vehicle
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:13: error: cannot find symbol
  import net.minecraft.client.renderer.state.CameraRenderState;
                                            ^
    symbol:   class CameraRenderState
    location: package net.minecraft.client.renderer.state
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:50: error: cannot find symbol
      private <S extends EntityRenderState> void sable$rotateEntity(final S renderState, final CameraRenderState cameraRenderState, final double x, final double y, final double z, final PoseStack poseStack, final SubmitNodeCollector submitNodeCollector, final CallbackInfo ci) {
                                                                                               ^
    symbol:   class CameraRenderState
    location: class EntityRenderDispatcherMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:85: error: cannot find symbol
      private <S extends EntityRenderState> void sable$popPose(final S renderState, final CameraRenderState cameraRenderState, final double x, final double y, final double z, final PoseStack poseStack, final SubmitNodeCollector submitNodeCollector, final CallbackInfo ci) {
                                                                                          ^
    symbol:   class CameraRenderState
    location: class EntityRenderDispatcherMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:15: error: cannot find symbol
  import net.minecraft.world.entity.projectile.AbstractArrow;
                                              ^
    symbol:   class AbstractArrow
    location: package net.minecraft.world.entity.projectile
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:41: error: cannot find symbol
      private void sable$setPos(final AbstractArrow arrow,
                                      ^
    symbol:   class AbstractArrow
    location: class AbstractArrowMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:65: error: cannot find symbol
      private void sable$setDeltaMovement(final AbstractArrow arrow,
                                                ^
    symbol:   class AbstractArrow
    location: class AbstractArrowMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rendering/EntityRendererMixin.java:11: error: cannot find symbol
  import net.minecraft.client.renderer.LightTexture;
                                      ^
    symbol:   class LightTexture
    location: package net.minecraft.client.renderer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error: cannot find symbol
  import net.minecraft.world.entity.animal.Parrot;
                                          ^
    symbol:   class Parrot
    location: package net.minecraft.world.entity.animal
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error: cannot find symbol
  import net.minecraft.world.entity.animal.ShoulderRidingEntity;
                                          ^
    symbol:   class ShoulderRidingEntity
    location: package net.minecraft.world.entity.animal
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error: cannot find symbol
      protected ParrotMixin(final EntityType<? extends ShoulderRidingEntity> entityType, final Level level) {
                                                       ^
    symbol:   class ShoulderRidingEntity
    location: class ParrotMixin
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error: cannot find symbol
  import net.minecraft.world.entity.projectile.ThrownTrident;
                                              ^
    symbol:   class ThrownTrident
    location: package net.minecraft.world.entity.projectile
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error: cannot find symbol
  import net.minecraft.world.level.BlockAndTintGetter;
                                  ^
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
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:4: error: cannot find symbol
import net.minecraft.client.renderer.state.LevelRenderState;
                                          ^
  symbol:   class LevelRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinterface/sublevel_render/SubLevelBlockEntityRenderExtension.java:11: error: cannot find symbol
            LevelRenderState levelRenderState
            ^
  symbol:   class LevelRenderState
  location: interface SubLevelBlockEntityRenderExtension
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:12: error: cannot find symbol
import net.minecraft.client.renderer.state.BlockOutlineRenderState;
                                          ^
  symbol:   class BlockOutlineRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/mixin/block_outline_render/LevelRendererMixin.java:39: error: cannot find symbol
                                        final double camZ, final BlockOutlineRenderState outlineState,
                                                                 ^
  symbol:   class BlockOutlineRenderState
  location: class LevelRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixinhelpers/entity/entity_rendering/shadows/SubLevelEntityShadowRenderer.java:14: error: cannot find symbol
import net.minecraft.client.renderer.LightTexture;
                                    ^
  symbol:   class LightTexture
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
import net.fabricmc.fabric.api.renderer.v1.render.BlockMultiBufferSource;
                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:10: error: cannot find symbol
import net.minecraft.client.renderer.RenderType;
                                    ^
  symbol:   class RenderType
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
        implements BlockMultiBufferSource, MultiBufferSource {
                   ^
  symbol: class BlockMultiBufferSource
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
    private final BlockMultiBufferSource blockDelegate;
                  ^
  symbol:   class BlockMultiBufferSource
  location: class SubLevelLightVertexConsumerProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
            final BlockMultiBufferSource blockDelegate,
                  ^
  symbol:   class BlockMultiBufferSource
  location: class SubLevelLightVertexConsumerProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:72: error: cannot find symbol
    public VertexConsumer getBuffer(final RenderType renderType) {
                                          ^
  symbol:   class RenderType
  location: class SubLevelLightVertexConsumerProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:9: error: cannot find symbol
import net.minecraft.world.entity.vehicle.AbstractMinecart;
                                         ^
  symbol:   class AbstractMinecart
  location: package net.minecraft.world.entity.vehicle
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:13: error: cannot find symbol
import net.minecraft.client.renderer.state.CameraRenderState;
                                          ^
  symbol:   class CameraRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:50: error: cannot find symbol
    private <S extends EntityRenderState> void sable$rotateEntity(final S renderState, final CameraRenderState cameraRenderState, final double x, final double y, final double z, final PoseStack poseStack, final SubmitNodeCollector submitNodeCollector, final CallbackInfo ci) {
                                                                                             ^
  symbol:   class CameraRenderState
  location: class EntityRenderDispatcherMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/EntityRenderDispatcherMixin.java:85: error: cannot find symbol
    private <S extends EntityRenderState> void sable$popPose(final S renderState, final CameraRenderState cameraRenderState, final double x, final double y, final double z, final PoseStack poseStack, final SubmitNodeCollector submitNodeCollector, final CallbackInfo ci) {
                                                                                        ^
  symbol:   class CameraRenderState
  location: class EntityRenderDispatcherMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:15: error: cannot find symbol
import net.minecraft.world.entity.projectile.AbstractArrow;
                                            ^
  symbol:   class AbstractArrow
  location: package net.minecraft.world.entity.projectile
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:41: error: cannot find symbol
    private void sable$setPos(final AbstractArrow arrow,
                                    ^
  symbol:   class AbstractArrow
  location: class AbstractArrowMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:65: error: cannot find symbol
    private void sable$setDeltaMovement(final AbstractArrow arrow,
                                              ^
  symbol:   class AbstractArrow
  location: class AbstractArrowMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rendering/EntityRendererMixin.java:11: error: cannot find symbol
import net.minecraft.client.renderer.LightTexture;
                                    ^
  symbol:   class LightTexture
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:7: error: cannot find symbol
import net.minecraft.world.entity.animal.Parrot;
                                        ^
  symbol:   class Parrot
  location: package net.minecraft.world.entity.animal
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:8: error: cannot find symbol
import net.minecraft.world.entity.animal.ShoulderRidingEntity;
                                        ^
  symbol:   class ShoulderRidingEntity
  location: package net.minecraft.world.entity.animal
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:15: error: cannot find symbol
public abstract class ParrotMixin extends ShoulderRidingEntity {
                                          ^
  symbol: class ShoulderRidingEntity
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:17: error: cannot find symbol
    protected ParrotMixin(final EntityType<? extends ShoulderRidingEntity> entityType, final Level level) {
                                                     ^
  symbol:   class ShoulderRidingEntity
  location: class ParrotMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:8: error: cannot find symbol
import net.minecraft.world.entity.projectile.ThrownTrident;
                                            ^
  symbol:   class ThrownTrident
  location: package net.minecraft.world.entity.projectile
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:8: error: cannot find symbol
import net.minecraft.world.level.BlockAndTintGetter;
                                ^
  symbol:   class BlockAndTintGetter
```

### Raw log tail (last 400 lines)
```
import net.minecraft.client.renderer.state.LevelRenderState;
                                          ^
  symbol:   class LevelRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:69: error: cannot find symbol
            final LevelRenderState levelRenderState,
                  ^
  symbol:   class LevelRenderState
  location: class LevelRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:79: error: cannot find symbol
            final LevelRenderState levelRenderState
                  ^
  symbol:   class LevelRenderState
  location: class LevelRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:146: error: cannot find symbol
    private void sable$transformBlockEntity(final PoseStack poseStack, final LevelRenderState levelRenderState, final SubmitNodeStorage submitNodeStorage, final CallbackInfo ci, @Local final BlockEntityRenderState renderState, @Local final BlockPos blockPos) {
                                                                             ^
  symbol:   class LevelRenderState
  location: class LevelRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:170: error: cannot find symbol
    private void sable$restoreCameraOrientation(final PoseStack poseStack, final LevelRenderState levelRenderState, final SubmitNodeStorage submitNodeStorage, final CallbackInfo ci) {
                                                                                 ^
  symbol:   class LevelRenderState
  location: class LevelRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
import net.minecraft.client.renderer.chunk.SectionBuffers;
                                          ^
  symbol:   class SectionBuffers
  location: package net.minecraft.client.renderer.chunk
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:19: error: package net.fabricmc.fabric.api.renderer.v1 does not exist
import net.fabricmc.fabric.api.renderer.v1.Renderer;
                                          ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:20: error: package net.fabricmc.fabric.api.renderer.v1.render does not exist
import net.fabricmc.fabric.api.renderer.v1.render.ChunkSectionLayerHelper;
                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
import net.minecraft.client.renderer.block.BlockRenderDispatcher;
                                          ^
  symbol:   class BlockRenderDispatcher
  location: package net.minecraft.client.renderer.block
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:31: error: cannot find symbol
import net.minecraft.client.renderer.state.LevelRenderState;
                                          ^
  symbol:   class LevelRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:70: error: cannot find symbol
            final LevelRenderState levelRenderState,
                  ^
  symbol:   class LevelRenderState
  location: class SodiumWorldRendererMixin
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/particle/ParticleMixin.java:20: error: cannot find symbol
import net.minecraft.client.renderer.LightTexture;
                                    ^
  symbol:   class LightTexture
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/debug_render/SubLevelBoundsRendererMixin.java:16: error: cannot find symbol
import net.minecraft.client.renderer.RenderType;
                                    ^
  symbol:   class RenderType
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:11: error: cannot find symbol
import net.minecraft.world.entity.projectile.AbstractArrow;
                                            ^
  symbol:   class AbstractArrow
  location: package net.minecraft.world.entity.projectile
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/entity/EntitySubLevelUtil.java:12: error: cannot find symbol
import net.minecraft.world.entity.projectile.AbstractHurtingProjectile;
                                            ^
  symbol:   class AbstractHurtingProjectile
  location: package net.minecraft.world.entity.projectile
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:16: error: cannot find symbol
@Mixin(AbstractMinecart.class)
       ^
  symbol: class AbstractMinecart
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/arrows_hit_blocks/AbstractArrowMixin.java:30: error: cannot find symbol
@Mixin(AbstractArrow.class)
       ^
  symbol: class AbstractArrow
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/parrot/ParrotMixin.java:14: error: cannot find symbol
@Mixin(Parrot.class)
       ^
  symbol: class Parrot
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/trident/ThrownTridentMixin.java:15: error: cannot find symbol
@Mixin(ThrownTrident.class)
       ^
  symbol: class ThrownTrident
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:16: error: cannot find symbol
@Mixin(BlockAndTintGetter.class)
       ^
  symbol: class BlockAndTintGetter
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: x has private access in ChunkPos
        return "[name=" + this.name + ", id=" + this.uniqueId + ", global_plot=" + this.plot.plotPos.x + "," + this.plot.plotPos.z + "]";
                                                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/SubLevel.java:228: error: z has private access in ChunkPos
        return "[name=" + this.name + ", id=" + this.uniqueId + ", global_plot=" + this.plot.plotPos.x + "," + this.plot.plotPos.z + "]";
                                                                                                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error: x has private access in ChunkPos
        return x >= this.plotPos.x << logBlockSize  && x < (this.plotPos.x + 1) << logBlockSize
                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:204: error: x has private access in ChunkPos
        return x >= this.plotPos.x << logBlockSize  && x < (this.plotPos.x + 1) << logBlockSize
                                                                        ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error: z has private access in ChunkPos
                && z >= this.plotPos.z << logBlockSize  && z < (this.plotPos.z + 1) << logBlockSize;
                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:205: error: z has private access in ChunkPos
                && z >= this.plotPos.z << logBlockSize  && z < (this.plotPos.z + 1) << logBlockSize;
                                                                            ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: x has private access in ChunkPos
        return new ChunkPos(this.plotPos.x << this.logSize, this.plotPos.z << this.logSize);
                                        ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:226: error: z has private access in ChunkPos
        return new ChunkPos(this.plotPos.x << this.logSize, this.plotPos.z << this.logSize);
                                                                        ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: x has private access in ChunkPos
        return new ChunkPos(((this.plotPos.x + 1) << this.logSize) - 1, ((this.plotPos.z + 1) << this.logSize) - 1);
                                          ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:233: error: z has private access in ChunkPos
        return new ChunkPos(((this.plotPos.x + 1) << this.logSize) - 1, ((this.plotPos.z + 1) << this.logSize) - 1);
                                                                                      ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: x has private access in ChunkPos
        return chunk.x >> this.logSize == this.plotPos.x && chunk.z >> this.logSize == this.plotPos.z;
                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: x has private access in ChunkPos
        return chunk.x >> this.logSize == this.plotPos.x && chunk.z >> this.logSize == this.plotPos.z;
                                                      ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: z has private access in ChunkPos
        return chunk.x >> this.logSize == this.plotPos.x && chunk.z >> this.logSize == this.plotPos.z;
                                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:240: error: z has private access in ChunkPos
        return chunk.x >> this.logSize == this.plotPos.x && chunk.z >> this.logSize == this.plotPos.z;
                                                                                                   ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: x has private access in ChunkPos
        return new ChunkPos(global.x - (this.plotPos.x << this.logSize), global.z - (this.plotPos.z << this.logSize));
                                  ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: x has private access in ChunkPos
        return new ChunkPos(global.x - (this.plotPos.x << this.logSize), global.z - (this.plotPos.z << this.logSize));
                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: z has private access in ChunkPos
        return new ChunkPos(global.x - (this.plotPos.x << this.logSize), global.z - (this.plotPos.z << this.logSize));
                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:247: error: z has private access in ChunkPos
        return new ChunkPos(global.x - (this.plotPos.x << this.logSize), global.z - (this.plotPos.z << this.logSize));
                                                                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: x has private access in ChunkPos
        return new ChunkPos(local.x + (this.plotPos.x << this.logSize), local.z + (this.plotPos.z << this.logSize));
                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: x has private access in ChunkPos
        return new ChunkPos(local.x + (this.plotPos.x << this.logSize), local.z + (this.plotPos.z << this.logSize));
                                                   ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: z has private access in ChunkPos
        return new ChunkPos(local.x + (this.plotPos.x << this.logSize), local.z + (this.plotPos.z << this.logSize));
                                                                             ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:254: error: z has private access in ChunkPos
        return new ChunkPos(local.x + (this.plotPos.x << this.logSize), local.z + (this.plotPos.z << this.logSize));
                                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: x has private access in ChunkPos
        if (local.x < 0 || local.x >= 1 << this.logSize || local.z < 0 || local.z >= 1 << this.logSize) {
                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: x has private access in ChunkPos
        if (local.x < 0 || local.x >= 1 << this.logSize || local.z < 0 || local.z >= 1 << this.logSize) {
                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: z has private access in ChunkPos
        if (local.x < 0 || local.x >= 1 << this.logSize || local.z < 0 || local.z >= 1 << this.logSize) {
                                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:261: error: z has private access in ChunkPos
        if (local.x < 0 || local.x >= 1 << this.logSize || local.z < 0 || local.z >= 1 << this.logSize) {
                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: z has private access in ChunkPos
        return this.chunks[local.z << this.logSize | local.x];
                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:265: error: x has private access in ChunkPos
        return this.chunks[local.z << this.logSize | local.x];
                                                          ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: z has private access in ChunkPos
        this.chunks[localChunkPos.z << this.logSize | localChunkPos.x] = holder;
                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:282: error: x has private access in ChunkPos
        this.chunks[localChunkPos.z << this.logSize | localChunkPos.x] = holder;
                                                                   ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: x has private access in ChunkPos
        return new ChunkPos((this.plotPos.x << this.logSize) + (1 << (this.logSize - 1)), (this.plotPos.z << this.logSize) + (1 << (this.logSize - 1)));
                                         ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:299: error: z has private access in ChunkPos
        return new ChunkPos((this.plotPos.x << this.logSize) + (1 << (this.logSize - 1)), (this.plotPos.z << this.logSize) + (1 << (this.logSize - 1)));
                                                                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/LevelPlot.java:395: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            final ChunkPos globalChunk = new ChunkPos(offsetPos);
                                         ^
  required: int,int
  found:    BlockPos
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: x has private access in ChunkPos
                this.removeSubLevel(plotPos.x - this.originX, plotPos.z - this.originZ, SubLevelRemovalReason.REMOVED);
                                           ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:165: error: z has private access in ChunkPos
                this.removeSubLevel(plotPos.x - this.originX, plotPos.z - this.originZ, SubLevelRemovalReason.REMOVED);
                                                                     ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:343: error: x has private access in ChunkPos
        final int plotX = (pos.x >> this.logPlotSize) - this.originX;
                              ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:344: error: z has private access in ChunkPos
        final int plotZ = (pos.z >> this.logPlotSize) - this.originZ;
                              ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: x has private access in ChunkPos
        return this.inBounds(pos.x, pos.z);
                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:353: error: z has private access in ChunkPos
        return this.inBounds(pos.x, pos.z);
                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:391: error: x has private access in ChunkPos
        final int plotX = (pos.x >> this.logPlotSize) - this.originX;
                              ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:392: error: z has private access in ChunkPos
        final int plotZ = (pos.z >> this.logPlotSize) - this.originZ;
                              ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:518: error: x has private access in ChunkPos
        final int x = subLevel.getPlot().plotPos.x - this.originX;
                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/api/sublevel/SubLevelContainer.java:519: error: z has private access in ChunkPos
        final int z = subLevel.getPlot().plotPos.z - this.originZ;
                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: x has private access in ChunkPos
                    this.pipeline.handleChunkSectionAddition(section, global.x, sectionY, global.z, true);
                                                                            ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelPhysicsSystem.java:378: error: z has private access in ChunkPos
                    this.pipeline.handleChunkSectionAddition(section, global.x, sectionY, global.z, true);
                                                                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: x has private access in ChunkPos
        return ChunkPos.asLong(plotPos.x - origin.x(), plotPos.z - origin.y);
                                      ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: z has private access in ChunkPos
        return ChunkPos.asLong(plotPos.x - origin.x(), plotPos.z - origin.y);
                                                              ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/SubLevelTrackingSystem.java:60: error: cannot find symbol
        return ChunkPos.asLong(plotPos.x - origin.x(), plotPos.z - origin.y);
                       ^
  symbol:   method asLong(int,int)
  location: class ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:100: error: cannot find symbol
        final long key = chunkPos.toLong();
                                 ^
  symbol:   method toLong()
  location: variable chunkPos of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:123: error: cannot find symbol
        final SubLevelHoldingChunk existingChunk = this.loadedHoldingChunks.get(chunkPos.toLong());
                                                                                        ^
  symbol:   method toLong()
  location: variable chunkPos of type ChunkPos
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


BUILD FAILED in 1m 5s
1 actionable task: 1 executed
```
