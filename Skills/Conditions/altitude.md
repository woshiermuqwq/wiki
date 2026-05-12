## 描述
检测目标生物离地面的高度。

## 属性

| 属性      | 别名              | 描述                         | 默认值 |
| --------- | ----------------- | ---------------------------- | ------ |
| height    | altitude, a, h    | 要检测的高度范围              |        |
| maxHeight | mH                | 限制此条件能检测的最大高度     | 30     |


## 示例

```yaml
Conditions:
- altitude{h=3-5} true
```

## 别名
- [x] heightfromsurface
