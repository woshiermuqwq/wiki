## 描述
目标 all adjancent 方块 that 匹配 the blocktype, starting 从 原点 of the 技能


## 属性
| 属性 | 别名 | Description | 默认 |
|----------------|-----------------|--------------------------------------------------------|---------|
| blocktypes | blocktype, bt, t, material, materials, mat, m, 方块, 方块, b | 方块 to 添加 to the vein. Can be a 列表.<br>You can 添加 a `*` at the front of the 类型 to indicate that the one specified 不是 a 方块 类型, but a [方块 tag](https://Minecraft.wiki/w/Tag#Block_tags_2) (示例: `blocktype=*sculk_replaceable` )| STONE |
| limit | max, l, m | Limit of the number of 方块 added to the vein. | 10 |
| originMustMatch| 匹配 | Should the targeted 方块 匹配 the one at the 原点 of the 元技能 | true |


## 示例
```yaml
# Vein mine whatever you mine (Crucible)
VeinMinerPickaxe:
  Id: NETHERITE_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=<caster.raycast>} ~onBlockBreak

# Vein mine only certain ores (Crucible)
VeinMinerPickaxeOres:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=REDSTONE_ORE, DEEPSLATE_REDSTONE_ORE} ~onBlockBreak

# Vein mine all ores (Crucible)
VeinMinerPickaxeOres_V2:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=#_ORE} ~onBlockBreak
```


## 别名
- [x] vein
- [x] bv