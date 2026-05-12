## 描述
从技能原点开始，选取所有相邻的、类型匹配的方块


## 属性
| 属性      | 别名         | 描述                                            | 默认值 |
|----------------|-----------------|--------------------------------------------------------|---------|
| blocktypes     | blocktype, bt, t, material, materials, mat, m, blocks, block, b                        | 要纳入矿脉的方块类型。支持列表。<br>可在类型前加 `*` 表示指定的不是方块类型，而是[方块标签](https://minecraft.wiki/w/Tag#Block_tags_2)（例如：`blocktype=*sculk_replaceable`）| STONE   |
| limit          | max, l, m       | 矿脉中方块数量的上限       | 10      |
| originMustMatch| match           | 目标方块是否必须与嵌套技能原点处的方块匹配                                                                                   | true    |


## 示例
```yaml
# 连锁挖矿——挖掘你挖到的方块对应矿脉（Crucible）
VeinMinerPickaxe:
  Id: NETHERITE_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=<caster.raycast>} ~onBlockBreak

# 仅连锁挖掘特定矿石（Crucible）
VeinMinerPickaxeOres:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=REDSTONE_ORE, DEEPSLATE_REDSTONE_ORE} ~onBlockBreak

# 连锁挖掘所有矿石（Crucible）
VeinMinerPickaxeOres_V2:
  Id: DIAMOND_PICKAXE
  Skills:
  - breakblock{origin=@TargetBlock} @Vein{bt=#_ORE} ~onBlockBreak
```


## 别名
- [x] vein
- [x] bv
