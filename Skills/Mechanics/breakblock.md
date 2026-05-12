## 描述
Will break a block at the 目标 location. This 技能 will also 掉落
the block (with exception of Bedrock). REQUIRES `forcesync=true`.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| doDrops   | 掉落, d  | 是否 to 掉落 the block/s                                   | true    |
| doEffect  | effect, e | 是否 to play the break block 粒子                     | true    |
| useTool   | tool, t   | 是否 to use the tool in 玩家的 hands                  | true    |


## 示例
此示例将 break the block at location x:100,y:64,z:100 in the
current world when right-clicked.
```yaml
Skills:
  - breakblock{forcesync=true} @location{c=100,64,100} ~onInteract
```
##
### Tests
> These tests were run using /mm test 施放 TestingBreakBlock
 
```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=true} @origin
```

When a player calls this without a tool in there hand it does not 掉落 a block or create the 粒子 effects.
## 
```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=false} @origin
```

When a player calls this without a tool in there hand it does 掉落 the block, but does not create the 粒子 effects. The same is true if setting doEffect to false. 

##
```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=false;doDrops=true;useTool=true} @origin
```

When a player calls this with a tool in their hand it 掉落 the block and does not play the 粒子 effects. 

##
```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=false;useTool=true} @origin
```

When a player calls this with a tool in their hand it does not 掉落 a block, nor does it create the 粒子 effects.

##
```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=true} @origin
```

When a player calls this with a tool in their hand it does 掉落 a block, and does create the 粒子 effects.


## 别名
- [x] blockBreak


<!--TAGS-->
<!--tag:World-->