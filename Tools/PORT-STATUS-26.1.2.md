# 26.1.2 移植状态报告

分支 `port/26.1.2` ｜ 全部验证经 GitHub Actions（用户要求不在本地跑 Gradle）

## 错误数收敛曲线

| 轮次 | 提交 | 错误数 | 说明 |
|---|---|---|---|
| 1 | `5609caa` | 300 | 日志被 javac 100 条/task 上限截断 |
| 2 | `f987659` | 300 | 机械重命名第一批（97 文件） |
| 3 | `8bc1a21` | 225 | 放开诊断上限后拿到**完整**错误面 |
| 4 | `8ddabdf` | **84** | 剩余集中在 8 个文件 |

当前 84 个错误全部位于 `sable` 模块（`--continue` 下其余模块被跳过，等 sable 绿后才会暴露）。

## 本轮已完成（纯机械重命名，约 480 处）

- **ChunkPos 变为 record**：`.x`/`.z`→`.x()`/`.z()`、`toLong()`→`pack()`、
  `asLong(int,int)`→`pack(int,int)`、`new ChunkPos(BlockPos)`→`ChunkPos.containing(...)`、
  `ChunkPos.containing(long)`→`ChunkPos.unpack(long)`
- **包迁移**：`client.renderer.state.*`→`state.level.*`；`projectile.arrow`、
  `projectile.hurtingprojectile`(+`.windcharge`)、`animal.parrot`、`vehicle.minecart`；
  `BlockAndTintGetter`→`client.renderer.block`；`RenderType`→`client.renderer.rendertype`
- **`LightTexture` 拆分**：静态工具→`net.minecraft.util.LightCoordsUtil`，
  亮度→`Lightmap.getBrightness`
- **FRAPI 变 client-only**：`fabric.api.renderer.v1`→`fabric.api.client.renderer.v1`
- **`RenderType` 的 54 个静态工厂**→`RenderTypes.<name>()`
- 其它：`getLightBlock`→`getLightDampening`、`displayClientMessage(m,bool)`→
  `sendOverlayMessage`/`sendSystemMessage`、`EntityType.is(TagKey)`→
  `builtInRegistryHolder().is(...)`、`hasImpulse`→`needsSync`、
  `ResourceKey.location()`→`identifier()`、`SoundInstance.getLocation()`→`getIdentifier()`、
  `CHUNK_LOAD` 新增 `newChunk` 参数、`SavedDataType` 改用 `Identifier`

## 剩余 84 个错误（需真正改代码，非改名）

| 文件 | 数 | 需要做的事 |
|---|---|---|
| `sublevel/render/SubLevelLightVertexConsumerProvider` | 18 | FRAPI **删除** `BlockMultiBufferSource`，改用 `Renderer.quadEmitter(...)` + `AltModelBlockRenderer#tesselateBlock`；补 `VertexConsumer#setLineWidth(float)` |
| `mixin/sublevel_render/impl/vanilla/LevelRendererMixin` | 18 | `SectionBuffers` 删除→`SectionMesh#getSectionDraw(ChunkSectionLayer)`；`DynamicUniforms.Transform` record 去掉 float；`ChunkSectionsToRender` record 结构变更 |
| `mixin/sublevel_render/impl/sodium/SodiumWorldRendererMixin` | 15 | `BlockRenderDispatcher`/`Minecraft#getBlockRenderer()` 删除；`ChunkSectionLayerHelper.movingDelegate` 删除 |
| `mixin/debug_render/SubLevelBoundsRendererMixin` | 12 | `ShapeRenderer.renderLineBox(...)`→`renderShape(PoseStack,VertexConsumer,VoxelShape,DDDIF)` |
| `sublevel/plot/EmbeddedPlotLevelAccessor` | 9 | 实现 `LevelReader#environmentAttributes()`；`Level#getShade(Direction,boolean)` 删除 |
| `mixin/sublevel_render/block_entity_render/LevelRendererMixin` | 6 | `LevelRenderer.getLightColor`→`getLightCoords` |
| `network/packets/tcp/ServerboundGizmoMoveSubLevelPacket` | 3 | `Player` 无 `hasPermission(s)`，改走 `Player#permissions()` |
| `compatibility/scalablelux/ScalableLuxCompat` | 3 | 第三方 `StarLightInterface#removeChunkTasks(ChunkPos)` 消失 |

## 关键结论

这 8 个文件几乎全部落在 **26.1 渲染引擎重构**上（QuadEmitter/提交节点/SectionMesh/
新 block-model 路径）。它们无法用改名解决，需要按新管线重写这部分渲染代码。
`Sable` 是 vendored 的独立库，渲染侧改造量集中在这里。
