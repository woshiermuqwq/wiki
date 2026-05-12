## 描述
测试目标是否在给定的生物群系类型列表中。



## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | t         | 要检查的生物群系类型列表                                            | ocean   |
| exact     | e         | 是否精确匹配类型                                    | true    |


## 示例
```yaml
Conditions:
- biometype{t=jungle,ocean,extreme_hills} true
```

## 生物群系类型
- none（无）
- taiga（针叶林）
- extreme_hills（山地）
- jungle（丛林）
- mesa（恶地）
- plains（平原）
- savanna（热带草原）
- icy（冰原）
- the_end（末地）
- beach（海滩）
- forest（森林）
- ocean（海洋）
- desert（沙漠）
- river（河流）
- swamp（沼泽）
- mushroom（蘑菇岛）
- nether（下界）
- underground（地下）
- mountain（山脉）

## 别名
- [x] biomecategory