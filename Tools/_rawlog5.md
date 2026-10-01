# Compile report - Minecraft 26.1.2 port

- commit: `a4cfd04295dfb3d53fe298ede58367a2d1ba0f74`
- ref: `port/26.1.2`
- date: 2026-10-01T08:53:50Z

## Result: BUILD FAILED

Total `error:` lines: 801
Total `error:` (unique): 522

### Top error sources
```
     12 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error:
      9 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:432: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:20: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:18: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:741: error:
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:74: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:5: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:59: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:58: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:73: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:65: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:31: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:30: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:21: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:20: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:18: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:82: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:34: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/rope/RopeStrandElement.java:19: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:97: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:56: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:29: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:13: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:29: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:23: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:15: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:38: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:31: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:6: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:230: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:225: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:212: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:65: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:139: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:134: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:129: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimBlocks.java:18: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:6: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimInventoryService.java:22: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:12: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:11: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/SimulatedDataGenerator.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:9: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:75: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:10: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:20: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:126: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:17: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:4: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:43: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:7: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:24: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:5: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:14: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:8: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:62: error:
      3 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:74: error:
```

### Errors grouped by package
```
     45 com/tterrag/registrate/providers/RegistrateItemModelProvider.java
     27 com/tterrag/registrate/providers/RegistrateBlockstateProvider.java
     18 com/tterrag/registrate/builders/BlockBuilder.java
     15 com/zurrtum/create/foundation/data/BlockStateGen.java
     12 com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java
      9 com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java
      9 com/zurrtum/create/foundation/data/AssetLookup.java
      9 com/tterrag/registrate/providers/RegistrateGenericProvider.java
      9 com/tterrag/registrate/providers/RegistrateDataProvider.java
      9 com/tterrag/registrate/builders/FluidBuilder.java
      6 com/zurrtum/create/foundation/data/SpecialBlockStateGen.java
      6 com/tterrag/registrate/providers/RegistrateItemTagsProvider.java
      6 com/tterrag/registrate/providers/RegistrateAdvancementProvider.java
      6 com/tterrag/registrate/providers/ProviderType.java
      6 com/tterrag/registrate/fabric/FluidData.java
      6 com/tterrag/registrate/AbstractRegistrate.java
      6 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:432: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:741: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error: cannot find symbol
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package MultiPartBlockStateBuilder does not exist
      4 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package ConfiguredModel does not exist
      3 com/tterrag/registrate/util/package-info.java
      3 com/tterrag/registrate/util/nullness/package-info.java
      3 com/tterrag/registrate/util/entry/package-info.java
      3 com/tterrag/registrate/providers/package-info.java
      3 com/tterrag/registrate/providers/loot/package-info.java
      3 com/tterrag/registrate/providers/RegistrateRecipeProvider.java
      3 com/tterrag/registrate/providers/RegistrateLangProvider.java
      3 com/tterrag/registrate/package-info.java
      3 com/tterrag/registrate/builders/package-info.java
      3   /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:432: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:9: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:74: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:5: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:59: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:9: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:58: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:73: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:65: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:31: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:30: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:21: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:20: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:18: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:13: error: package foundry.veil.impl.client.render.perspective does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:12: error: package foundry.veil.api.client.render.framebuffer does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:11: error: package foundry.veil.api.client.render does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:82: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:34: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:13: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/rope/RopeStrandElement.java:19: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:97: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:13: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:9: error: package EndDragonFight does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:4: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:56: error: package EndDragonFight does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:29: error: package EndDragonFight does not exist
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:11: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:13: error: cannot find symbol
      2 /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:12: error: cannot find symbol
```

