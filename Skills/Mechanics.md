技能（也称基础技能）是 MythicMobs 内置的简单技能。你可以在生物的 Skill List 中直接调用这些基础技能，也可以通过组合多个技能来创建你自己的元技能。

部分技能可以以实体为目标，也可以以位置为目标，或者两者皆可。有些技能则不需要任何目标。你通过[目标选择器]来控制技能瞄准的目标。  

你也可以在[这里](/Skills/Tags/Mechanic-Tags)按标签查找技能。


[[_TOC_]]


# 扩展技能
以下是扩展插件提供的技能链接。如果没有安装对应的插件，这些技能不会生效。

- [ModelEngine 4](/../../../model-engine-4/-/wikis/Skills/Mechanics)
- [Mythic Crucible](/../../../mythiccrucible/-/wikis/Skills/Mechanics)
- [Mythic Enchantments](/../../../mythicenchants/-/wikis/Skills/Mechanics)
- [MCPets](https://mcpets.gitbook.io/mcpets/tutorials/mythicmobs-features#mechanics)


# 技能列表
以下技能通常以实体（玩家或其他生物）为目标，部分技能也可以以位置为目标。

| 技能                       | 描述                                                                                      |
|---------------------------|------------------------------------------------------------------------------------------|
| [ActivateSpawner]         | 在目标位置激活一个 MythicMobs 生成器                                                        |
| [AddTrade]                | 修改村民的交易内容                                                                          |
| [AnimateArmorStand]       | 为盔甲架播放动画                                                                            |
| [ArmAnimation]            | 让施法者挥动手臂                                                                            |
| [ArrowVolley]             | 发射一排箭矢                                                                                |
| [Attribute]               | 在目标实体上设置属性（若该实体支持属性）                                                       |
| [AttributeModifier]       | 为目标添加属性修饰符                                                                        |
| [AuraRemove]              | 从目标实体上移除一个[光环]                                                                    |
| [BarCreate]               | 为施法者生物创建一个自定义 Boss 血条                                                          |
| [BarRemove]               | 移除施法者生物的自定义 Boss 血条                                                              |
| [BarSet]                  | 修改施法者生物的自定义 Boss 血条                                                              |
| [BlackScreen]             | 在指定持续时间内使目标的屏幕变黑                                                               |
| [BlockDestabilize]        | 使目标方块像受重力影响一样掉落                                                                |
| [BlockMask]               | 临时将方块伪装成另一种方块                                                                   |
| [BlockUnmask]             | 还原被伪装的方块                                                                             |
| [BlockPhysics]            | 在目标位置触发一次方块物理更新                                                                |
| [BlockWave]               | 在目标位置创建一道「方块波浪」                                                                 |
| [BloodyScreen]            | 使目标的屏幕呈现红色光芒                                                                      |
| [BoneMeal]                | 对目标方块施加骨粉效果                                                                        |
| [BossBorder]              | 在生物周围创建一个无法逃脱的边界                                                               |
| [Bouncy]                  | 对目标施加一个使其具有弹跳效果的[光环]                                                           |
| [BreakBlock]              | 破坏目标位置的方块                                                                            |
| [BreakBlockAndGiveItem]   | 破坏目标位置的方块并给予物品/掉落表                                                             |
| [ClearExperience]         | 清除目标玩家的经验值                                                                          |
| [ClearExperienceLevels]   | 清除目标玩家的经验等级                                                                        |
| [ClearTarget]             | 强制技能目标重置当前锁定的目标                                                                 |
| [GiveExperienceLevels]    | 给予目标玩家经验等级                                                                          |
| [TakeExperienceLevels]    | 取走目标玩家的经验等级                                                                        |
| [CloseInventory]          | 关闭目标玩家的背包界面                                                                        |
| [Command]                 | 对每个目标执行一条命令                                                                        |
| [Consume]                 | 造成伤害的同时根据命中目标数量恢复生命值                                                        |
| [ConsumeSlot]             | 移除目标玩家指定槽位中的物品                                                                   |
| [DirectionalVelocity]     | 沿指定矢量方向改变目标实体的速度向量                                                            |
| [Disengage]               | 让施法者向后跳离目标实体                                                                      |
| [Disguise]                | 改变施法者的伪装外观                                                                          |
| [DisguiseModify]          | 修改施法者已应用的外观伪装                                                                     |
| [DisguiseTarget]          | 改变目标的伪装外观                                                                            |
| [Undisguise]              | 移除施法者的伪装                                                                              |
| [Dismount]                | 让施法者下马/下车                                                                             |
| [DisplayTransformation]   | 设置目标 Display 实体的变换属性                                                                |
| [ClearThreat]             | 清空生物的仇恨表                                                                              |
| [CurrencyGive]            | 给予玩家金钱。需要 Vault 和一个经济插件                                                        |
| [CurrencyTake]            | 取走玩家金钱。需要 Vault 和一个经济插件                                                        |
| [Damage]                  | 对目标造成指定数值的伤害                                                                       |
| [BaseDamage]              | 对目标造成基于生物伤害属性百分比的伤害                                                           |
| [PercentDamage]           | 对目标造成基于其当前生命值百分比的伤害                                                           |
| [Decapitate]              | 基于目标掉落一个玩家头颅物品                                                                    |
| [Doppleganger]            | 复制目标玩家的外观                                                                             |
| [DropItem]                | 在目标位置掉落物品或按掉落表掉落                                                                |
| [EjectPassenger]          | 将骑在施法者身上的实体弹开                                                                      |
| [Ender]                   | 产生「末影」视觉效果                                                                           |
| [EnderBeam]               | 向目标创建末影水晶光束效果                                                                     |
| [EnderDragonResetCrystals] | 生成末影龙的水晶                                                                               |
| [EnderDragonSetPhase]     | 设置末影龙的战斗阶段                                                                            |
| [EnderDragonSetRespawnPhase] | 设置末影龙的重生阶段                                                                        |
| [EnderDragonSpawnPortal]  | 生成末影龙战斗的传送门                                                                         |
| [Equip]                   | 让施法者生物装备一个物品                                                                        |
| [EquipCopy]               | 让施法者复制目标的装备                                                                         |
| [Explosion]               | 引发一次爆炸                                                                                  |
| [FakeExplosion]           | 引发一次假爆炸（纯视觉效果）                                                                     |
| [Extinguish]              | 熄灭目标实体身上的火焰                                                                         |
| [FawePaste]               | 使用 FAWE（Fast Async World Edit）粘贴一个 Schematic                                             |
| [Feed]                    | 喂饱目标玩家                                                                                  |
| [FillChest]               | 用物品或掉落表填充箱子                                                                         |
| [Firework]                | 在目标位置创建烟花效果                                                                         |
| [Flames]                  | 在目标选择器的位置创建火焰效果                                                                   |
| [Fly]                     | 对目标施加一个允许目标玩家飞行的[光环]                                                            |
| [ForcePull]               | 将目标传送到施法者身边                                                                         |
| [Freeze]                  | 使用细雪的冻结效果将目标冻结指定刻数                                                              |
| [Geyser]                  | 创建一道水或熔岩「喷泉」                                                                        |
| [GiveItem]                | 给予目标一个物品                                                                               |
| [GiveItemFromSlot]        | 将施法者指定槽位中的物品给予目标                                                                |
| [GiveItemFromTarget]      | 给予施法者物品并播放从目标实体或位置捡起的动画                                                     |
| [Glow]                    | 让目标发光                                                                                   |
| [GoatRam]                 | 让作为施法者的山羊实体冲撞目标实体                                                               |
| [GoTo]                    | 向目标选择器指定的位置（实体或坐标）移动                                                          |
| [GuardianBeam]            | 在原点与目标之间绘制一条守卫者光束                                                                |
| [Heal]                    | 治疗目标                                                                                     |
| [HealPercent]             | 按目标最大生命值的百分比进行治疗                                                                 |
| [Hide]                    | 在指定时间内对目标玩家隐藏施法者                                                                 |
| [Hit]                     | 模拟生物的一次物理攻击                                                                         |
| [Hologram]                | 在目标位置召唤一个全息投影                                                                      |
| [Ignite]                  | 点燃目标                                                                                     |
| [ItemSpray]               | 在目标位置产生一次临时物品的爆炸式散落效果                                                         |
| [JSONMessage]             | 向目标玩家发送 JSON 格式消息                                                                    |
| [Jump]                    | 让施法者跳跃                                                                                  |
| [Leap]                    | 让施法者向目标跳跃                                                                             |
| [Lightning]               | 在目标处召唤闪电                                                                               |
| [FakeLightning]           | 在目标处产生一个假闪电（纯视觉效果）                                                              |
| [Log]                     | 向控制台输出一条日志消息                                                                        |
| [Look]                    | 让施法者看向目标                                                                               |
| [Lunge]                   | 让施法者向目标方向冲刺                                                                          |
| [MatchRotation]           | 将施法者的朝向和俯仰角设置为与目标相同                                                            |
| [Message]                 | 向目标玩家发送一条消息                                                                          |
| [ModifyDamage]            | 修改触发该技能的伤害事件                                                                        |
| [ModifyGlobalScore]       | 修改虚拟玩家 \_\_GLOBAL\_\_ 的计分板值                                                           |
| [ModifyTargetScore]       | 修改目标的计分板值                                                                             |
| [ModifyMobScore]          | 修改施法者生物的计分板值                                                                        |
| [ModifyScore]             | 修改虚拟玩家的计分板值                                                                          |
| [Mount]                   | 为施法者召唤一个生物并骑上去                                                                     |
| [MountMe]                 | 强制目标实体骑上施法者                                                                          |
| [MountTarget]             | 让施法者骑上目标                                                                               |
| [MovePin]                 | 将指定标记点移动到目标位置                                                                      |
| [OpenTrades]              | 对目标玩家打开施法者村民的交易界面                                                               |
| [Oxygen]                  | 给目标玩家补充氧气（水下呼吸）                                                                   |
| [Particle]                | 在目标周围创建粒子效果                                                                          |
| [ParticleBox]             | 在目标周围绘制一个粒子盒子                                                                      |
| [ParticleEquation]        | 基于数学方程生成粒子                                                                            |
| [ParticleLine]            | 向目标绘制一条粒子线                                                                            |
| [ParticleLineHelix]       | 绘制一条线状螺旋效果                                                                            |
| [ParticleLineRing]        | 绘制由线段连接的粒子环                                                                          |
| [ParticleOrbital]         | 在目标周围绘制环绕粒子效果                                                                      |
| [ParticleRing]            | 在目标周围绘制一个粒子环                                                                        |
| [ParticleSphere]          | 在目标周围绘制一个粒子球体                                                                      |
| [ParticleTornado]         | 在目标处绘制一个持续的粒子「龙卷风」                                                              |
| [Atom]                    | 创建呈现原子形状的粒子                                                                          |
| [PickUpItem]              | 捡起目标物品                                                                                  |
| [PlayAnimation]           | 强制实体播放一段动画                                                                            |
| [PlayBlockBreakSound]     | 播放方块被破坏的声音                                                                            |
| [PlayBlockFallSound]      | 播放方块掉落的声音                                                                             |
| [PlayBlockHitSound]       | 播放方块被敲击的声音                                                                            |
| [PlayBlockPlaceSound]     | 播放方块被放置的声音                                                                            |
| [PlayBlockStepSound]      | 播放踩踏方块的声音                                                                              |
| [PoseArmorStand]          | 改变目标盔甲架的姿势                                                                            |
| [Potion]                  | 对目标施加药水效果                                                                              |
| [PotionClear]             | 移除目标实体的所有药水效果                                                                       |
| [Prison]                  | 将目标囚禁在方块内部                                                                            |
| [PrintParentTree]         | 输出关于执行该技能的元技能及其技能树的调试信息                                                       |
| [Propel]                  | 将施法者向目标推进                                                                              |
| [Pull]                    | 将目标拉向生物                                                                                 |
| [PushBlock]               | 将目标位置的方块沿指定方向推动                                                                   |
| [PushButton]              | 按下目标位置的按钮                                                                              |
| [RayTrace]                | 沿直线追踪到目标                                                                               |
| [RayTraceTo]              | 通过光线追踪到目标位置的方法来执行技能                                                             |
| [Rally]                   | 让附近的其他生物攻击目标                                                                        |
| [RandomMessage]           | 向目标玩家发送随机消息                                                                          |
| [Recoil]                  | 抖动目标屏幕以模拟后坐力                                                                        |
| [Remount]                 | 重新骑上施法者最初生成时骑乘的生物（如果该生物仍存活）                                               |
| [Remove]                  | 移除目标生物                                                                                   |
| [RemoveHeldItem]          | 移除目标玩家手持的部分物品                                                                      |
| [RemoveOwner]             | 移除目标生物的拥有者                                                                             |
| [ResetAI]                 | 尝试将施法者生物的 AI 重置为该基础类型的默认值                                                       |
| [RotateTowards]           | 将施法者转向目标位置方向                                                                        |
| [RunAIGoalSelector]       | 修改施法者的 [AIGoalSelectors]                                                                    |
| [RunAITargetSelector]     | 修改施法者的 [AITargetSelectors]                                                                  |
| [Saddle]                  | 为目标实体装备或移除鞍                                                                          |
| [SendActionMessage]       | 向目标玩家发送一条操作栏消息                                                                     |
| [SendResourcePack]        | 向目标玩家发送资源包                                                                            |
| [SendTitle]               | 向目标玩家发送标题/副标题消息                                                                     |
| [SendToast]               | 向目标玩家发送成就弹窗                                                                          |
| [SetAI]                   | 禁用/启用目标生物的 AI                                                                           |
| [SetBlockOpen]            | 设置目标方块的开启状态                                                                          |
| [SetBlockType]            | 改变目标位置的方块类型                                                                          |
| [SetChunkForceLoaded]     | 设置某位置区块的强制加载状态                                                                     |
| [SetCollidable]           | 设置目标是否应具有可碰撞的碰撞箱                                                                  |
| [SetDragonPodium]         | 在目标位置设置末影龙的基座位置                                                                   |
| [SetGameMode]             | 设置目标玩家的游戏模式                                                                          |
| [SetGliding]              | 如果目标有鞘翅，使其开始滑翔                                                                      |
| [SetGlobalScore]          | 设置虚拟玩家 \_\_GLOBAL\_\_ 的计分板值                                                            |
| [SetGravity]              | 设置目标实体是否受重力影响                                                                        |
| [SetHealth]               | 设置目标实体的生命值                                                                             |
| [SetInteractionSize]      | 设置目标 `INTERACTION` 实体的大小                                                                 |
| [SetItemGroupCooldown]    | 为目标玩家的物品组设置冷却时间                                                                   |
| [setDisplayEntityItem]    | 设置 `ITEM_DISPLAY` 实体的物品组件                                                                |
| [SetLeashHolder]          | 改变生物拴绳的把持者                                                                             |
| [SetLevel]                | 改变施法者生物的等级                                                                             |
| [SetMaterialCooldown]     | 为可使用物品（如末影珍珠、紫颂果等）设置冷却时间                                                     |
| [SetMaxHealth]            | 设置目标实体的最大生命值                                                                         |
| [SetMobColor]             | 改变目标的颜色（如果目标是可染色的生物）                                                            |
| [SetMobScore]             | 设置施法者生物的计分板值                                                                         |
| [SetName]                 | 改变施法者实体的名称                                                                             |
| [setRaiderCanJoinRaid]    | 设置目标掠夺者实体是否可以参与袭击                                                                 |
| [SetRaiderPatrolBlock]    | 设置目标掠夺者去巡逻某个位置                                                                      |
| [SetRaiderPatrolLeader]   | 设置掠夺者巡逻队长                                                                               |
| [SetFaction]              | 改变目标实体的阵营                                                                               |
| [SetFlying]               | 设置目标玩家是否在飞行                                                                           |
| [SetNoDamageTicks]        | 设置目标的无敌帧                                                                                |
| [SetOwner]                | 使目标成为施法者生物的拥有者                                                                      |
| [SetParent]               | 使目标成为施法者生物的父实体                                                                      |
| [SetPathfindingMalus]     | 设置生物对给定地形类型的寻路惩罚值                                                                 |
| [SetPitch]                | 设置目标实体的俯仰角                                                                             |
| [SetPose]                 | 设置实体的姿势                                                                                  |
| [SetRotation]             | 设置目标的旋转角度                                                                               |
| [SetTarget]               | 设置施法者的目标                                                                                |
| [SetTargetScore]          | 设置目标的计分板值                                                                               |
| [SetTextDisplay]          | 设置目标 Text Display 实体的文本组件                                                              |
| [SetTongueTarget]         | 将施法者青蛙的舌头瞄准目标实体                                                                    |
| [SetScore]                | 设置虚拟玩家的计分板值                                                                           |
| [SetSpeed]                | 设置目标实体的移动速度属性                                                                        |
| [SetStance]               | 设置目标生物的形态                                                                               |
| [Shield]                  | 为目标实体施加一个吸收护盾                                                                        |
| [ShieldBreak]             | 强制玩家放下盾牌并使其进入冷却                                                                     |
| [ShieldPercent]           | 按目标最大生命值的百分比为其施加吸收护盾                                                            |
| [ShootFireball]           | 向目标发射一个火球                                                                               |
| [ShootPotion]             | 向目标投掷一瓶药水                                                                               |
| [ShootSkull]              | 向目标发射一个凋零头颅                                                                            |
| [ShootShulkerBullet]      | 向目标实体发射一颗潜影贝导弹                                                                      |
| [ShowEntity]              | 向目标玩家显示隐藏的施法者                                                                        |
| [Signal]                  | 向生物发送一个信号                                                                               |
| [Skybox]                  | 改变目标玩家的天空盒                                                                             |
| [Smoke]                   | 创建一股烟雾                                                                                    |
| [SmokeSwirl]              | 创建一个持续的烟雾「漩涡」                                                                         |
| [Sound]                   | 播放音效（支持原版 Minecraft 和资源包）                                                             |
| [StealItem]               | 从目标身上偷取物品并放到生物手中                                                                   |
| [StopSound]               | 停止正在播放的音效                                                                               |
| [Speak]                   | 让生物在聊天中说话，可选择聊天气泡                                                                 |
| [Spin]                    | 让目标旋转                                                                                      |
| [Spring]                  | 在目标位置创建一个临时的液体弹簧                                                                  |
| [Stun]                    | 对目标实体施加一个使其眩晕的[光环]                                                                  |
| [StopUsingItem]           | 阻止目标实体使用物品                                                                             |
| [Suicide]                 | 让施法者死亡                                                                                    |
| [Summon]                  | 在目标位置召唤其他生物                                                                            |
| [SummonAreaEffectCloud]   | 在目标位置召唤粒子云                                                                             |
| [SummonFallingBlock]      | 召唤一个下落的方块                                                                               |
| [SummonPassenger]         | 召唤一个生物骑在目标身上                                                                          |
| [Swap]                    | 与目标交换位置                                                                                  |
| [SwingOffhand]            | 让作为施法者的玩家挥动副手                                                                        |
| [AddTag]                  | 为目标添加一个计分板标签                                                                          |
| [RemoveTag]               | 移除目标的计分板标签                                                                              |
| [TakeItem]                | 从目标玩家背包中移除物品                                                                          |
| [Taunt]                   | 调整施法者对目标实体的仇恨值                                                                      |
| [Teleport]                | 传送到目标位置                                                                                   |
| [TeleportY]               | 垂直传送施法者                                                                                   |
| [TeleportIn]              | 基于施法者的朝向，将目标传送到相对位置                                                              |
| [TeleportTo]              | 将目标传送到指定位置                                                                              |
| [Time]                    | 改变时间                                                                                        |
| [Threat]                  | 修改生物对目标的仇恨值                                                                            |
| [Throw]                   | 投掷目标实体                                                                                    |
| [ThunderLevel]             | 创建一个客户端级别的、按玩家独立的无雨雷暴效果                                                       |
| [ToggleLever]             | 切换目标位置的拉杆                                                                               |
| [TogglePiston]            | 切换目标位置的活塞                                                                               |
| [ToggleSitting]            | 切换猫、狗、狐狸和鹦鹉的坐下状态                                                                   |
| [TotemOfUndying]           | 播放玩家复活的效果                                                                               |
| [TrackLocation]           | 将生物的追踪位置设置为目标位置                                                                     |
| [UndoPaste]               | 撤销之前进行的粘贴操作                                                                            |
| [Velocity]                | 修改目标实体的速度向量                                                                             |
| [Weather]                 | 修改目标世界的天气                                                                               |
| [WolfSit]                 | 强制目标狼坐下                                                                                   |
| [WorldEditReplace]        | 使用 WorldEdit 替换区域内的方块                                                                     |


## 元技能

以下技能具有特殊的高级功能，大多用于调用其他技能。如果你指定了目标，由这些技能调用的所有其他技能都将「继承」这些目标（在适用的情况下）。

| 技能                      | 描述                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Skill]**             | 执行一个元技能，就像面包离不开黄油一样基础。                                                                                                    |
| **[VariableSkill]**     | 执行一个元技能，支持占位符。                                                                                                                     |
| [Aura]                  | 对目标实体施加光环，允许技能以 onStart/onTick/onEnd 等方式运行，所有技能都以目标为起效点。                                                         |
| [Beam]                  | 在施法者和目标之间创建一道材质光束                                                                                                                |
| [CancelEvent]           | 取消触发当前技能树的事件。仅对部分触发器有效。                                                                                                    |
| [CancelSkill]           | 被触发时取消当前元技能的执行。                                                                                                                     |
| [Cast]                  | 施加一个光环，以多种高级选项「施放」一个元技能。                                                                                                    |
| [Chain]                 | 在彼此靠近的多个目标之间链式传递技能。                                                                                                             |
| [ChainMissile]          | 在实体之间链式传递的制导弹射物。**仅限高级版！**                                                                                                    |
| [Delay]                 | 将当前技能列表的执行延迟指定刻数。                                                                                                                 |
| [DetermineCondition]    | 确定用作条件的元技能（通过 [MetaskillCondition](/Skills/Conditions/MetaskillCondition) 条件）的结果。                                              |
| [EndProjectile]         | 终止当前弹射物。只能在弹射物技能内使用。                                                                                                           |
| [ForEach]               | 对技能的每个目标执行一次元技能                                                                                                                     |
| [ForEachValue]          | 对指定值中的每个条目或键值对执行一次元技能                                                                                                          |
| [GlobalCooldown]        | 设置施法者的全局冷却计时器                                                                                                                         |
| [Missile]               | 向目标发射一个制导弹射物。                                                                                                                         |
| [ModifyProjectile]      | 修改弹射物/制导弹射物/环绕弹射物                                                                                                                    |
| [OnAttack]              | 对目标施加一个[光环]，在他们攻击时触发技能                                                                                                           |
| [OnDamaged]             | 对目标施加一个[光环]，在他们受到伤害时触发技能                                                                                                       |
| [OnShoot]               | 对目标施加一个[光环]，在他们射箭时触发技能                                                                                                           |
| [OnBlockBreak]          | 对目标施加一个[光环]，在他们破坏方块时触发技能                                                                                                       |
| [OnBlockPlace]          | 对目标施加一个[光环]，在他们放置方块时触发技能                                                                                                       |
| [OnChat]                | 对目标施加一个[光环]，在他们聊天时触发技能                                                                                                           |
| [OnSwing]               | 对目标施加一个[光环]，在他们挥动手臂/左键点击时触发技能                                                                                              |
| [OnInteract]            | 对目标施加一个[光环]，在他们交互/手持方块或看向轮廓方块时右键点击时触发技能（NOT AIR）                                                                 |
| [OnJump]                | 对目标施加一个[光环]，在他们跳跃时触发技能（仅 Paper 端有效）                                                                                       |
| [OnDeath]               | 对目标施加一个[光环]，在他们死亡时触发技能                                                                                                           |
| [Orbital]               | 对目标施加一个[光环]，使弹射物环绕目标运行                                                                                                           |
| [FollowPath]            | 对目标施加一个[光环]，让生物沿着路径移动                                                                                                             |
| [FormLine]              | 对目标施加一个[光环]，让生物沿着*直线*移动                                                                                                          |
| [Polygon]               | 创建高度可定制的多边形图案并可执行元技能                                                                                                            |
| [Projectile]            | 向目标发射一个高度可定制的弹射物                                                                                                                    |
| [ProjectileVelocity]    | 修改调用弹射物或制导弹射物的速度向量                                                                                                                |
| [RandomSkill]           | 从列表中随机执行一个技能                                                                                                                            |
| [SetSkillCooldown]      | 将指定元技能的冷却时间设置为给定值                                                                                                                  |
| [SetProjectileDirection]| 将调用弹射物的移动方向设置为目标方向                                                                                                               |
| [SetProjectileBulletModel] | 设置弹射物的模型（仅 DISPLAY 类型弹头有效）                                                                                                    |
| [Shoot]                 | 向目标发射一个物品弹射物，类似于箭/鸡蛋/雪球。                                                                                                      |
| [Slash]                 | 创建高度可定制的斩击图案并可执行元技能                                                                                                              |
| [SudoSkill]             | 让目标执行一个技能                                                                                                                                  |
| [Switch]                | 作为 switch/case 分支判断                                                                                                                           |
| [StatAura]              | 对目标施加一个光环，对其加成指定属性                                                                                                                |
| [Totem]                 | 在某个位置创建一个可执行其他技能的静态「图腾」                                                                                                        |
| [Terminable]            | 创建一个[光环]，当满足某些条件时取消其 onStart 元技能的执行                                                                                           |
| [Volley]                | 以多种选项向目标发射一排物品弹射物                                                                                                                  |
| [VariableAdd]           | 为数值变量增加一个值                                                                                                                                 |
| [VariableMath]          | 对数值变量执行数学运算                                                                                                                              |
| [SetVariable]           | 设置变量的值                                                                                                                                        |
| [SetVariableLocation]   | 将变量设置为目标位置                                                                                                                                |
| [VariableUnset]         | 删除变量                                                                                                                                            |
| [VariableSubtract]      | 从数值变量中减去一个值                                                                                                                              |
| [VariableMove]          | 将已创建的变量在不同名称和/或注册表之间移动                                                                                                           |
| [Wait]                  | 将元技能暂停，直到一组条件满足                                                                                                                       |


