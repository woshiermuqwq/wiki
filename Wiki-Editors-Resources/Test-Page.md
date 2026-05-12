> [!important]
> 这是一条你需要了解的重要信息。

以下是已实现的粒子列表，按它们所属的 DataType 分组。根据粒子所属的 DataType，可以使用的属性也会相应变化。

**此列表的最新版本始终位于 Spigot Javadoc 中，[点击此处查看](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Particle.html)。**

- [DataType](#datatypes)
  - [ItemStack](#itemstack)
  - [BlockData](#blockdata)
  - [MaterialData](#materialdata)
  - [DustOptions](#dustoptions)
  - [DustTransition](#dusttransition)
- [粒子](#particles)

# DataType

## ItemStack
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m         | 粒子所基于的材质                           | STONE   |

## BlockData
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m         | 粒子所基于的材质                           | STONE   |

```yaml
  - effect:particles{particle=block_crack;material=COBBLESTONE}
```

## MaterialData
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| material  | m         | 粒子所基于的材质                           | STONE   |

## DustOptions
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color     | c         | 粒子的颜色                                            | #FF0000 |
| size      |           | 粒子的大小                                             | 1       |

## DustTransition
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| color     | c, color1, c1, fromcolor, fc | 粒子起始颜色                 | #FF0000 |
| color2    | c2, tocolor, tc | 粒子过渡到的颜色                         | #0000FF |
| size      |           | 粒子的大小                                             | 1       |

##
# 粒子


| Ash | Block Crack |   |   |
|:---:|:-----------:|:-:|:-:|
| <a href="/skills/mechanics/Particle/Particle-Types/Ash"><img src="https://imgur.com/ggCYoIB.gif"></a>       | <a href="/skills/mechanics/Particle/Particle-Types/BlockCrack"><img src="https://imgur.com/bHpnok7.gif"></a>                                                                                                      |



### ash
![ash](https://imgur.com/ggCYoIB.gif)

##
### block_crack
![block_crack](https://imgur.com/bHpnok7.gif)
### [BlockData](#blockdata)
### 别名
- [x] block
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
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| rotation  | rot, r    | 粒子的旋转角度                                         | 0       |

##
### sculk_charge
![image](https://example.org/)
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| rotation  | rot, r    | 粒子的旋转角度                                         | 0       |
### 别名
- [x] sculkcharge