### Unique errors (first 800)
```
  simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:294: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:80: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:13: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:16: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:17: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:18: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:255: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:86: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:29: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:30: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:31: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/builders/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/fabric/FluidData.java:6: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/fabric/FluidData.java:7: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/ProviderType.java:11: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/ProviderType.java:63: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateAdvancementProvider.java:16: error: package io.github.fabricators_of_create.porting_lib.conditions does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateAdvancementProvider.java:17: error: package io.github.fabricators_of_create.porting_lib.conditions does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:16: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:20: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:40: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:45: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:52: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:8: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:18: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:51: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:53: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:22: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:4: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:71: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:170: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:174: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:178: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:182: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:186: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:18: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:190: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:194: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:19: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:202: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:206: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:20: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:30: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:36: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:8: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemTagsProvider.java:14: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemTagsProvider.java:27: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateLangProvider.java:9: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/RegistrateRecipeProvider.java:7: error: package io.github.fabricators_of_create.porting_lib.tags does not exist
  simulated/src/main/java/com/tterrag/registrate/providers/loot/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/providers/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/util/entry/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/util/nullness/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/tterrag/registrate/util/package-info.java:2: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:17: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:21: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:7: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:24: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:28: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:32: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:6: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:7: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/zurrtum/create/foundation/data/SpecialBlockStateGen.java:14: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/data/SpecialBlockStateGen.java:5: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:12: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:16: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:3: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:6: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:11: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:5: error: cannot find symbol
  simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:18: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:4: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:5: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:6: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/KineticBlockEntityRenderer.java:9: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:183: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:22: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:23: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:26: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:284: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:28: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:308: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/compat/jei/SimulatedJEI.java:15: error: package mezz.jei.library.ingredients.itemStacks does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/auger_shaft/AugerShaftBlock.java:22: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/auger_shaft/AugerShaftBlock.java:269: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:57: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:100: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:112: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:143: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:93: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nav_table/NavTableRenderer.java:19: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nav_table/navigation_target/RenderableNavigationTarget.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/physics_assembler/PhysicsAssemblerGUIHandler.java:126: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/physics_assembler/PhysicsAssemblerGUIHandler.java:14: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:99: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:11: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:196: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:87: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterMenuCommon.java:15: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterMenuCommon.java:93: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:166: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:188: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:24: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/ConfirmationWidgetBase.java:26: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/ConfirmationWidgetBase.java:6: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:38: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:61: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:24: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:103: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:17: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:180: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:12: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package ConfiguredModel does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package MultiPartBlockStateBuilder does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:72: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/rope/RopeStrandHolderBehavior.java:46: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:35: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:12: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:42: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:20: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:21: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:22: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:23: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelVisual.java:18: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:11: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:51: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:42: error: package VeilRenderLevelStageEvent does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:43: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:4: error: package foundry.veil.api.client.render does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:5: error: package foundry.veil.api.event does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/DiagramEntity.java:51: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramButton.java:49: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramButton.java:5: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:69: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:91: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:1025: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:1045: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:23: error: package foundry.veil.api.client.render does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:24: error: package foundry.veil.api.client.render does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:25: error: package foundry.veil.api.client.render.framebuffer does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:26: error: package foundry.veil.api.client.render.post does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:27: error: package foundry.veil.api.client.render.post does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:35: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:432: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:465: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:584: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:660: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:674: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:741: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:750: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:811: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:933: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:970: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:97: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:98: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:99: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:10: error: package foundry.veil.api.client.render does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:11: error: package foundry.veil.api.client.render.framebuffer does not exist
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:181: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:255: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:48: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:49: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:50: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:14: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:74: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:62: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:14: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:5: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:24: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:7: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:43: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:4: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:17: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:4: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:126: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:20: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:18: error: package ConfiguredModel does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:18: error: package MultiPartBlockStateBuilder does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:20: error: package ConfiguredModel does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:20: error: package MultiPartBlockStateBuilder does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:75: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:8: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/data/SimulatedDataGenerator.java:7: error: package io.github.fabricators_of_create.porting_lib.data does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:12: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimInventoryService.java:22: error: package team.reborn.energy.api does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:6: error: package team.reborn.energy.api does not exist
  simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimBlocks.java:18: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
  simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:129: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:134: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:139: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:8: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:10: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:65: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:12: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:14: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:212: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:225: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:230: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:6: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:10: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:31: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:10: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:38: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:15: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:7: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:23: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:29: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:7: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:12: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:11: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:29: error: package EndDragonFight does not exist
  simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:56: error: package EndDragonFight does not exist
  simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:4: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:9: error: package EndDragonFight does not exist
  simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:97: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/rope/RopeStrandElement.java:19: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:13: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:34: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:82: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:11: error: package foundry.veil.api.client.render does not exist
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:12: error: package foundry.veil.api.client.render.framebuffer does not exist
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:13: error: package foundry.veil.impl.client.render.perspective does not exist
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:18: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:20: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:21: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:30: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:31: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:65: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:73: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:58: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:9: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:59: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:5: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:74: error: cannot find symbol
  simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:9: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:294: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:80: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:13: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:16: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:17: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:18: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:255: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:86: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:29: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:30: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:31: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/builders/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/fabric/FluidData.java:6: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/fabric/FluidData.java:7: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/ProviderType.java:11: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/ProviderType.java:63: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateAdvancementProvider.java:16: error: package io.github.fabricators_of_create.porting_lib.conditions does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateAdvancementProvider.java:17: error: package io.github.fabricators_of_create.porting_lib.conditions does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:16: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:20: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:40: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:45: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:52: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:8: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:18: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:51: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:53: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:22: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:4: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateGenericProvider.java:71: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:170: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:174: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:178: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:182: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:186: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:18: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:190: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:194: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:19: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:202: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:206: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:20: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:30: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:36: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemModelProvider.java:8: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemTagsProvider.java:14: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateItemTagsProvider.java:27: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateLangProvider.java:9: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/com/tterrag/registrate/providers/RegistrateRecipeProvider.java:7: error: package io.github.fabricators_of_create.porting_lib.tags does not exist
simulated/src/main/java/com/tterrag/registrate/providers/loot/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/providers/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/util/entry/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/util/nullness/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/tterrag/registrate/util/package-info.java:2: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:17: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:21: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/AssetLookup.java:7: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:24: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:28: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:32: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:6: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:7: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/zurrtum/create/foundation/data/SpecialBlockStateGen.java:14: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/data/SpecialBlockStateGen.java:5: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:12: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:16: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:3: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:6: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:11: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:5: error: cannot find symbol
simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:18: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:4: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:5: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:6: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/client/model/BakedItemModelPart.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/KineticBlockEntityRenderer.java:9: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:183: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:22: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:23: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:26: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:284: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:28: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/create/SableCreateBlockEntityRenderer.java:308: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/compat/jei/SimulatedJEI.java:15: error: package mezz.jei.library.ingredients.itemStacks does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/auger_shaft/AugerShaftBlock.java:22: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/auger_shaft/AugerShaftBlock.java:269: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:57: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:100: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:112: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:143: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nameplate/NameplateScreen.java:93: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nav_table/NavTableRenderer.java:19: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/nav_table/navigation_target/RenderableNavigationTarget.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/physics_assembler/PhysicsAssemblerGUIHandler.java:126: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/physics_assembler/PhysicsAssemblerGUIHandler.java:14: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:99: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:11: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:196: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:87: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterMenuCommon.java:15: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterMenuCommon.java:93: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:166: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:188: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:24: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/ConfirmationWidgetBase.java:26: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/ConfirmationWidgetBase.java:6: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:38: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:61: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:24: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:103: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:17: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/modulating_receiver/ModulatingLinkedReceiverScreen.java:180: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:12: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package ConfiguredModel does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:15: error: package MultiPartBlockStateBuilder does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/redstone_accumulator/RedstoneAccumulatorBlockStateGen.java:72: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/rope/RopeStrandHolderBehavior.java:46: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:35: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:12: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:42: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:20: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:21: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:22: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:23: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelVisual.java:18: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:11: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:51: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:42: error: package VeilRenderLevelStageEvent does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:43: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:4: error: package foundry.veil.api.client.render does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/end_sea/EndSeaShadowRenderer.java:5: error: package foundry.veil.api.event does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/DiagramEntity.java:51: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramButton.java:49: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramButton.java:5: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:69: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramForceGroupToggle.java:91: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:1025: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:1045: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:23: error: package foundry.veil.api.client.render does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:24: error: package foundry.veil.api.client.render does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:25: error: package foundry.veil.api.client.render.framebuffer does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:26: error: package foundry.veil.api.client.render.post does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:27: error: package foundry.veil.api.client.render.post does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:35: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:432: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:465: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:584: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:660: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:674: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:741: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:750: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:811: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:933: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:970: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:97: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:98: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramScreen.java:99: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:10: error: package foundry.veil.api.client.render does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:11: error: package foundry.veil.api.client.render.framebuffer does not exist
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:181: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:255: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:48: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:49: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/entities/diagram/screen/DiagramStickyNote.java:50: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:14: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:74: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:62: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:14: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:5: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:24: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:7: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:43: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimpleSimulatedTrigger.java:4: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:17: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/data/advancements/SimulatedCriterionTriggerBase.java:4: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:126: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/events/SimulatedCommonClientEvents.java:20: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:18: error: package ConfiguredModel does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:18: error: package MultiPartBlockStateBuilder does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:20: error: package ConfiguredModel does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:20: error: package MultiPartBlockStateBuilder does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:75: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:8: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/FabricAugerShaftGen.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/data/SimulatedDataGenerator.java:7: error: package io.github.fabricators_of_create.porting_lib.data does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimBlockStateService.java:12: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/service/FabricSimInventoryService.java:22: error: package team.reborn.energy.api does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:6: error: package team.reborn.energy.api does not exist
simulated/src/main/java/dev/simulated_team/simulated/fabric/transfer/SingleBatteryStorage.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimBlocks.java:18: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:129: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:134: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:139: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimGUITextures.java:8: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:10: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:65: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:12: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:14: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:212: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:225: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:230: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:6: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:10: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/creative_tab_sections/CreativeModeInventoryScreenMixin.java:31: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:10: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/hold_interaction/GoggleOverlayRendererMixin.java:38: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:15: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:7: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:23: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:29: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/ponder/TextWindowElementMixin.java:7: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:12: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/CreateWorldScreenMixin.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:11: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:29: error: package EndDragonFight does not exist
simulated/src/main/java/dev/simulated_team/simulated/mixin/world_presets/PrimaryLevelDataMixin.java:56: error: package EndDragonFight does not exist
simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:4: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/mixin_interface/PrimaryLevelDataExtension.java:9: error: package EndDragonFight does not exist
simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/KeybindWindowElement.java:97: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/ponder/elements/rope/RopeStrandElement.java:19: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:13: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:34: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/registrate/simulated_tab/SimulatedCreativeTab.java:82: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:11: error: package foundry.veil.api.client.render does not exist
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:12: error: package foundry.veil.api.client.render.framebuffer does not exist
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:13: error: package foundry.veil.impl.client.render.perspective does not exist
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:18: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:20: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:21: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:30: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:31: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:65: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/SimpleSubLevelGroupRenderer.java:73: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:58: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/BlockHoldInteraction.java:9: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:59: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldInteractionManager.java:5: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:74: error: cannot find symbol
simulated/src/main/java/dev/simulated_team/simulated/util/hold_interaction/HoldTipManager.java:9: error: cannot find symbol
```