# 通用属性

以下属性适用于所有技能。

| 属性       | 别名          | 描述                                                                                   | 默认值   |
|-----------|--------------|---------------------------------------------------------------------------------------|--------|
| cooldown  | cd           | 冷却时间，单位为秒。支持小数。                                                             | 0      |
| delay     |              | 将技能的延迟执行推迟指定刻数。                                                              | 0      |
| repeat    |              | 重复执行的次数。如果 repeatInterval 设为 `0`，则此值变为执行次数而非重复次数                   | 0      |
| repeatInterval | repeatI | 每次重复之间需要间隔的刻数                                                              | 0      |
| targetInterval | targetI | 每次选择目标之间需要间隔的刻数                                                           | 0      |
| origin | | *[高级版]* 将原点改为所提供目标选择器的位置。如果解析出多个目标则不生效。`origin=@Forward{f=10}`<br>origin 属性的目标选择器会独立于技能的目标选择器进行解析，因此如果使用 `origin=@targetedlocation`，它不会返回技能显式的目标，而是返回元技能继承到的目标  |   |
| power     |              | [Power](/mobs/Power) 倍率                                                              | 1      |
| fromorigin | fo, sourceisorigin, castfromorigin | 是否从原点施放技能。仅对少数几个技能有效，通常也会在其自身属性中列出                | false  |
| targetisorigin |      | 是否将技能的目标设为原点                                                                  | false  |
| targetcreative |      | 是否将创造模式玩家也设为目标                                                               | false  |
| splitPower| powersplit, powersplitbetweentargets | 是否在各个目标之间分摊强度                                              | false  |
| faulty    |              | 是否使用旧版矢量公式                                                                    | true   |
| chance    |              | 技能执行的几率。例如 0.1 代表 10%                                                       | 1      |
| forcesync | sync         | 是否强制在主线程同步运行。这*通常*会降低性能（但通常不易察觉），但**部分技能需要将此设为 true** *(例如 [cancelevent] 技能，因为如果技能来得「太迟」，事件已经发生就无法取消了)* | false  |


