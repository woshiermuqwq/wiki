## 描述
检测目标周围给定半径内是否有玩家。此条件在无玩家在范围内时通过。

## 属性

| 属性       | 别名   | 描述               | 默认值 |
| ---------- | ------ | ------------------ | ------ |
| distance   | d      | 检测半径            | 0      |


## 示例
```yaml
  Conditions:
  - playernotwithin{d=10} true
```

## 别名
- [x] playersnotwithin
