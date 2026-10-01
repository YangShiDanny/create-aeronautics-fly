# Compile report - Minecraft 26.1.2 port

- commit: `f98765941b97c790f22ac759ce2cf7b07f6ec83e`
- ref: `port/26.1.2`
- date: 2026-10-01T07:31:15Z

## Result: BUILD FAILED

Total `error:` lines: 300
Total `error:` (unique): 192

### Top error sources
```
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error:
      9 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/util/LevelAccelerator.java:101: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/tracking_points/SubLevelTrackingPointSavedData.java:53: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:430: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:165: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:115: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelStorage.java:44: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:529: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:448: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:309: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:280: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:271: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:246: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:206: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:138: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelTicketsSavedData.java:50: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelOccupancySavedData.java:31: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/vanilla/VanillaChunkedSubLevelRenderData.java:194: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:66: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:179: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:492: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:361: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:359: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:358: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:296: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:290: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:249: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:164: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:90: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:88: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:49: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:83: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:81: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:27: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:234: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/packets/udp/SableUDPEchoPacket.java:21: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/packets/tcp/ServerboundGizmoMoveSubLevelPacket.java:54: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:110: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:93: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:130: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:56: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:33: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerLevelMixin.java:100: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:144: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:129: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:118: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ServerLevelMixin.java:19: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ChunkMapMixin.java:22: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/EntityMixin.java:332: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:27: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/LivingEntityMixin.java:54: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:86: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:76: error:
```

### Errors grouped by package
```
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: z has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: x has private access in ChunkPos
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/util/LevelAccelerator.java:101: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/tracking_points/SubLevelTrackingPointSavedData.java:53: error: incompatible types: String cannot be converted to Identifier
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:430: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:165: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:115: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelStorage.java:44: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:529: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:448: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:309: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:280: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:271: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:246: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:206: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:138: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:15: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:14: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelTicketsSavedData.java:50: error: incompatible types: String cannot be converted to Identifier
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelOccupancySavedData.java:31: error: incompatible types: String cannot be converted to Identifier
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/vanilla/VanillaChunkedSubLevelRenderData.java:194: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:66: error: method does not override or implement a method from a supertype
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:179: error: SubLevelLightVertexConsumerProvider.SubLevelLightVertexConsumer is not abstract and does not override abstract method setLineWidth(float) in VertexConsumer
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:492: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:361: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:359: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:358: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:296: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:290: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:249: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:164: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:90: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:88: error: method does not override or implement a method from a supertype
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:49: error: EmbeddedPlotLevelAccessor is not abstract and does not override abstract method environmentAttributes() in LevelReader
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: z has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: x has private access in ChunkPos
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:83: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:81: error: method does not override or implement a method from a supertype
```

