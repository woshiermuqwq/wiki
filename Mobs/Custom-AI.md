[[_TOC_]]

# AI 目标 Selectors
AI 目标 Selectors are used 与 AIGoalSelectors field and determine what 生物 want to “do”. Certain 自定义 AI 目标 可能不 work if 它们是 not included in the base AI of the 生物 您是 creating. For 示例, a zombie 不会 be able to use the AI 目标 “EatGrass” 因为 a zombie would 永不 use that AI 目标 in the first place. Feel free to experiment to figure out what does and 不 work!

Note: Certain AI 目标 不会 work correctly if the 世界 is in peaceful 模式.

Example:

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

This zombie would 攻击 玩家, and walk around randomly when not targeting an enemy.

## All 生物
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| clear | reset | 移除 the AI 从 生物 |
| [breakdoors](/生物/ai/AI 目标/BreakDoor) | | Causes the 生物 to break down doors it runs into |
| [eatgrass](/生物/ai/AI 目标/EatGrass) | | Makes the 生物 偶尔… eat grass |
| [float](/生物/ai/AI 目标/Float) | swim | Makes the 生物 swim in water/not |
| [lookatplayers](/生物/ai/AI 目标/lookatplayers) | | The 生物 will look at nearby 玩家 |
| [LookAtTarget](/生物/ai/AI 目标/LookAtTarget) | | The 生物 will look at its 目标 |
| [opendoor](/生物/ai/AI 目标/OpenDoor)| opendoors | The 生物 will open doors it runs into and close the door behind it |
| [randomlookaround](/生物/ai/AI 目标/RandomLookAround) | lookaround | The 生物 will randomly look around |
| [gotospawnlocation](/生物/ai/AI 目标/gotospawn) | gotospawn | 生物 will pathfind to its 生成 位置 |
| [doNothing](/生物/ai/AI 目标/doNothing)<br>**[Premium-仅]** | | Causes the 生物 to 不要hing if 条件 are met. |

## Creatures Only
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [meleeattack](/生物/ai/AI 目标/meleeattack) | | Causes the 生物 to move to and melee-攻击 its 目标 |
| [movetowardstarget](/生物/ai/AI 目标/MoveTowardsTarget) | | Causes the 生物 to move towards its 目标 |
| [randomstroll](/生物/ai/AI 目标/RandomStroll) | | The 生物 will randomly walk around |
| [restrictsun](/生物/ai/AI 目标/RestrictSun) | | Will prevent the 生物 from entering sunlight |
| [fleeplayers](/生物/ai/AI 目标/fleeplayers) | runfromplayers | Causes the 生物 to avoid 玩家 |
| [fleegolems](/生物/ai/AI 目标/fleegolems) | runfromgolems | Causes the 生物 to avoid Iron Golems |
| [fleevillagers](/生物/ai/AI 目标/fleevillagers) | runfromvillagers | Causes the 生物 to avoid villagers |
| [fleewolf](/生物/ai/AI 目标/fleewolf) | runfromwolves | Causes the 生物 to avoid wolves |
| [fleefaction](/生物/ai/AI 目标/fleefaction) | runfromfaction | Causes the 生物 to avoid 实体 in a given 阵营 |
| [fleesun](/生物/ai/AI 目标/fleesun) | | The 生物 will hide in the shade when the sun it out |
| [fleeConditional](/生物/ai/AI 目标/fleeconditional)<br>**[Premium-仅]** | fleeIf | Causes the 生物 to flee 基于 provided 条件. Safe 速度 is 必需 for distances 大于 5 |
| [spiderattack](/生物/ai/AI 目标/SpiderAttack) | | Uses the 攻击 a spider would |
| [zombieattack](/生物/ai/AI 目标/ZombieAttack) | | Zombie melee 攻击 |
| [leapattarget](/生物/ai/AI 目标/leapattarget) | | Makes the 生物 leap at its 目标 |
| [move通过village](/生物/ai/AI 目标/move通过village) | | |
| [movetoblock](/生物/ai/AI 目标/movetoblock)| | Makes the 生物 go towards a specific 类型 of 方块 |
| [movetolava](/生物/ai/AI 目标/movetolava) | | Makes the 生物 move towards lava |
| [movetowater](/生物/ai/AI 目标/movetowater) | | Makes the 生物 move towards water |
| [movetowardsrestriction](/生物/ai/AI 目标/MoveTowardsRestriction) | | Make a 生物 move towards its "Restriction Point" for some 实体 (例如, the village of a Villager) |
| [MoveWithinDistanceOfTarget](/生物/ai/AI 目标/MoveWithinDistanceOfTarget) | | Moves 朝向 目标 to be 在...内 a certain 范围 |
|| [FollowRoute](/生物/ai/AI 目标/FollowRoute) | followpath | Makes the 生物 follow a specific path, one time 仅. |
| [patrol](/生物/ai/AI 目标/Patrol) x1,y1,z1;x2,y2,z2;x3,y3,z3;… | patrolroute | Makes the 生物 patrol 在...之间 specified 位置 |
| [gotolocation](/生物/ai/AI 目标/GoToLocation) x,y,z | goto | Makes the 生物 go to the specified 位置(Notice Followrange must 多于 the 距离 between 位置 and 生物) |
| [go也wner](/生物/ai/AI 目标/GoToOwner) # | | Makes the 生物 move towards its [主人](/技能/目标选择器/主人) when beyond a certain 距离 (默认为 5 方块)<br>[Followrange](/生物/选项#followrange) 必须为 多于 the 距离 在...之间 主人 and the 生物) |
| [gotoparent](/生物/ai/AI 目标/GoToParent) | | Makes the 生物 move towards its 父级 生物 |
| [Panic](/生物/ai/AI 目标/Panic) | panicWhenOnFire | Run around panicking when on 触发 and look for water |
| [randomFly](/生物/ai/AI 目标/RandomFly) | | Fly around randomly |
| [randomNod](/生物/ai/AI 目标/RandomNod) | | Makes the 生物 randomly nod its head |
| [horrified](/生物/ai/AI 目标/Horrified) | | Run around frantically |

