[[_TOC_]]

# AI 目标选择器
目标选择器用在 `AIGoalSelectors` 字段中，决定生物"想要做什么"。某些自定义目标如果不在你所创建生物的基础 AI 中，可能不会生效。例如，僵尸无法使用 AI 目标 `EatGrass`，因为僵尸本来就不会有吃草的行为。建议多尝试以找出哪些可行、哪些不行！

注意：在世界处于和平模式时，某些目标可能无法正常工作。

示例：

```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
```

这个僵尸会攻击玩家，并在没有攻击目标时随机走动。

## 所有生物
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| clear                | reset        | 清除该生物的所有 AI                                                 |
| [breakdoors](/Mobs/ai/goals/BreakDoor) |              | 使生物撞破挡路的门                                                  |
| [eatgrass](/Mobs/ai/goals/EatGrass) |       | 使生物偶尔…吃草                                                     |
| [float](/Mobs/ai/goals/Float) | swim         | 使生物在水中游泳/不下沉                                              |
| [lookatplayers](/Mobs/ai/goals/lookatplayers) | | 生物会注视附近的玩家                                                  |
| [LookAtTarget](/Mobs/ai/goals/LookAtTarget) | | 生物会注视自己的目标                                                  |
| [opendoor](/Mobs/ai/goals/OpenDoor) | opendoors | 生物会打开挡路的门并随手关门                                          |
| [randomlookaround](/Mobs/ai/goals/RandomLookAround) | lookaround | 生物会随机环顾四周                                              |
| [gotospawnlocation](/Mobs/ai/goals/gotospawn) | gotospawn | 生物会寻路返回其生成位置                                              |
| [doNothing](/Mobs/ai/goals/doNothing)<br>**[仅高级版]** | | 使生物在满足条件时什么也不做                                                                                        |

## 仅生物实体
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [meleeattack](/Mobs/ai/goals/meleeattack) | | 使生物移动并近战攻击其目标                                    |
| [movetowardstarget](/Mobs/ai/goals/MoveTowardsTarget) | | 使生物朝目标移动                                  |
| [randomstroll](/Mobs/ai/goals/RandomStroll) |              | 生物会随机走动                                           |
| [restrictsun](/Mobs/ai/goals/RestrictSun) | | 阻止生物进入阳光下                                              |
| [fleeplayers](/Mobs/ai/goals/fleeplayers) | runfromplayers | 使生物躲避玩家                             |
| [fleegolems](/Mobs/ai/goals/fleegolems) | runfromgolems | 使生物躲避铁傀儡                              |
| [fleevillagers](/Mobs/ai/goals/fleevillagers) | runfromvillagers | 使生物躲避村民                         |
| [fleewolf](/Mobs/ai/goals/fleewolf) | runfromwolves | 使生物躲避狼                                       |
| [fleefaction](/Mobs/ai/goals/fleefaction) | runfromfaction | 使生物躲避指定阵营的实体                                                                                                  |
| [fleesun](/Mobs/ai/goals/fleesun) | | 太阳出来时生物会躲到阴凉处                                       |
| [fleeConditional](/Mobs/ai/goals/fleeconditional)<br>**[仅高级版]** | fleeIf | 使生物根据指定条件逃跑。距离超过 5 格时需要设置安全速度                              |
| [spiderattack](/Mobs/ai/goals/SpiderAttack) | | 使用蜘蛛的攻擊方式                                               |
| [zombieattack](/Mobs/ai/goals/ZombieAttack) | | 僵尸式近战攻击                                                    |
| [leapattarget](/Mobs/ai/goals/leapattarget) | | 使生物扑向目标                                                   |
| [movethroughvillage](/Mobs/ai/goals/movethroughvillage) |              |                                                                    |
| [movetoblock](/Mobs/ai/goals/movetoblock)| | 使生物走向指定类型的方块                                              |
| [movetolava](/Mobs/ai/goals/movetolava) | | 使生物走向熔岩                                                      |
| [movetowater](/Mobs/ai/goals/movetowater) | | 使生物走向水域                                                        |
| [movetowardsrestriction](/Mobs/ai/goals/MoveTowardsRestriction) | | 使生物朝其"限制点"移动，适用于某些实体（如村民的村庄）                   |
| [MoveWithinDistanceOfTarget](/Mobs/ai/goals/MoveWithinDistanceOfTarget) | | 朝目标移动以保持在指定范围内                              |
| [FollowRoute](/Mobs/ai/goals/FollowRoute) | followpath | 使生物沿特定路径移动，仅执行一次                                    |
| [patrol](/Mobs/ai/goals/Patrol) x1,y1,z1;x2,y2,z2;x3,y3,z3;… | patrolroute | 使生物在指定位置之间巡逻                                      |
| [gotolocation](/Mobs/ai/goals/GoToLocation) x,y,z | goto | 使生物前往指定位置（注意跟随距离必须大于位置与生物之间的距离）                                     |
| [gotoowner](/Mobs/ai/goals/GoToOwner) # |                | 使生物在超过一定距离（默认 5 格）后朝其[主人](/Skills/Targeters/Owner)移动<br>[跟随距离](/Mobs/Options#followrange) 必须大于主人与生物之间的距离)                                                    |
| [gotoparent](/Mobs/ai/goals/GoToParent) |       | 使生物朝其父生物移动                                                |
| [Panic](/Mobs/ai/goals/Panic) | panicWhenOnFire | 着火时惊慌逃跑并寻找水源                              |
| [randomFly](/Mobs/ai/goals/RandomFly) |               | 随机飞行                                                     |
| [randomNod](/Mobs/ai/goals/RandomNod) |         | 使生物随机点头                                                  |
| [horrified](/Mobs/ai/goals/Horrified) |         | 疯狂地跑来跑去                                                    |