### Unique errors (first 800)
```
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:38: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/fabric/platform/SableChunkEventPlatformImpl.java:26: error: method onChunkLoad in interface Load cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:76: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:86: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/LivingEntityMixin.java:54: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:27: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/EntityMixin.java:332: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ChunkMapMixin.java:22: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ServerLevelMixin.java:19: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:118: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:129: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:144: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerLevelMixin.java:100: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:33: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:56: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:130: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:93: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:110: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/packets/tcp/ServerboundGizmoMoveSubLevelPacket.java:54: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/network/packets/udp/SableUDPEchoPacket.java:21: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:234: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:27: error: MovingSoundInstanceDelegate is not abstract and does not override abstract method getIdentifier() in SoundInstance
  sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:81: error: method does not override or implement a method from a supertype
  sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:83: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:49: error: EmbeddedPlotLevelAccessor is not abstract and does not override abstract method environmentAttributes() in LevelReader
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:88: error: method does not override or implement a method from a supertype
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:90: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:164: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:249: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:290: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:296: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:358: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:359: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:361: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:492: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:179: error: SubLevelLightVertexConsumerProvider.SubLevelLightVertexConsumer is not abstract and does not override abstract method setLineWidth(float) in VertexConsumer
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:66: error: method does not override or implement a method from a supertype
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/render/vanilla/VanillaChunkedSubLevelRenderData.java:194: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelOccupancySavedData.java:31: error: incompatible types: String cannot be converted to Identifier
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelTicketsSavedData.java:50: error: incompatible types: String cannot be converted to Identifier
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:14: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:15: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:138: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: x has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: z has private access in ChunkPos
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:206: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:246: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:271: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:280: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:309: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:448: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:529: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelStorage.java:44: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:115: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:165: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
  sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:430: error: cannot find symbol
  sable/src/main/java/dev/ryanhcode/sable/sublevel/tracking_points/SubLevelTrackingPointSavedData.java:53: error: incompatible types: String cannot be converted to Identifier
  sable/src/main/java/dev/ryanhcode/sable/util/LevelAccelerator.java:101: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:38: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/fabric/platform/SableChunkEventPlatformImpl.java:26: error: method onChunkLoad in interface Load cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:76: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:86: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/LivingEntityMixin.java:54: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:27: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/EntityMixin.java:332: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ChunkMapMixin.java:22: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ServerLevelMixin.java:19: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:118: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:129: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:144: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerLevelMixin.java:100: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:33: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:56: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:130: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:93: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:110: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/packets/tcp/ServerboundGizmoMoveSubLevelPacket.java:54: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/network/packets/udp/SableUDPEchoPacket.java:21: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:234: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:27: error: MovingSoundInstanceDelegate is not abstract and does not override abstract method getIdentifier() in SoundInstance
sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:81: error: method does not override or implement a method from a supertype
sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:83: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:49: error: EmbeddedPlotLevelAccessor is not abstract and does not override abstract method environmentAttributes() in LevelReader
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:88: error: method does not override or implement a method from a supertype
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:90: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:164: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:249: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:290: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:296: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:358: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:359: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:361: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:434: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:492: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:676: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:677: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:179: error: SubLevelLightVertexConsumerProvider.SubLevelLightVertexConsumer is not abstract and does not override abstract method setLineWidth(float) in VertexConsumer
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:29: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:38: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:50: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:66: error: method does not override or implement a method from a supertype
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/render/vanilla/VanillaChunkedSubLevelRenderData.java:194: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelOccupancySavedData.java:31: error: incompatible types: String cannot be converted to Identifier
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelTicketsSavedData.java:50: error: incompatible types: String cannot be converted to Identifier
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:14: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:15: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:138: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: x has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: z has private access in ChunkPos
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:206: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:246: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:271: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:280: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:309: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:448: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:529: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/serialization/SubLevelStorage.java:44: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:115: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:165: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:430: error: cannot find symbol
sable/src/main/java/dev/ryanhcode/sable/sublevel/tracking_points/SubLevelTrackingPointSavedData.java:53: error: incompatible types: String cannot be converted to Identifier
sable/src/main/java/dev/ryanhcode/sable/util/LevelAccelerator.java:101: error: cannot find symbol
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
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              final ChunkPos moveToChunk = new ChunkPos(BlockPos.containing(currentPosition.x, currentPosition.y, currentPosition.z));
                                           ^
    required: int,int
    found:    BlockPos
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              final ChunkPos chunkPos = new ChunkPos(longKey);
                                        ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              this.processUnload(new ChunkPos(l), forceLoaded);
                                 ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              this.processLoad(new ChunkPos(l));
                               ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:492: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                          .promotePartial(string -> logLoadingErrors(new ChunkPos(chunkPos), chunk.getSectionYFromSectionIndex(yIndex), string))
                                                                     ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                      level.getChunkSource().removeTicketWithRadius(vanillaTicket.getType(), new ChunkPos(chunkLong), 0);
                                                                                             ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/platform/SableChunkEventPlatformImpl.java:26: error: method onChunkLoad in interface Load cannot be applied to given types;
          ServerChunkEvents.CHUNK_LOAD.invoker().onChunkLoad((ServerLevel) chunk.getLevel(), chunk);
                                                ^
    required: ServerLevel,LevelChunk,boolean
    found:    ServerLevel,LevelChunk
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ServerLevelMixin.java:19: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
          final ChunkPos chunkPos = new ChunkPos(l);
                                    ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ChunkMapMixin.java:22: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
          final ChunkPos chunkPos = new ChunkPos(l);
                                    ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:33: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                  final LevelPlot plot = plotContainer.getPlot(new ChunkPos(blockPos));
                                                               ^
    required: int,int
    found:    BlockPos
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:56: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                  final LevelPlot plot = plotContainer.getPlot(new ChunkPos(blockPos));
                                                               ^
    required: int,int
    found:    BlockPos
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:118: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              final ChunkPos chunkPos = new ChunkPos(pos);
                                        ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:129: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
              final ChunkPos chunkPos = new ChunkPos(pos);
                                        ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:144: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
          final ChunkPos pos = new ChunkPos(blockPos);
                               ^
    required: int,int
    found:    BlockPos
    reason: actual and formal argument lists differ in length
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerLevelMixin.java:100: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
          if (plotContainer.getPlot(new ChunkPos(l)) != null) {
                                    ^
    required: int,int
    found:    long
    reason: actual and formal argument lists differ in length
  Note: Recompile with -Xlint:deprecation for details.
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: cannot find symbol
  import net.fabricmc.fabric.api.client.renderer.v1.render.BlockMultiBufferSource;
                                                          ^
    symbol:   class BlockMultiBufferSource
    location: package net.fabricmc.fabric.api.client.renderer.v1.render
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
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
  import net.minecraft.client.renderer.chunk.SectionBuffers;
                                            ^
    symbol:   class SectionBuffers
    location: package net.minecraft.client.renderer.chunk
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
  import net.minecraft.client.renderer.block.BlockRenderDispatcher;
                                            ^
    symbol:   class BlockRenderDispatcher
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
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:7: error: cannot find symbol
import net.fabricmc.fabric.api.client.renderer.v1.render.BlockMultiBufferSource;
                                                        ^
  symbol:   class BlockMultiBufferSource
  location: package net.fabricmc.fabric.api.client.renderer.v1.render
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
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:26: error: cannot find symbol
import net.minecraft.client.renderer.chunk.SectionBuffers;
                                          ^
  symbol:   class SectionBuffers
  location: package net.minecraft.client.renderer.chunk
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin.java:27: error: cannot find symbol
import net.minecraft.client.renderer.block.BlockRenderDispatcher;
                                          ^
  symbol:   class BlockRenderDispatcher
  location: package net.minecraft.client.renderer.block
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:138: error: cannot find symbol
        if (!this.loadedHoldingChunks.containsKey(chunkPos.toLong())) {
                                                          ^
  symbol:   method toLong()
  location: variable chunkPos of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: x has private access in ChunkPos
        final BoundingBox3d bounds = new BoundingBox3d(chunkPos.x << 4, -Double.MAX_VALUE, chunkPos.z << 4, (chunkPos.x << 4) + 16, Double.MAX_VALUE, (chunkPos.z << 4) + 16);
                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: z has private access in ChunkPos
        final BoundingBox3d bounds = new BoundingBox3d(chunkPos.x << 4, -Double.MAX_VALUE, chunkPos.z << 4, (chunkPos.x << 4) + 16, Double.MAX_VALUE, (chunkPos.z << 4) + 16);
                                                                                                   ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: x has private access in ChunkPos
        final BoundingBox3d bounds = new BoundingBox3d(chunkPos.x << 4, -Double.MAX_VALUE, chunkPos.z << 4, (chunkPos.x << 4) + 16, Double.MAX_VALUE, (chunkPos.z << 4) + 16);
                                                                                                                     ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:146: error: z has private access in ChunkPos
        final BoundingBox3d bounds = new BoundingBox3d(chunkPos.x << 4, -Double.MAX_VALUE, chunkPos.z << 4, (chunkPos.x << 4) + 16, Double.MAX_VALUE, (chunkPos.z << 4) + 16);
                                                                                                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:206: error: cannot find symbol
            Sable.LOGGER.info("Saving sub-levels for level '{}'/{}", this.level, this.level.dimension().location());
                                                                                                       ^
  symbol:   method location()
  location: class ResourceKey<Level>
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:234: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            final ChunkPos moveToChunk = new ChunkPos(BlockPos.containing(currentPosition.x, currentPosition.y, currentPosition.z));
                                         ^
  required: int,int
  found:    BlockPos
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:246: error: cannot find symbol
                final SubLevelHoldingChunk holdingChunk = this.loadedHoldingChunks.get(moveToChunk.toLong());
                                                                                                  ^
  symbol:   method toLong()
  location: variable moveToChunk of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:271: error: cannot find symbol
                final ChunkHolder chunkHolder = this.level.getChunkSource().chunkMap.visibleChunkMap.get(holdingChunkPos.toLong());
                                                                                                                        ^
  symbol:   method toLong()
  location: variable holdingChunkPos of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:280: error: cannot find symbol
            final SubLevelHoldingChunk holdingChunk = this.loadedHoldingChunks.get(unload.toLong());
                                                                                         ^
  symbol:   method toLong()
  location: variable unload of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:295: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            final ChunkPos chunkPos = new ChunkPos(longKey);
                                      ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:309: error: cannot find symbol
            this.loadedHoldingChunks.remove(unload.toLong());
                                                  ^
  symbol:   method toLong()
  location: variable unload of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:448: error: cannot find symbol
        final long longKey = chunkPos.toLong();
                                     ^
  symbol:   method toLong()
  location: variable chunkPos of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:529: error: cannot find symbol
        this.dirtyHoldingChunks.add(chunkPos.toLong());
                                            ^
  symbol:   method toLong()
  location: variable chunkPos of type ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:588: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            this.processUnload(new ChunkPos(l), forceLoaded);
                               ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/SubLevelHoldingChunkMap.java:592: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            this.processLoad(new ChunkPos(l));
                             ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:14: error: x has private access in ChunkPos
            Codec.INT.fieldOf("chunk_x").forGetter(x -> x.chunkPos().x),
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/holding/GlobalSavedSubLevelPointer.java:15: error: z has private access in ChunkPos
            Codec.INT.fieldOf("chunk_z").forGetter(x -> x.chunkPos().z),
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: x has private access in ChunkPos
        Sable.LOGGER.error("Recoverable errors when loading plot section [{}, {}, {}]: {}", chunkPos.x, y, chunkPos.z, errorText);
                                                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:135: error: z has private access in ChunkPos
        Sable.LOGGER.error("Recoverable errors when loading plot section [{}, {}, {}]: {}", chunkPos.x, y, chunkPos.z, errorText);
                                                                                                                   ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/ServerLevelPlot.java:164: error: cannot find symbol
            cache.chunkMap.updatingChunkMap.remove(pos.toLong());
                                                      ^
```