### Missing symbols (top 120)
```
```

### Gradle failure block
```
FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':simulated:compileJava' (registered by plugin class 'org.gradle.api.plugins.JavaBasePlugin').
> Compilation failed; see the compiler output below.
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:3: error: cannot find symbol
  import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                  ^
    symbol:   class SimpleModelWrapper
    location: package net.minecraft.client.renderer.block.model
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:6: error: cannot find symbol
      private final SimpleModelWrapper originalModel;
                    ^
    symbol:   class SimpleModelWrapper
    location: class CustomRenderedItemModel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:12: error: cannot find symbol
      public CustomRenderedItemModel(SimpleModelWrapper originalModel) {
                                     ^
    symbol:   class SimpleModelWrapper
    location: class CustomRenderedItemModel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:16: error: cannot find symbol
      public SimpleModelWrapper getOriginalModel() {
             ^
    symbol:   class SimpleModelWrapper
    location: class CustomRenderedItemModel
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:5: error: cannot find symbol
  import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                  ^
    symbol:   class SimpleModelWrapper
    location: package net.minecraft.client.renderer.block.model
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:8: error: cannot find symbol
      public void render(SimpleModelWrapper model, int light) {
                         ^
    symbol:   class SimpleModelWrapper
    location: class PartialItemModelRenderer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:11: error: cannot find symbol
      public void render(SimpleModelWrapper model, RenderType type, int light) {
                         ^
    symbol:   class SimpleModelWrapper
    location: class PartialItemModelRenderer
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:24: error: cannot find symbol
                                                                 BiFunction<BlockState, Boolean, ModelFile> models) {
                                                                                                 ^
    symbol:   class ModelFile
    location: class BlockStateGen
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:28: error: cannot find symbol
                                                     Function<BlockState, ModelFile> models) {
                                                                          ^
    symbol:   class ModelFile
    location: class BlockStateGen
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:32: error: cannot find symbol
                                                        Function<BlockState, ModelFile> models) {
                                                                             ^
    symbol:   class ModelFile
    location: class BlockStateGen
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:20: error: cannot find symbol
      public RegistrateBlockstateProvider(AbstractRegistrate<?> parent, PackOutput packOutput, ExistingFileHelper exFileHelper) {
                                                                                               ^
    symbol:   class ExistingFileHelper
    location: class RegistrateBlockstateProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:40: error: cannot find symbol
      ExistingFileHelper getExistingFileHelper() {
      ^
    symbol:   class ExistingFileHelper
    location: class RegistrateBlockstateProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:45: error: cannot find symbol
      public Optional<VariantBlockStateBuilder> getExistingVariantBuilder(Block block) {
                      ^
    symbol:   class VariantBlockStateBuilder
    location: class RegistrateBlockstateProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:52: error: cannot find symbol
      public Optional<MultiPartBlockStateBuilder> getExistingMultipartBuilder(Block block) {
                      ^
    symbol:   class MultiPartBlockStateBuilder
    location: class RegistrateBlockstateProvider
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:294: error: cannot find symbol
      public void setupDatagen(FabricDataGenerator.Pack pack, ExistingFileHelper existingFileHelper) {
                                                              ^
    symbol:   class ExistingFileHelper
    location: class AbstractRegistrate<S>
    where S is a type-variable:
      S extends AbstractRegistrate<S> declared in class AbstractRegistrate
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:16: error: cannot find symbol
  import net.fabricmc.fabric.api.client.rendering.v1.ChunkSectionLayerMap;
                                                    ^
    symbol:   class ChunkSectionLayerMap
    location: package net.fabricmc.fabric.api.client.rendering.v1
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:17: error: cannot find symbol
  import net.fabricmc.fabric.api.client.rendering.v1.ColorProviderRegistry;
                                                    ^
    symbol:   class ColorProviderRegistry
    location: package net.fabricmc.fabric.api.client.rendering.v1
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:18: error: cannot find symbol
  import net.minecraft.client.color.block.BlockColor;
                                         ^
    symbol:   class BlockColor
    location: package net.minecraft.client.color.block
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:29: error: cannot find symbol
  import net.fabricmc.fabric.api.client.rendering.v1.ChunkSectionLayerMap;
                                                    ^
    symbol:   class ChunkSectionLayerMap
    location: package net.fabricmc.fabric.api.client.rendering.v1
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:30: error: cannot find symbol
  import net.fabricmc.fabric.api.client.render.fluid.v1.FluidRenderHandlerRegistry;
                                                       ^
    symbol:   class FluidRenderHandlerRegistry
    location: package net.fabricmc.fabric.api.client.render.fluid.v1
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/FluidBuilder.java:31: error: cannot find symbol
  import net.fabricmc.fabric.api.client.render.fluid.v1.SimpleFluidRenderHandler;
                                                       ^
    symbol:   class SimpleFluidRenderHandler
    location: package net.fabricmc.fabric.api.client.render.fluid.v1
  /home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:86: error: cannot find symbol
      private NonNullSupplier<Supplier<BlockColor>> colorHandler;
                                       ^
    symbol:   class BlockColor
    location: class BlockBuilder<T,P>
    where T,P are type-variables:
      T extends Block declared in class BlockBuilder
      P extends Object declared in class BlockBuilder
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
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/sable/src/main/java/dev/ryanhcode/sable/compatibility/scalablelux/ScalableLuxCompat.java:91: warning: [removal] getLightEngine() in StarLightLightingProvider has been deprecated and marked for removal
        return provider.getLightEngine();
                       ^
Note: Some input files use or override a deprecated API.
Note: Recompile with -Xlint:deprecation for details.
Note: Some input files use unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
1 warning

> Task :simulated:compileJava
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:3: error: cannot find symbol
import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                ^
  symbol:   class SimpleModelWrapper
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:6: error: cannot find symbol
    private final SimpleModelWrapper originalModel;
                  ^
  symbol:   class SimpleModelWrapper
  location: class CustomRenderedItemModel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:12: error: cannot find symbol
    public CustomRenderedItemModel(SimpleModelWrapper originalModel) {
                                   ^
  symbol:   class SimpleModelWrapper
  location: class CustomRenderedItemModel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/CustomRenderedItemModel.java:16: error: cannot find symbol
    public SimpleModelWrapper getOriginalModel() {
           ^
  symbol:   class SimpleModelWrapper
  location: class CustomRenderedItemModel
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:5: error: cannot find symbol
import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                ^
  symbol:   class SimpleModelWrapper
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:8: error: cannot find symbol
    public void render(SimpleModelWrapper model, int light) {
                       ^
  symbol:   class SimpleModelWrapper
  location: class PartialItemModelRenderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/item/render/PartialItemModelRenderer.java:11: error: cannot find symbol
    public void render(SimpleModelWrapper model, RenderType type, int light) {
                       ^
  symbol:   class SimpleModelWrapper
  location: class PartialItemModelRenderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:6: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ConfiguredModel;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:7: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ModelFile;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:8: error: package io.github.fabricators_of_create.porting_lib.data does not exist
import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.BlockStateProvider;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.MultiPartBlockStateBuilder;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.VariantBlockStateBuilder;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:16: error: cannot find symbol
public class RegistrateBlockstateProvider extends BlockStateProvider implements RegistrateProvider {
                                                  ^
  symbol: class BlockStateProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:24: error: cannot find symbol
                                                               BiFunction<BlockState, Boolean, ModelFile> models) {
                                                                                               ^
  symbol:   class ModelFile
  location: class BlockStateGen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:28: error: cannot find symbol
                                                   Function<BlockState, ModelFile> models) {
                                                                        ^
  symbol:   class ModelFile
  location: class BlockStateGen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/zurrtum/create/foundation/data/BlockStateGen.java:32: error: cannot find symbol
                                                      Function<BlockState, ModelFile> models) {
                                                                           ^
  symbol:   class ModelFile
  location: class BlockStateGen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:80: error: package io.github.fabricators_of_create.porting_lib.data does not exist
import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:20: error: cannot find symbol
    public RegistrateBlockstateProvider(AbstractRegistrate<?> parent, PackOutput packOutput, ExistingFileHelper exFileHelper) {
                                                                                             ^
  symbol:   class ExistingFileHelper
  location: class RegistrateBlockstateProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:40: error: cannot find symbol
    ExistingFileHelper getExistingFileHelper() {
    ^
  symbol:   class ExistingFileHelper
  location: class RegistrateBlockstateProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:45: error: cannot find symbol
    public Optional<VariantBlockStateBuilder> getExistingVariantBuilder(Block block) {
                    ^
  symbol:   class VariantBlockStateBuilder
  location: class RegistrateBlockstateProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateBlockstateProvider.java:52: error: cannot find symbol
    public Optional<MultiPartBlockStateBuilder> getExistingMultipartBuilder(Block block) {
                    ^
  symbol:   class MultiPartBlockStateBuilder
  location: class RegistrateBlockstateProvider
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/ProviderType.java:11: error: package io.github.fabricators_of_create.porting_lib.data does not exist
import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/RegistrateDataProvider.java:18: error: package io.github.fabricators_of_create.porting_lib.data does not exist
import io.github.fabricators_of_create.porting_lib.data.ExistingFileHelper;
                                                       ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/AbstractRegistrate.java:294: error: cannot find symbol
    public void setupDatagen(FabricDataGenerator.Pack pack, ExistingFileHelper existingFileHelper) {
                                                            ^
  symbol:   class ExistingFileHelper
  location: class AbstractRegistrate<S>
  where S is a type-variable:
    S extends AbstractRegistrate<S> declared in class AbstractRegistrate
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:13: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.BlockStateProvider;
```

