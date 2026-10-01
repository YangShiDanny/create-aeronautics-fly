# 移植到 Minecraft 26.1.2 — 状态与后续工作

分支：`port/26.1.2`
基线：`master`（1.21.10 / Fabric / Mojang 官方映射）
目标：26.1.2 / Java 25 / Fabric Loader 0.19.5 / Loom 1.18

> 本机无法编译（本地网络对 Maven 有 TLS 证书问题），所有验证走 GitHub Actions。
> 工作流：`.github/workflows/compile-26.1.2.yml`（推送到本分支即触发）。

---

## 一、已完成

### 1. 工具链与构建脚本

| 文件 | 改动 |
|---|---|
| `gradle.properties` | `java_version=25`、`minecraft_version=26.1.2`、`fabric_version=0.155.3+26.1.2`、`fabric_loader_version=0.19.5`、`loom_version=1.18-SNAPSHOT`、`create_fly_version=26.1.2-6.0.9-4`、`forgeconfigapiport_version=26.1.5`、新增 `puzzleslib_version=26.1.15`；删除 `veil_version` / `sable_companion_version` / `energy_version` |
| `build.gradle` | 插件 id → `net.fabricmc.fabric-loom`；4in1 打包的 `remapJar` → `jar` |
| `gradle/fabric-module.gradle` | 删除 `mappings` 整段；`modImplementation/modCompileOnly/modLocalRuntime` → `implementation/compileOnly/localRuntime`；删除 `loom { mixin { useLegacyMixinAp / defaultRefmapName } }`；删除 energy / veil / sable-companion / Porting-Lib 依赖；接入 `fuzs.puzzleslib:puzzleslib-fabric` |
| `sable/build.gradle` | 同上；删除 `sableCompanionRuntimeCompat` 配置与该段 jar 打包 |
| `simulated/build.gradle` | **删除 `unpackPortingLibCompat` 整个 ASM 字节码改写任务**（它依赖 Porting-Lib 与 Yarn 中间名 `class_2753`，在 26.1 完全不成立）；删除 refmap 校验 |
| `offroad/build.gradle`、`aeronautics/build.gradle` | `namedElements` 配置 → 普通 project 依赖；iris / entityculling 版本参数化 |
| `gradle/wrapper` | Gradle 9.4.1 → **9.7.1**（jar + properties 同步，保证 `wrapper-validation` 通过） |

### 2. 资源与元数据

- 10 个 `*.mixins.json`：删除 `refmap` 字段、`compatibilityLevel` → `JAVA_25`、补 `"overwrites": { "requireAnnotations": true }`
- 4 个 `*.accesswidener`：头部 `named` → `official`
- 5 个 `fabric.mod.json`：`minecraft` 加 `~` 前缀、删除 `team_reborn_energy` 依赖、新增 `puzzleslib` 依赖
- `sable/fabric.mod.json`：删除 `breaks.sablecompanion`（该依赖已移除，且属性占位符会令 `expand` 失败）

### 3. 代码机械改名（177 个文件 / 729 处）

脚本：`Tools/_rename.py`（可用 `--apply` 重跑；默认 dry-run）

- **Fabric API**：由官方迁移映射 `Tools/fabric-api-26-1-migration-map.xml` 驱动，139 条类改名（该 XML **只含 class 类型**），另手工补齐 38 条成员改名（`PayloadTypeRegistry.playC2S → serverboundPlay`、`ItemGroupEvents.modifyEntriesEvent → modifyOutputEvent`、`KeyBindingHelper.registerKeyBinding → registerKeyMapping`、`WorldRenderEvents → LevelRenderEvents`、`ColorProviderRegistry.BLOCK → BlockColorRegistry` 等）
- **原版 1.21.11 重命名**：
  - `net.minecraft.resources.ResourceLocation` → `net.minecraft.resources.Identifier`（全仓库已无残留）
  - `ResourceLocationException` → `IdentifierException`
  - `net.minecraft.advancements.critereon` → `net.minecraft.advancements.criterion`
  - `net.minecraft.BlockUtil` / `FileUtil` / `Util` → `net.minecraft.util.*`

已验证：模块源码中 `ResourceLocation`、`ItemGroupEvents`、`ParticleFactoryRegistry`、`FabricDataOutput`、`KeyBindingHelper`、`WorldRenderEvents`、`ExtendedScreenHandlerFactory`、`FabricTagProvider`、`BlockRenderLayerMap`、`InventoryStorage` 等旧名已全部清除。

---

## 二、依赖闸门（阻塞项）

| 依赖 | 26.1.2 可用性 | 处理 |
|---|---|---|
| `create-fly` | ✅ `26.1.2-6.0.9-4` | 已升级 |
| `forgeconfigapiport` | ✅ `26.1.5` | 已升级 |
| `puzzleslib` | ✅ `26.1.15`（`fuzs.puzzleslib:puzzleslib-fabric`，仓库 `raw.githubusercontent.com/Fuzss/modresources/main/maven/`） | 已接入 |
| JEI / Sodium / Iris / EntityCulling / CC:Tweaked / 双 Compass / ScalableLux | ✅ 均有 26.1.2 版 | 版本号已更新 |
| `foundry.veil` | ❌ 最高只到 `veil-fabric-1.21.1`（blamejared 仓库） | 已移除依赖；**大部分 API 已 vendored**（`simulated/.../foundry/veil/**` 10 个文件，覆盖 117 处引用中的 ~94 处），剩余 ~23 处是渲染侧（`VeilRenderSystem`、`AdvancedFbo`、`PostPipeline`、`ShaderProgram`、`VeilRenderLevelStageEvent` 等），需随渲染重构一并处理或继续 vendored |
| `sable-companion` | ❌ 只发布 1.21.1 | 已移除依赖与 jar 内置 |
| `team.reborn.energy` | ❌ 无 26.1 构建 | 已移除依赖；源码仅 2 处引用 `team.reborn.energy.api.EnergyStorage`（在 `simulated`），需 vendored 或删除该功能 |
| Porting-Lib | ❌ 无 26.1 构建 | 已移除依赖；**55 处引用**（`util.DeferredHolder` 18 处、`models.generators.*` 数据生成器、`data.ExistingFileHelper`、`conditions.*`、`tags.Tags`），需 vendored 或改写 |

