## 描述
Applies an 光环 to the 目标 that 触发 a skill when they break a block


## 属性

| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onBreakSkill | onBreak, oB | Skill to 执行 if the 目标 breaks a block                   |<!--type:Metaskill-->|
| cancelEvent | cancel, cE   | 是否 to cancel the event that triggered the 光环      | false   |
| dropitem  | 掉落, allowDrop | If the broken item should be dropped or not                    | true    |
| blocktypes | bt, t, material, materials, m, blocks, block, b| What blocks should 触发 this 光环<br>You can add a `*` at the front of the type to indicate that the one specified is not a block type, but a [block tag](https://minecraft.wiki/w/Tag#Block_tags_2) (example: `blocktype=*sculk_replaceable` )|         |

> This 技能 继承 [光环] 技能

## 示例

Simple:

Apply an onBlockBreak 光环 to yourself that makes 粒子 happen at the location of the broken block
```yaml
ApplyAura:
  Skills:
  - onBlockBreak{oB=FlameParticlesAtBlock;cE=false;auraname=Fire;d=300;i=1} @self
FlameParticlesAtBlock:
  Skills:
  - particles{particle=flame;a=2;hs=0.25;vs=0.25;y=0.5;s=0.1125} @targetlocation
```

##

Intermediate: (because you can crash / lag you server if you don't read this!)

Apply an onBlockBreak 光环 to yourself, then when you break blocks it'll mine in a 5x5 area (3 半径 in each direction from center block) based on the targetlocation of the block you broke. The 冷却 here is REQUIRED. Without the 冷却 the breakblock 技能 will retrigger the onblockbreak 光环 infinitely. You need MINIMUM 冷却 of 0.1 seconds (2 ticks). 

We need the 2 meta-skills here so that we can force the blockinradius to work at the block you broke. Without using 2 meta-skills, the blocksInRadius will 目标 the blocks around the player who broke the blocks instead of the location the blocks were broken.
```yaml
ApplyAura:
  Skills:
  - onBlockBreak{oB=AreaMining1;cE=false;auraname=TotalDestruction;d=300;i=1} @self
AreaMining1:
  Cooldown: 0.1
  Skills:
  - skill{s=AreaMining2} @targetLocation
AreaMining2:
  Skills:
  - breakblock{doDrops=true;doEffect=true;useTool=false;forcesync=true} @BlocksInRadius{r=3;ry=3}
```

##
```yaml
  Skills:
  - onBlockBreak{d=99999;bt=#TORCH,#LIGHT;oB=[ addVar{var=caster.lightsBroken;a=1} ]}
```


## 别名
- [x] onbreakblock


<!-- LINKS -->
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
