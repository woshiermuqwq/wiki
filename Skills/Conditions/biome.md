## 描述
此条件测试目标是否在给定的生物群系列表中。  
如果未提供命名空间，默认使用 `minecraft:`

## 属性

| 属性 | 别名 | 描述               | 默认值          |
| --------- | --------| --------------------------|------------------|
| biome     | b       | 要检查的生物群系列表 | minecraft:plains |
| exact     | e       | 是否精确匹配生物群系 | true    |


## 示例

```yaml
Conditions:
- biome{b=minecraft:plains,river} true
```

如果使用自定义生物群系（例如来自数据包），可以用命名空间键来定义：

```yaml
Conditions:
- biome{b=far_end:void,far_end:warped_marsh} true
```