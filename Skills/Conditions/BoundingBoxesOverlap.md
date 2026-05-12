## 描述
检查施法者的包围盒是否与目标的包围盒重叠。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| shiftforward | so, forwardoffset, fo, forward, f | 施法者包围盒的前向偏移量 |0.0 |


## 示例
```yaml
  TargetConditions:
  - boundingBoxesOverlap false
```


## 别名
- [x] bbsoverlap