### Raw log tail (last 400 lines)
```
  location: class ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:165: error: cannot find symbol
                    final long chunkLong = ChunkPos.asLong(x, z);
                                                   ^
  symbol:   method asLong(int,int)
  location: class ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:299: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                    level.getChunkSource().removeTicketWithRadius(vanillaTicket.getType(), new ChunkPos(chunkLong), 0);
                                                                                           ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/system/ticket/PhysicsChunkTicketManager.java:430: error: cannot find symbol
        return distanceManager.inBlockTickingRange(ChunkPos.asLong(x, z));
                                                           ^
  symbol:   method asLong(int,int)
  location: class ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:49: error: EmbeddedPlotLevelAccessor is not abstract and does not override abstract method environmentAttributes() in LevelReader
public class EmbeddedPlotLevelAccessor implements CommonLevelAccessor, ServerLevelAccessor {
       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:88: error: method does not override or implement a method from a supertype
    @Override
    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:90: error: cannot find symbol
        return this.level.getShade(direction, shade);
                         ^
  symbol:   method getShade(Direction,boolean)
  location: variable level of type Level
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: x has private access in ChunkPos
        return this.level.getChunk(i + this.centerChunk.x, j + this.centerChunk.z, chunkStatus, bl);
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:130: error: z has private access in ChunkPos
        return this.level.getChunk(i + this.centerChunk.x, j + this.centerChunk.z, chunkStatus, bl);
                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: x has private access in ChunkPos
        return this.level.hasChunk(i + this.centerChunk.x, j + this.centerChunk.z);
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/plot/EmbeddedPlotLevelAccessor.java:171: error: z has private access in ChunkPos
        return this.level.hasChunk(i + this.centerChunk.x, j + this.centerChunk.z);
                                                                               ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/util/LevelAccelerator.java:101: error: cannot find symbol
        final long pos = ChunkPos.asLong(chunkX, chunkZ);
                                 ^
  symbol:   method asLong(int,int)
  location: class ChunkPos
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: x has private access in ChunkPos
        return this.getContaining(level, chunkPos.x, chunkPos.z);
                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:94: error: z has private access in ChunkPos
        return this.getContaining(level, chunkPos.x, chunkPos.z);
                                                             ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: x has private access in ChunkPos
        return this.isInPlotGrid(level, chunkPos.x, chunkPos.z);
                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/companion/SableCompanion.java:724: error: z has private access in ChunkPos
        return this.isInPlotGrid(level, chunkPos.x, chunkPos.z);
                                                            ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/fabric/platform/SableChunkEventPlatformImpl.java:26: error: method onChunkLoad in interface Load cannot be applied to given types;
        ServerChunkEvents.CHUNK_LOAD.invoker().onChunkLoad((ServerLevel) chunk.getLevel(), chunk);
                                              ^
  required: ServerLevel,LevelChunk,boolean
  found:    ServerLevel,LevelChunk
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/packets/tcp/ServerboundGizmoMoveSubLevelPacket.java:54: error: cannot find symbol
        if (!context.player().hasPermissions(1)) {
                             ^
  symbol:   method hasPermissions(int)
  location: class Player
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/network/packets/udp/SableUDPEchoPacket.java:21: error: cannot find symbol
        Minecraft.getInstance().player.displayClientMessage(Component.literal("Received UDP Test Ping: " + this.text), false);
                                      ^
  symbol:   method displayClientMessage(MutableComponent,boolean)
  location: variable player of type LocalPlayer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:234: error: cannot find symbol
                        || blockState.getLightBlock() <= 0 && !blockState.useShapeForLightOcclusion()) {
                                     ^
  symbol:   method getLightBlock()
  location: variable blockState of type BlockState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error: cannot find symbol
                        || blockState.getLightBlock() > existingState.getLightBlock()
                                     ^
  symbol:   method getLightBlock()
  location: variable blockState of type BlockState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:244: error: cannot find symbol
                        || blockState.getLightBlock() > existingState.getLightBlock()
                                                                     ^
  symbol:   method getLightBlock()
  location: variable existingState of type BlockState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error: cannot find symbol
                        || blockState.getLightBlock() == existingState.getLightBlock()
                                     ^
  symbol:   method getLightBlock()
  location: variable blockState of type BlockState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/render/SubLevelDynamicLights.java:245: error: cannot find symbol
                        || blockState.getLightBlock() == existingState.getLightBlock()
                                                                      ^
  symbol:   method getLightBlock()
  location: variable existingState of type BlockState
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/tracking_points/SubLevelTrackingPointSavedData.java:53: error: incompatible types: String cannot be converted to Identifier
                        SubLevelTrackingPointSavedData.FILE_ID,
                                                      ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelOccupancySavedData.java:31: error: incompatible types: String cannot be converted to Identifier
                        SubLevelOccupancySavedData.FILE_ID,
                                                  ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/storage/SubLevelTicketsSavedData.java:50: error: incompatible types: String cannot be converted to Identifier
                        SubLevelTicketsSavedData.FILE_ID,
                                                ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:66: error: method does not override or implement a method from a supertype
    @Override
    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/SubLevelLightVertexConsumerProvider.java:179: error: SubLevelLightVertexConsumerProvider.SubLevelLightVertexConsumer is not abstract and does not override abstract method setLineWidth(float) in VertexConsumer
    private final class SubLevelLightVertexConsumer implements VertexConsumer {
                  ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sublevel/render/vanilla/VanillaChunkedSubLevelRenderData.java:194: error: cannot find symbol
        final Vector3d cameraPos = JOMLConversion.atCenterOf(camera.getBlockPosition()).sub(8, 8, 8);
                                                                   ^
  symbol:   method getBlockPosition()
  location: variable camera of type Camera
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:38: error: cannot find symbol
        getLightEngine(engine).removeChunkTasks(pos);
                              ^
  symbol:   method removeChunkTasks(ChunkPos)
  location: class StarLightInterface
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:48: warning: [removal] getLightEngine() in StarLightLightingProvider has been deprecated and marked for removal
        return provider.getLightEngine();
                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: x has private access in ChunkPos
        return this.getContaining(level, chunkPos.x, chunkPos.z);
                                                 ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:83: error: z has private access in ChunkPos
        return this.getContaining(level, chunkPos.x, chunkPos.z);
                                                             ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: x has private access in ChunkPos
        return this.getContaining(entity.level(), chunkPos.x, chunkPos.z);
                                                          ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:114: error: z has private access in ChunkPos
        return this.getContaining(entity.level(), chunkPos.x, chunkPos.z);
                                                                      ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: x has private access in ChunkPos
        return (ClientSubLevel) this.getContaining(SableDistUtil.getClientLevel(), chunkPos.x, chunkPos.z);
                                                                                           ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:130: error: z has private access in ChunkPos
        return (ClientSubLevel) this.getContaining(SableDistUtil.getClientLevel(), chunkPos.x, chunkPos.z);
                                                                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: x has private access in ChunkPos
        return (ClientSubLevel) this.getContaining(entity.level(), chunkPos.x, chunkPos.z);
                                                                           ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/ActiveSableCompanion.java:161: error: z has private access in ChunkPos
        return (ClientSubLevel) this.getContaining(entity.level(), chunkPos.x, chunkPos.z);
                                                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/EntityMixin.java:332: error: cannot find symbol
            if (!this.getBoundingBox().intersects(containingSubLevel.getPlot().getBoundingBox().toAABB().inflate(1.0)) && this.getType().is(SableTags.DESTROY_WHEN_LEAVING_PLOT)) {
                                                                                                                                        ^
  symbol:   method is(TagKey<EntityType<?>>)
  location: class EntityType<CAP#1>
  where CAP#1 is a fresh type-variable:
    CAP#1 extends Entity from capture of ?
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_sublevel_collision/AbstractMinecartMixin.java:27: error: cannot find symbol
        if (!this.getType().is(SableTags.DESTROY_WHEN_LEAVING_PLOT)) {
                           ^
  symbol:   method is(TagKey<EntityType<?>>)
  location: class EntityType<CAP#1>
  where CAP#1 is a fresh type-variable:
    CAP#1 extends Entity from capture of ?
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/entity_rotations_and_riding/LivingEntityMixin.java:54: error: cannot find symbol
            this.hasImpulse = true;
                ^
  symbol: variable hasImpulse
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ServerLevelMixin.java:19: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
        final ChunkPos chunkPos = new ChunkPos(l);
                                  ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/entity/server_entities_tick/ChunkMapMixin.java:22: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
        final ChunkPos chunkPos = new ChunkPos(l);
                                  ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:33: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                final LevelPlot plot = plotContainer.getPlot(new ChunkPos(blockPos));
                                                             ^
  required: int,int
  found:    BlockPos
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/lighting/BlockAndTintGetterMixin.java:56: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
                final LevelPlot plot = plotContainer.getPlot(new ChunkPos(blockPos));
                                                             ^
  required: int,int
  found:    BlockPos
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:118: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            final ChunkPos chunkPos = new ChunkPos(pos);
                                      ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:129: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
            final ChunkPos chunkPos = new ChunkPos(pos);
                                      ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerChunkCacheMixin.java:144: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
        final ChunkPos pos = new ChunkPos(blockPos);
                             ^
  required: int,int
  found:    BlockPos
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/plot/ServerLevelMixin.java:100: error: constructor ChunkPos in record ChunkPos cannot be applied to given types;
        if (plotContainer.getPlot(new ChunkPos(l)) != null) {
                                  ^
  required: int,int
  found:    long
  reason: actual and formal argument lists differ in length
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:27: error: MovingSoundInstanceDelegate is not abstract and does not override abstract method getIdentifier() in SoundInstance
public class MovingSoundInstanceDelegate implements SoundInstance, TickableSoundInstance {
       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:81: error: method does not override or implement a method from a supertype
    @Override
    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/sound/MovingSoundInstanceDelegate.java:83: error: cannot find symbol
        return this.instance.getLocation();
                            ^
  symbol:   method getLocation()
  location: variable instance of type SoundInstance
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:76: error: cannot find symbol
            this.player.displayClientMessage(Component.translatable("camera_type.sub_level_view").withColor(0xffaaaaaa), true);
                       ^
  symbol:   method displayClientMessage(MutableComponent,boolean)
  location: variable player of type LocalPlayer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/camera/new_camera_types/MinecraftMixin.java:86: error: cannot find symbol
            this.player.displayClientMessage(Component.translatable("camera_type.sub_level_view_unlocked").withColor(0xffaaaaaa), true);
                       ^
  symbol:   method displayClientMessage(MutableComponent,boolean)
  location: variable player of type LocalPlayer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:93: error: cannot find symbol
        final Vec3 cameraPosition = camera.getPosition();
                                          ^
  symbol:   method getPosition()
  location: variable camera of type Camera
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/block_entity_render/LevelRendererMixin.java:130: error: cannot find symbol
                            renderState.lightCoords = LevelRenderer.getLightColor(
                                                                   ^
  symbol:   method getLightColor(ClientLevel,BlockPos)
  location: class LevelRenderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/mixin/sublevel_render/impl/vanilla/LevelRendererMixin.java:110: error: cannot find symbol
            final List<RenderPass.Draw<GpuBufferSlice[]>> existingDraws = original.drawsPerLayer().get(layer);
                                                                                  ^
  symbol:   method drawsPerLayer()
  location: variable original of type ChunkSectionsToRender
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


BUILD FAILED in 43s
1 actionable task: 1 executed
```
