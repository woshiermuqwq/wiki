## 描述
检测目标位置处的光照等级。

## 属性

| 属性       | 别名   | 描述               | 默认值 |
| ---------- | ------ | ------------------ | ------ |
| level      | l      | 要匹配的光照等级范围 | 0      |


## 示例
```yaml
  Conditions:
  - lightlevel{l=10} true
```

```yaml
  Conditions:
  - lightlevel{l=>10} true
```

```yaml
  Conditions:
  - lightlevel{l=1to10} true
```