## Animals Only
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [breed](/生物/ai/AI 目标/breed) | | Causes the 生物 to be able to breed with 其他 生物 |

## Creepers Only
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [creeperswell](/生物/ai/AI 目标/CreeperSwell) | creeperexplode | Make a creeper want to explode on its 目标 |

## Ranged 实体 Only
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [rangedattack](/生物/ai/AI 目标/arrowattack) | arrowattack | A basic ranged/弹射物 攻击 |
| [bowattack](/生物/ai/AI 目标/bowattack) | bowshoot, bowmaster | An advanced bow 攻击. |

## Piglins and Pillagers Only
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [crossbowAttack](/生物/ai/AI 目标/crossbowattack) | | 攻击 with a crossbow |


# AI 目标选择器
目标 Selectors are used 与 AITargetSelectors field and determine what 生物 try to 目标.

> If the 生物 has AITargets but not AIGoal that 允许 them to act 基于 their 目标, 它们将 *仍然* be considered to have valid targets chosen according to the AITargets used (so, 例如, a @目标 目标选择器可以usedand so on)。

示例
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

## All Creatures
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| clear | | Special 选项. Clears all of the 生物 AI |
| [hurtbytarget](/生物/ai/targets/HurtByTarget) | attacker, damager | Targets whatever 攻击 the 生物 |
| [monsters](/生物/ai/targets/Monsters) | monster | Targets monsters |
| [玩家](/生物/ai/targets/玩家) | 玩家 | Targets 玩家 |
| [Villagers](/生物/ai/targets/Villagers) | villager | Targets villagers |
| [irongolem](/生物/ai/targets/Irongolems) | irongolem, iron_golems, iron_golem | Targets Golems |
| [nearestConditionalTarget](/生物/ai/targets/nearestconditionaltarget)<br>**[Premium-仅]** | nearestConditional, nearestIf | Targets the nearest 实体 that meets the 条件 provided |
| [OwnerAttacker](/生物/ai/targets/OwnerAttacker) | ownerHurtBy, ownerHurtByTarget, ownerDamager | Targets whatever 攻击 the 生物 主人 |
| [OwnerTarget](/生物/ai/targets/OwnerTarget) | ownerAttack, ownerhurt | Targets whatever the 生物 主人 攻击. |
| [ParentHurtBy](/生物/ai/targets/ParentHurtBy) | parentHurtByTarget, parentDamager, parentAttacker | Targets the 实体 that 攻击 the 生物 父级 |
| [ParentTarget](/生物/ai/targets/ParentTarget) | parentHurt, parentAttack | Targets the 实体 即 being hit by the 施法者 父级 |

## All Creatures ([阵营](/生物/阵营) 支持)
| AI 目标 | 别名 | Description |
|--------------------|--------------|--------------------------------------------------------------------|
| [NearestOtherFaction](/生物/ai/targets/NearestOtherFaction) | OtherFaction | Targets ANY 实体 即 in a different 阵营 |
| [NearestOtherFactionMonsters](/生物/ai/targets/NearestOtherFactionMonsters) | OtherFactionMonsters | Targets any monster 即 in a different 阵营 |
| [SpecificFaction](/生物/ai/targets/specificfaction) [faction_name] | | Targets any 实体 即 in the given 阵营 |
| [SpecificFactionMonsters](/生物/ai/targets/specificfactionmonsters) [faction_name] | | Targets any monsters 即 in the given 阵营 |