# 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - message{m="This message will only be shown once every 5 seconds!";cooldown=5} @trigger ~onInteract
  - message{m="This one 5 times in a row over 2 seconds!";repeat=4;repeatInterval=10} @trigger ~onInteract
```



  [AIGoalSelectors]: /Mobs/Custom-AI#ai-goal-selectors
  [AITargetSelectors]: /Mobs/Custom-AI#ai-target-selectors
  [here!]: /skills/skillparametersystem
  [目标选择器]: /skills/targeters/

  [ActivateSpawner]: /skills/mechanics/activatespawner
  [AddTrade]: /skills/mechanics/AddTrade
  [AnimateArmorStand]: /skills/mechanics/animatearmorstand
  [ArmAnimation]: /skills/mechanics/ArmAnimation
  [ArrowVolley]: /skills/mechanics/arrowvolley
  [Attribute]: /skills/mechanics/Attribute
  [AttributeModifier]: /skills/mechanics/AttributeModifier
  [AuraRemove]: /skills/mechanics/auraremove
  [BarCreate]: /skills/mechanics/barcreate
  [BarSet]: /skills/mechanics/barset
  [BarRemove]: /skills/mechanics/barremove
  [BlackScreen]: /skills/mechanics/BlackScreen
  [BlockDestabilize]: /skills/mechanics/blockdestabilize
  [BlockMask]: /skills/mechanics/BlockMask
  [BlockUnmask]: /skills/mechanics/BlockUnmask
  [BlockPhysics]: /skills/mechanics/blockphysics
  [BlockWave]: /skills/mechanics/BlockWave
  [BloodyScreen]: /skills/mechanics/BloodyScreen
  [BoneMeal]: /skills/mechanics/bonemeal
  [BossBorder]: /skills/mechanics/bossborder
  [Bouncy]: /skills/mechanics/Bouncy
  [BreakBlock]: /skills/mechanics/breakblock
  [BreakBlockAndGiveItem]: /skills/mechanics/breakBlockAndGiveItem
  [ClearExperience]: /skills/mechanics/ClearExperience
  [ClearExperienceLevels]: /skills/mechanics/ClearExperienceLevels
  [ClearTarget]: /skills/mechanics/ClearTarget
  [GiveExperienceLevels]: /skills/mechanics/GiveExperienceLevels
  [TakeExperienceLevels]: /skills/mechanics/TakeExperienceLevels
  [CloseInventory]: /skills/mechanics/closeinventory
  [Command]: /skills/mechanics/command
  [Consume]: /skills/mechanics/consume
  [ConsumeSlot]: /skills/mechanics/consumeslot
  [DirectionalVelocity]: /skills/mechanics/DirectionalVelocity
  [Disengage]: /skills/mechanics/disengage
  [Disguise]: /skills/mechanics/disguise
  [DisguiseModify]: /skills/mechanics/DisguiseModify
  [DisguiseTarget]: /skills/mechanics/disguisetarget
  [Undisguise]: /skills/mechanics/undisguise
  [Dismount]: /skills/mechanics/dismount
  [DisplayTransformation]: /skills/mechanics/DisplayTransformation
  [ClearThreat]: /skills/mechanics/clearthreat
  [CurrencyGive]: /skills/mechanics/currencygive
  [CurrencyTake]: /skills/mechanics/currencytake
  [Damage]: /skills/mechanics/damage
  [BaseDamage]: /skills/mechanics/basedamage
  [PercentDamage]: /skills/mechanics/percentdamage
  [Decapitate]: /skills/mechanics/decapitate
  [Doppleganger]: /skills/mechanics/doppleganger
  [DropItem]: /skills/mechanics/dropitem
  [EjectPassenger]: /skills/mechanics/ejectpassenger
  [Ender]: /skills/mechanics/Ender
  [EnderBeam]: /skills/mechanics/EnderBeam
  [EnderDragonResetCrystals]: /Skills/Mechanics/EnderDragonResetCrystals
  [EnderDragonSetPhase]: /Skills/Mechanics/EnderDragonSetPhase
  [EnderDragonSetRespawnPhase]: /Skills/Mechanics/EnderDragonSetRespawnPhase
  [EnderDragonSpawnPortal]: /Skills/Mechanics/EnderDragonSpawnPortal
  [Equip]: /skills/mechanics/equip
  [EquipCopy]: /skills/mechanics/equipcopy
  [Explosion]: /skills/mechanics/explosion
  [FakeExplosion]: /skills/mechanics/FakeExplosion
  [Extinguish]: /skills/mechanics/extinguish
  [FawePaste]: /skills/mechanics/fawepaste
  [Feed]: /skills/mechanics/feed
  [FillChest]: /skills/mechanics/fillChest
  [Firework]: /skills/mechanics/firework
  [Flames]: /skills/mechanics/flames
  [Fly]: /skills/mechanics/fly
  [Freeze]: /skills/mechanics/freeze
  [ForcePull]: /skills/mechanics/forcepull
  [Geyser]: /skills/mechanics/geyser
  [Glow]: /skills/mechanics/glow
  [GiveItem]: /skills/mechanics/giveitem
  [GiveItemFromSlot]: /skills/mechanics/giveitemfromslot
  [GiveItemFromTarget]: /skills/mechanics/giveitemfromtarget
  [GoatRam]: /skills/mechanics/GoatRam
  [GoTo]: /skills/mechanics/goto
  [GuardianBeam]: /skills/mechanics/guardianbeam
  [Heal]: /skills/mechanics/heal
  [HealPercent]: /skills/mechanics/healpercent
  [Hide]: /skills/mechanics/hide
  [Hit]:  /skills/mechanics/hit 
  [Hologram]: /skills/mechanics/hologram
  [Ignite]: /skills/mechanics/ignite
  [ItemSpray]: /skills/mechanics/itemspray
  [JSONMessage]: /skills/mechanics/jsonmessage
  [Jump]: /skills/mechanics/jump
  [Leap]: /skills/mechanics/leap
  [Lightning]: /skills/mechanics/lightning
  [FakeLightning]: /skills/mechanics/FakeLightning
  [Log]: /skills/mechanics/Log
  [Look]: /skills/mechanics/look
  [Lunge]: /skills/mechanics/lunge
  [MatchRotation]: /skills/mechanics/MatchRotation
  [Message]: /skills/mechanics/message
  [ModifyDamage]: /skills/mechanics/ModifyDamage
  [ModifyGlobalScore]: /skills/mechanics/modifyglobalscore
  [ModifyTargetScore]: /skills/mechanics/modifytargetscore
  [ModifyMobScore]: /skills/mechanics/modifymobscore
  [ModifyScore]: /skills/mechanics/modifyscore
  [Mount]: /skills/mechanics/mount
  [MountMe]: /skills/mechanics/mountme
  [MountTarget]: /skills/mechanics/mounttarget
  [MovePin]: /skills/mechanics/MovePin
  [OpenTrades]: /skills/mechanics/OpenTrades
  [Oxygen]: /skills/mechanics/oxygen
  [Particle]: /skills/mechanics/Particle
  [ParticleBox]: /skills/mechanics/ParticleBox
  [ParticleEquation]: /skills/mechanics/ParticleEquation
  [ParticleLine]: /skills/mechanics/ParticleLine
  [ParticleLineHelix]: /skills/mechanics/ParticleLineHelix
  [ParticleLineRing]: /skills/mechanics/ParticleLineRing
  [ParticleOrbital]: /skills/mechanics/ParticleOrbital
  [ParticleRing]: /skills/mechanics/ParticleRing
  [ParticleSphere]: /skills/mechanics/ParticleSphere
  [ParticleTornado]: /skills/mechanics/ParticleTornado
  [Atom]: /skills/mechanics/Atom
  [PickUpItem]: /skills/mechanics/pickupitem
  [PlayAnimation]: /skills/mechanics/PlayAnimation
  [PlayBlockBreakSound]: /skills/mechanics/PlayBlockBreakSound
  [PlayBlockFallSound]: /skills/mechanics/PlayBlockFallSound
  [PlayBlockHitSound]: /skills/mechanics/PlayBlockHitSound
  [PlayBlockPlaceSound]: /skills/mechanics/PlayBlockPlaceSound
  [PlayBlockStepSound]: /skills/mechanics/PlayBlockStepSound
  [PoseArmorStand]: /skills/mechanics/posearmorstand
  [Potion]: /skills/mechanics/potion
  [PotionClear]: /skills/mechanics/potionclear
  [Prison]: /skills/mechanics/prison
  [PrintParentTree]: /skills/mechanics/PrintParentTree
  [Propel]: /skills/mechanics/propel
  [Pull]: /skills/mechanics/pull
  [PushBlock]: /skills/mechanics/PushBlock
  [PushButton]: /skills/mechanics/pushbutton
  [Rally]: /skills/mechanics/rally
  [RandomMessage]: /skills/mechanics/randommessage
  [Recoil]: /skills/mechanics/Recoil
  [Remount]: /skills/mechanics/remount
  [Remove]: /skills/mechanics/remove
  [RemoveHeldItem]: /skills/mechanics/removehelditem
  [RemoveOwner]: /skills/mechanics/removeowner
  [ResetAI]: /skills/mechanics/ResetAI
  [RotateTowards]: /skills/mechanics/RotateTowards
  [RunAIGoalSelector]: /skills/mechanics/runaigoalselector
  [RunAITargetSelector]: /skills/mechanics/runaitargetselector
  [Saddle]: /skills/mechanics/saddle
  [SendActionMessage]: /skills/mechanics/sendactionmessage
  [SendResourcePack]: /skills/mechanics/sendresourcepack
  [SendTitle]: /Skills/Mechanics/SendTitle
  [SendToast]: /skills/mechanics/sendtoast
  [SetAI]: /skills/mechanics/setai
  [SetBlockOpen]: /skills/mechanics/SetBlockOpen
  [SetBlockType]: /skills/mechanics/setblocktype

  [SetChunkForceLoaded]: /skills/mechanics/SetChunkForceLoaded
  [SetCollidable]: /skills/mechanics/setcollidable
  [SetDragonPodium]: /skills/mechanics/SetDragonPodium
  [SetFaction]: /skills/mechanics/setFaction
  [SetFlying]: /skills/mechanics/SetFlying
  [SetGameMode]: /skills/mechanics/setgamemode
  [SetGliding]: /skills/mechanics/setgliding
  [SetGlobalScore]: /skills/mechanics/setglobalscore
  [SetGravity]: /skills/mechanics/setgravity
  [SetHealth]: /skills/mechanics/sethealth
  [SetInteractionSize]: /skills/mechanics/SetInteractionSize
  [SetItemGroupCooldown]: /skills/mechanics/SetItemGroupCooldown
  [setDisplayEntityItem]: /skills/mechanics/setDisplayEntityItem
  [SetLeashHolder]: /skills/mechanics/setleashholder
  [SetLevel]: /skills/mechanics/setlevel
  [SetMaterialCooldown]: /skills/mechanics/setmaterialcooldown
  [SetMaxHealth]: /skills/mechanics/setmaxhealth
  [SetMobColor]: /skills/mechanics/setmobcolor
  [SetMobScore]: /skills/mechanics/setmobscore
  [SetName]: /skills/mechanics/setname
  [SetNoDamageTicks]: /skills/mechanics/setnodamageticks
  [SetOwner]: /skills/mechanics/setowner
  [SetParent]: /skills/mechanics/SetParent
  [SetPathfindingMalus]: /skills/mechanics/SetPathfindingMalus
  [SetPitch]: /skills/mechanics/SetPitch
  [SetPose]: /skills/mechanics/SetPose
  [setRaiderCanJoinRaid]: /Skills/Mechanics/setRaiderCanJoinRaid
  [SetRaiderPatrolBlock]: /skills/mechanics/setraiderpatrolblock
  [SetRaiderPatrolLeader]: /skills/mechanics/setraiderpatrolleader
  [SetRotation]: /skills/mechanics/setrotation
  [SetTarget]: /skills/mechanics/settarget
  [SetTargetScore]: /skills/mechanics/settargetscore
  [SetTextDisplay]: /skills/mechanics/SetTextDisplay
  [SetTongueTarget]: /skills/mechanics/settonguetarget
  [SetScore]: /skills/mechanics/setscore
  [SetSpeed]: /skills/mechanics/setspeed
  [SetStance]: /skills/mechanics/setstance
  [Shield]: /skills/mechanics/shield
  [ShieldBreak]: /skills/mechanics/shieldbreak
  [ShieldPercent]: /skills/mechanics/shieldpercent
  [ShootFireball]: /skills/mechanics/shootfireball
  [ShootPotion]: /skills/mechanics/shootpotion
  [ShootSkull]: /skills/mechanics/shootskull
  [ShootShulkerBullet]: /skills/mechanics/shootshulkerbullet
  [ShowEntity]: /skills/mechanics/showentity
  [Signal]: /skills/mechanics/signal
  [Skybox]: /skills/mechanics/Skybox
  [Smoke]: /skills/mechanics/Smoke
  [SmokeSwirl]: /skills/mechanics/SmokeSwirl
  [Sound]: /skills/mechanics/Sound
  [StealItem]: /skills/mechanics/StealItem
  [StopSound]: /skills/mechanics/StopSound
  [Speak]: /skills/mechanics/speak
  [Spin]: /skills/mechanics/Spin
  [Spring]: /skills/mechanics/spring
  [StopUsingItem]: /skills/mechanics/stopusingitem
  [Stun]: /skills/mechanics/stun
  [Suicide]: /skills/mechanics/suicide
  [Summon]: /skills/mechanics/summon
  [SummonAreaEffectCloud]: /skills/mechanics/summonareaeffectcloud
  [SummonFallingBlock]: /skills/mechanics/SummonFallingBlock
  [SummonPassenger]: /skills/mechanics/summonpassenger
  [Swap]: /skills/mechanics/swap
  [SwingOffhand]: /skills/mechanics/SwingOffhand
  [AddTag]: /skills/mechanics/addtag
  [RemoveTag]: /skills/mechanics/removetag
  [TakeItem]: /skills/mechanics/takeitem
  [Taunt]: /skills/mechanics/Taunt
  [Teleport]: /skills/mechanics/teleport
  [TeleportY]: /skills/mechanics/teleporty
  [TeleportIn]: /skills/mechanics/teleportin
  [TeleportTo]: /skills/mechanics/teleportto
  [Threat]: /skills/mechanics/threat
  [Throw]: /skills/mechanics/throw
  [ThunderLevel]: /skills/mechanics/ThunderLevel
  [Time]: /skills/mechanics/time
  [ToggleLever]: /skills/mechanics/togglelever
  [TogglePiston]: /skills/mechanics/TogglePiston
  [ToggleSitting]: /skills/mechanics/togglesitting
  [TotemOfUndying]: /skills/mechanics/TotemOfUndying
  [TrackLocation]: /skills/mechanics/tracklocation
  [UndoPaste]: /skills/mechanics/undopaste
  [Velocity]: /skills/mechanics/velocity
  [Weather]: /skills/mechanics/weather
  [WolfSit]: /skills/mechanics/wolfsit
  [WorldEditReplace]: /skills/mechanics/WorldEditReplace
  
  <!-- METAMECHANICS -->
  [Skill]: /skills/mechanics/skill
  [VariableSkill]: /skills/mechanics/variableskill
  [Aura]: /skills/mechanics/aura
  [光环]: /skills/mechanics/aura
  [Beam]: /skills/mechanics/Beam
  [CancelEvent]: /skills/mechanics/cancelevent
  [CancelSkill]: /skills/mechanics/CancelSkill
  [Cast]: /skills/mechanics/cast
  [Chain]: /skills/mechanics/chain
  [ChainMissile]: /skills/mechanics/chainmissile
  [Delay]: /skills/mechanics/delay
  [DetermineCondition]: /skills/mechanics/DetermineCondition
  [EndProjectile]: /skills/mechanics/endprojectile
  [ForEach]: /skills/mechanics/ForEach
  [ForEachValue]: /skills/mechanics/ForEachValue
  [GlobalCooldown]: /skills/mechanics/globalcooldown
  [Missile]: /skills/mechanics/missile
  [ModifyProjectile]: /skills/mechanics/modifyprojectile
  [OnAttack]: /skills/mechanics/onattack
  [OnDamaged]: /skills/mechanics/ondamaged
  [OnJump]: /skills/mechanics/onjump
  [OnShoot]: /skills/mechanics/onshoot
  [OnSwing]: /skills/mechanics/onswing
  [OnUse]: /skills/mechanics/onuse
  [Orbital]: /skills/mechanics/orbital
  [FollowPath]: /skills/mechanics/FollowPath
  [FormLine]: /skills/mechanics/FormLine
  [Polygon]: /skills/mechanics/polygon
  [Projectile]: /skills/mechanics/projectile
  [ProjectileVelocity]: /skills/mechanics/projectilevelocity
  [RayTrace]: /skills/mechanics/raytrace
  [RayTraceTo]: /skills/mechanics/raytraceto
  [Shoot]: /skills/mechanics/shoot
  [Slash]: /skills/mechanics/slash
  [Volley]: /skills/mechanics/volley
  [SudoSkill]: /skills/mechanics/sudoskill
  [RandomSkill]: /skills/mechanics/randomskill
  [SetSkillCooldown]: /skills/mechanics/setskillcooldown
  [SetProjectileDirection]: /skills/mechanics/SetProjectileDirection
  [SetProjectileBulletModel]: /skills/mechanics/setprojectilebulletmodel
  [StatAura]: /skills/mechanics/StatAura
  [Totem]: /skills/mechanics/totem
  [VariableAdd]: /skills/mechanics/variableadd
  [VariableMath]: /skills/mechanics/variablemath
  [SetVariable]: /skills/mechanics/setvariable
  [SetVariableLocation]: /skills/mechanics/setvariablelocation
  [VariableUnset]: /skills/mechanics/variableunset
  [VariableSubtract]: /skills/mechanics/variablesubtract
  [VariableMove]: /skills/mechanics/VariableMove
  [Terminable]: /skills/mechanics/terminable
  [OnBlockBreak]: /skills/mechanics/onblockbreak
  [OnBlockPlace]: /skills/mechanics/onblockplace
  [OnChat]: /skills/mechanics/OnChat
  [OnSwing]: /skills/mechanics/onswing
  [OnInteract]: /skills/mechanics/oninteract
  [OnJump]: /skills/mechanics/onjump
  [OnDeath]: /skills/mechanics/ondeath
  [Switch]: /skills/mechanics/Switch
  [Wait]: /skills/mechanics/Wait
  [cancelevent]: /skills/mechanics/cancelevent