---

## 三、待办（按优先级）

### P0 — CI 首轮会暴露的编译错误

1. **Porting-Lib 替代**（55 处）：`simulated/src/main/java/io/github/fabricators_of_create/porting_lib/...` 已在仓库内 vendored 了 `util/DeferredHolder.java`，但 datagen 的 `ModelFile` / `ConfiguredModel` / `MultiPartBlockStateBuilder` / `ExistingFileHelper` 等没有。
2. **Veil 渲染侧**（~23 处）：见上表。
3. **`ColorProviderRegistry`**：`simulated/src/main/java/com/tterrag/registrate/builders/BlockBuilder.java:264` —— 26.1 改为 `BlockColorRegistry.register(List<BlockTintSource>, Block...)`，**不是纯改名**，签名形态变了，需按新 API 重写。
4. **`net.minecraft.client.model` / `net.minecraft.world.entity` 子包重整**：影响 `simulated` 中 3 个类（`HumanoidModel`、`Model`、`geom.ModelPart`）与部分 `world.entity` 直接子包类，需按 26.1.2 实际包结构调整 import。
5. **原版语义变更**：`ItemStackTemplate`（世界加载前不能构造 `ItemStack`）、战利品类型展开（`LootPoolEntryType` 移除、注册表直接存 `MapCodec`）、`Validatable`/`ValidationContext`、村民交易数据包化、GameRules 注册表化。

### P1 — 渲染重构（**最难，官方文档缺失**）

26.1 是渲染引擎最大的一次改动。Fabric 官方博客只列了少数几项，渲染细节需参照 NeoForge primer 或直接读 26.1.2 反编译源码（`mcsrc.dev`）。

本项目的渲染重心在 `sable`：
- `SubLevelRenderer`、`VanillaChunkedSubLevelRenderData`、`SubLevelLightVertexConsumerProvider`、`SimpleCulledRenderRegion`
- 手写 OpenGL：`DSAStagingBuffer`、`SimpleSubLevelGroupRenderer` 等 11 个文件（26.1 是最后一个纯 OpenGL 版本，26.2 上 Vulkan；裸 GL 调用长期要迁到 Blaze3D）
- Sodium / Iris / EntityCulling / ScalableLux 兼容 mixin
- `fabric-module.gradle` 里已 `exclude` 的 13 个渲染 mixin 文件需全部重新评估

### P2 — 注册迁移到 Puzzles Lib（用户要求）

现状：注册体系基于 vendored 的 **Registrate**（`com.tterrag.registrate`，280 处引用）+ `com.zurrtum.create` shim（1851 处引用）。

迁移范围（注册入口）：
- `aeronautics/.../registry/AeroRegistrate.java`、`index/AeroItems.java`、`AeroBlocks.java`、`AeroEntityTypes.java`、`AeroBlockEntityTypes.java`、`AeroFluids`、`AeroParticleTypes` 等
- `offroad/.../index/OffroadItems.java`、`OffroadBlocks.java`、`OffroadEntityTypes.java`、`OffroadBlockEntityTypes.java` 等
- `simulated/.../registrate/**`（含 `SimulatedRegistrate`、`SimulatedCreativeTab`）
- `sable/.../platform/registry/SableRegistrationProvider.java`

建议路径：先接 Puzzles Lib 的 `RegistryManager` / `RegistryFactory` 到**新注册的**内容上，再逐步把 Registrate 的 builder 链式调用（`BlockBuilder` / `ItemBuilder` / `EntityBuilder` / `MenuBuilder` / 各 `RegistrateXxxProvider`）替换掉。Registrate 的 datagen provider 体系与 Puzzles Lib 的 `AbstractXxxProvider` 差异较大，需逐类对照。

---

## 四、怎么用

```bash
# 本地（若网络可用）
./gradlew :sable:compileJava :simulated:compileJava :offroad:compileJava :aeronautics:compileJava --continue

# 推送触发 CI
git push -u origin port/26.1.2
```

CI 的 `Compile 26.1.2` 工作流会：
1. 校验 Gradle wrapper
2. JDK 25 编译四个模块（`--continue`，尽量一次暴露全部错误）
3. 在 Summary 里按文件聚合 Top 60 错误源
4. 上传 `compile.log`

原 `CI`（gametests）工作流已收窄为只在 `master` 触发，避免在移植分支上白跑 45 分钟。

---

## 五、辅助脚本（`Tools/`）

| 脚本 | 用途 |
|---|---|
| `_rename.py` | 批量改名（Fabric API XML + 原版表）。默认 dry-run，`--apply` 落盘 |
| `_resources.py` | mixins.json / accesswidener 批量处理 |
| `_fmj.py` | fabric.mod.json 依赖处理 |
| `_phcheck.py` | 校验资源里的 `${placeholder}` 是否都有对应 Gradle 属性（防 `expand` 报错） |
| `_imports.py`、`_imports_detail.py` | 全量 import 统计，用于评估外部依赖改动面 |
| `_depcheck.py` | 查 Modrinth 上各依赖的 26.1.2 版本 |
| `_mavenprobe*.py` | 探测非 Modrinth 的 Maven 坐标 |