## 仅动物
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [breed](/Mobs/ai/goals/breed) |   | 使生物能够与其他生物繁殖                                                   |

## 仅苦力怕
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [creeperswell](/Mobs/ai/goals/CreeperSwell) | creeperexplode | 使苦力怕在接近目标时爆炸                                          |

## 仅远程实体
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [rangedattack](/Mobs/ai/goals/arrowattack) | arrowattack         | 基础远程/弹射物攻击            |
| [bowattack](/Mobs/ai/goals/bowattack)      | bowshoot, bowmaster | 高级弓箭攻击                     |

## 仅猪灵和掠夺者
| AI 目标              | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [crossbowAttack](/Mobs/ai/goals/crossbowattack) | | 使用弩进行攻击                                                    |

# AI 攻击目标选择器
攻击目标选择器用在 `AITargetSelectors` 字段中，决定生物尝试攻击什么目标。

> 如果生物设置了 AITargets 但没有能够基于目标采取行动的 AIGoal，它们仍然会被视为根据所使用的 AITargets 选择了有效的目标（因此，例如可以使用 @target 目标选择器等）。

示例：
```yaml
SuperMob:
  Type: zombie
  Health: 200
  Display: 'Superb Zombie'
  AIGoalSelectors:
  - clear
  - meleeattack
  - randomstroll
  AITargetSelectors:
  - clear
  - players
  - golems
```

## 所有生物实体
| AI 攻击目标          | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| clear                |              | 特殊选项。清除该生物的所有 AI                                       |
| [hurtbytarget](/Mobs/ai/targets/HurtByTarget) | attacker, damager | 攻击任何攻击该生物的实体           |
| [monsters](/Mobs/ai/targets/Monsters) | monster | 攻击怪物                                                           |
| [Players](/Mobs/ai/targets/Players) | player | 攻击玩家                                                              |
| [Villagers](/Mobs/ai/targets/Villagers) | villager | 攻击村民                                                   |
| [irongolem](/Mobs/ai/targets/Irongolems) | irongolem, iron_golems, iron_golem | 攻击铁傀儡                       |
| [nearestConditionalTarget](/Mobs/ai/targets/nearestconditionaltarget)<br>**[仅高级版]** | nearestConditional, nearestIf | 攻击最近且满足指定条件的实体            |
| [OwnerAttacker](/Mobs/ai/targets/OwnerAttacker) | ownerHurtBy, ownerHurtByTarget, ownerDamager | 攻击任何攻击该生物主人的实体 |
| [OwnerTarget](/Mobs/ai/targets/OwnerTarget) | ownerAttack, ownerhurt | 攻击该生物主人正在攻击的实体                                 |
| [ParentHurtBy](/Mobs/ai/targets/ParentHurtBy) | parentHurtByTarget, parentDamager, parentAttacker | 攻击攻击该生物父实体的实体                 |
| [ParentTarget](/Mobs/ai/targets/ParentTarget) | parentHurt, parentAttack | 攻击施法者父实体正在攻击的实体                                   |

## 所有生物实体（支持[阵营](/Mobs/Factions)）
| AI 攻击目标          | 别名          | 说明                                                               |
|----------------------|--------------|--------------------------------------------------------------------|
| [NearestOtherFaction](/Mobs/ai/targets/NearestOtherFaction) | OtherFaction | 攻击任意不同阵营的实体                           |
| [NearestOtherFactionMonsters](/Mobs/ai/targets/NearestOtherFactionMonsters) | OtherFactionMonsters | 攻击任意不同阵营的怪物                |
| [SpecificFaction](/Mobs/ai/targets/specificfaction) [faction_name] | | 攻击指定阵营中的任意实体                                                                                        |
| [SpecificFactionMonsters](/Mobs/ai/targets/specificfactionmonsters) [faction_name] | | 攻击指定阵营中的任意怪物                                                                   |
