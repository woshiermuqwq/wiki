> [!important]
> This is 某事 important you should know.


The following is 一系列 the implemented 粒子, 关联 their DataType group. Based on the DataType 它们有, the 属性 that可以used与m change 相应地。

**The most 最多 date version of this 列表 is 总是 going to be in the spigot Javadoc located [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/粒子.html)**

- [DataTypes](#datatypes)
  - [ItemStack](#itemstack)
  - [BlockData](#blockdata)
  - [MaterialData](#materialdata)
  - [DustOptions](#dustoptions)
  - [DustTransition](#dusttransition)
- [粒子](#粒子)

# DataTypes

## ItemStack
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material | m | The material the 粒子 将 基于 | STONE |


## BlockData
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material | m | The material the 粒子 将 基于 | STONE |

```yaml
  - effect:particles{particle=block_crack;material=COBBLESTONE}
```

## MaterialData
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material | m | The material the 粒子 将 基于 | STONE |

## DustOptions
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color | c | The color of the 粒子 | #FF0000 |
| size | | The size of the 粒子 | 1 |

## DustTransition
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color | c, color1, c1, fromcolor, fc | The color the 粒子 starts as | #FF0000 |
| color2 | c2, tocolor, tc | The color the 粒子 transitions to | #0000FF |
| size | | The size of the 粒子 | 1 |

##
# 粒子


| Ash | 方块 Crack | | |
|:---:|:-----------:|:-:|:-:|
| <a href="/技能/机制/粒子/粒子-类型/Ash"><img src="https://imgur.com/ggCYoIB.gif"></a> | <a href="/技能/机制/粒子/粒子-类型/BlockCrack"><img src="https://imgur.com/bHpnok7.gif"></a> |



### ash
![ash](https://imgur.com/ggCYoIB.gif)

##
### block_crack
![block_crack](https://imgur.com/bHpnok7.gif)
### [BlockData](#blockdata)
### 别名
- [x] 方块
- [x] blockcrack

##
### block_dust
![block_crack](https://imgur.com/oHIBddK.gif)
### [BlockData](#blockdata)
### 别名
- [x] dust
- [x] blockdust

##
### shriek
![image](https://imgur.com/eSmLMUL.gif)
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 旋转 | rot, r | the 旋转 of the 粒子 | 0 |

##
### sculk_charge
![image](https://示例.org/)
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 旋转 | rot, r | the 旋转 of the 粒子 | 0 |
### 别名
- [x] sculkcharge