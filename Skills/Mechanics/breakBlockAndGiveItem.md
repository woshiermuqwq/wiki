## 描述
Breaks the block at a 目标 location and gives item(s). This 技能 will also 掉落 the block (with exception of Bedrock). REQUIRES `forcesync=true`.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| dodrops   | 掉落, d  | 是否 to 掉落 the block/s | true          |
| doeffect  | effect, e | 是否 to play the break block 粒子 (?) | true |
| usetool   | tool, t   | 是否 to use the tool in 玩家的 hands (?) | true |
| doFakeLooting | fakeLooting, fl | Plays the pickup-item animation from the 原点 | false |
| items | item, i | An array of item materials, or droptables. | |


## 示例
Using Crucible Items:

Instead of dropping dirt, it'll instead give diamonds to the player.
```yaml
#Items Document
CustomItem:
  Id: GOLDEN_SHOVEL
  Display: 'Lucky Shovel'
  Skills:
  - skill{s=dirtToDiamonds;sync=true} @origin ~onBreakBlock

#Skills Document
dirtToDiamonds:
  TargetConditions:
  - blocktype{t=DIRT,GRASS_BLOCK} true
  Skills:
  - breakBlockAndGiveItem{dodrops=false;items=diamond}
```


## 别名
- [x] blockBreakAndGiveItem


<!--TAGS-->
<!--tag:World-->
<!--tag:Inventory-->
<!--tag:Item-->