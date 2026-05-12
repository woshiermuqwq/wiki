## 描述
检测目标距离世界出生点的距离是否在给定范围内。

## 属性

| 属性       | 别名   | 描述             | 默认值 |
| ---------- | ------ | ---------------- | ------ |
| distance   | d      | 要匹配的距离      |        |


## 示例
```yaml
  Conditions:
  - distancefromspawn{d=<100} true
```
```yaml
  Conditions:
  - distancefromspawn{d=>50} true
```