### Raw log tail (last 400 lines)
```
    public void doRender(final GuiGraphics graphics, final int mouseX, final int mouseY,
                               ^
  symbol:   class GuiGraphics
  location: class ConfirmationWidgetBase
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/KeyEditorScreen.java:196: error: cannot find symbol
        private void renderBackground(final GuiGraphics graphics, final int index) {
                                            ^
  symbol:   class GuiGraphics
  location: class KeyEditorScreen.KeyEntryWidget
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:13: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:13: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:166: error: cannot find symbol
    protected void renderBg(final GuiGraphics graphics, final float partialTick,
                                  ^
  symbol:   class GuiGraphics
  location: class LinkedTypewriterScreen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/LinkedTypewriterScreen.java:188: error: cannot find symbol
    private void renderTypewriter(final GuiGraphics graphics) {
                                        ^
  symbol:   class GuiGraphics
  location: class LinkedTypewriterScreen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:38: error: cannot find symbol
    protected void renderWidget(final GuiGraphics graphics, final int mouseX, final int mouseY,
                                      ^
  symbol:   class GuiGraphics
  location: class KeyWidget
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/KeyWidget.java:61: error: cannot find symbol
    private void renderHover(final GuiGraphics graphics) {
                                   ^
  symbol:   class GuiGraphics
  location: class KeyWidget
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:8: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/EntryModifierScreen.java:99: error: cannot find symbol
    public void renderBackground(final GuiGraphics graphics) {
                                       ^
  symbol:   class GuiGraphics
  location: class EntryModifierScreen
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/redstone/linked_typewriter/screen/widgets/PromptWidget.java:24: error: cannot find symbol
    protected void doRender(final GuiGraphics graphics, final int mouseX, final int mouseY,
                                  ^
  symbol:   class GuiGraphics
  location: class PromptWidget
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:11: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/throttle_lever/ThrottleLeverHandler.java:51: error: cannot find symbol
    public void renderOverlay(final GuiGraphics graphics, final int width, final int height, final boolean hideGui) {
                                    ^
  symbol:   class GuiGraphics
  location: class ThrottleLeverHandler
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:9: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ModelFile;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.MultiPartBlockStateBuilder;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/directional_gearshift/DirectionalGearshiftGenerator.java:57: error: cannot find symbol
    private static ModelFile model(final RegistrateBlockstateProvider p, final String part, final boolean powered, final boolean vertical) {
                   ^
  symbol:   class ModelFile
  location: class DirectionalGearshiftGenerator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/auger_shaft/AugerShaftBlock.java:269: error: cannot find symbol
    @MethodsReturnNonnullByDefault
     ^
  symbol:   class MethodsReturnNonnullByDefault
  location: class AugerShaftBlock
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:10: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ConfiguredModel;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:11: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ModelFile;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelGenerator.java:35: error: cannot find symbol
    public <T extends Block> ModelFile getModel(final DataGenContext<Block, T> ctx, final RegistrateBlockstateProvider prov, final BlockState state) {
                             ^
  symbol:   class ModelFile
  location: class SteeringWheelGenerator
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelVisual.java:18: error: cannot find symbol
import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                ^
  symbol:   class SimpleModelWrapper
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:20: error: cannot find symbol
import net.minecraft.client.renderer.block.model.BakedQuad;
                                                ^
  symbol:   class BakedQuad
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:21: error: cannot find symbol
import net.minecraft.client.renderer.block.model.BlockModelPart;
                                                ^
  symbol:   class BlockModelPart
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:22: error: cannot find symbol
import net.minecraft.client.renderer.block.model.BlockStateModel;
                                                ^
  symbol:   class BlockStateModel
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:23: error: cannot find symbol
import net.minecraft.client.renderer.block.model.SimpleModelWrapper;
                                                ^
  symbol:   class SimpleModelWrapper
  location: package net.minecraft.client.renderer.block.model
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error: cannot find symbol
    public static SimpleModelWrapper generateModel(final SimpleModelWrapper template, final BlockState planksBlockState) {
                                                         ^
  symbol:   class SimpleModelWrapper
  location: class SteeringWheelRenderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelRenderer.java:88: error: cannot find symbol
    public static SimpleModelWrapper generateModel(final SimpleModelWrapper template, final BlockState planksBlockState) {
                  ^
  symbol:   class SimpleModelWrapper
  location: class SteeringWheelRenderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:12: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/blocks/steering_wheel/SteeringWheelHandler.java:42: error: cannot find symbol
    public void renderOverlay(final GuiGraphics guiGraphics, final int width1, final int height1, final boolean hideGui) {
                                    ^
  symbol:   class GuiGraphics
  location: class SteeringWheelHandler
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:7: error: cannot find symbol
import net.minecraft.world.level.GameRules;
                                ^
  symbol:   class GameRules
  location: package net.minecraft.world.level
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/SimulatedWorldPreset.java:24: error: cannot find symbol
	public void modifyGameRules(final GameRules gameRules) {}
	                                  ^
  symbol:   class GameRules
  location: class SimulatedWorldPreset
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:5: error: cannot find symbol
import net.minecraft.world.level.GameRules;
                                ^
  symbol:   class GameRules
  location: package net.minecraft.world.level
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/worldgen/AirshipReadyPreset.java:14: error: cannot find symbol
	public void modifyGameRules(final GameRules gameRules) {
	                                  ^
  symbol:   class GameRules
  location: class AirshipReadyPreset
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:8: error: cannot find symbol
import net.minecraft.client.renderer.state.QuadParticleRenderState;
                                          ^
  symbol:   class QuadParticleRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/MagnetFieldParticle2.java:62: error: cannot find symbol
    public void extract(final QuadParticleRenderState state, final Camera renderInfo, final float partialTicks) {
                              ^
  symbol:   class QuadParticleRenderState
  location: class MagnetFieldParticle2
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:14: error: cannot find symbol
import net.minecraft.client.renderer.state.QuadParticleRenderState;
                                          ^
  symbol:   class QuadParticleRenderState
  location: package net.minecraft.client.renderer.state
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/content/particle/AugerIndicatorParticle.java:74: error: cannot find symbol
    public void extract(final QuadParticleRenderState state, final Camera renderInfo, final float partialTicks) {
                              ^
  symbol:   class QuadParticleRenderState
  location: class AugerIndicatorParticle
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimBlocks.java:18: error: package io.github.fabricators_of_create.porting_lib.models.generators does not exist
import io.github.fabricators_of_create.porting_lib.models.generators.ConfiguredModel;
                                                                    ^
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:10: error: cannot find symbol
import net.minecraft.client.gui.GuiGraphics;
                               ^
  symbol:   class GuiGraphics
  location: package net.minecraft.client.gui
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimIcons.java:65: error: cannot find symbol
    public void render(final GuiGraphics graphics, final int x, final int y) {
                             ^
  symbol:   class GuiGraphics
  location: class SimIcons
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:6: error: cannot find symbol
import com.mojang.blaze3d.platform.DepthTestFunction;
                                  ^
  symbol:   class DepthTestFunction
  location: package com.mojang.blaze3d.platform
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:12: error: cannot find symbol
import com.zurrtum.create.client.foundation.render.RenderTypes;
                                                  ^
  symbol:   class RenderTypes
  location: package com.zurrtum.create.client.foundation.render
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:14: error: cannot find symbol
import net.minecraft.client.renderer.RenderStateShard;
                                    ^
  symbol:   class RenderStateShard
  location: package net.minecraft.client.renderer
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:212: error: cannot find symbol
    private static RenderType.CompositeState compositeState(final Identifier texture,
                             ^
  symbol:   class CompositeState
  location: class RenderType
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:225: error: cannot find symbol
                                     final RenderType.CompositeState state) {
                                                     ^
  symbol:   class CompositeState
  location: class RenderType
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/index/SimRenderTypes.java:230: error: cannot find symbol
                                           final RenderType.CompositeState state) {
                                                           ^
  symbol:   class CompositeState
  location: class RenderType
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/dev/simulated_team/simulated/mixin/physics_staff/GuiGraphicsMixin.java:15: error: cannot find symbol
@Mixin(GuiGraphics.class)
       ^
  symbol: class GuiGraphics
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/loot/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/providers/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/builders/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/util/nullness/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/util/entry/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
/home/runner/work/create-aeronautics-fly/create-aeronautics-fly/simulated/src/main/java/com/tterrag/registrate/util/package-info.java:2: error: cannot find symbol
@net.minecraft.MethodsReturnNonnullByDefault
              ^
  symbol:   class MethodsReturnNonnullByDefault
  location: package net.minecraft
267 errors
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


BUILD FAILED in 1m 32s
2 actionable tasks: 2 executed
```
