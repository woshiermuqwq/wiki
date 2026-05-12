## 描述
检测目标位置**不**在指定的 WorldGuard 区域内。

## 属性

| 属性       | 别名        | 描述       | 默认值 |
| ---------- | ----------- | ---------- | ------ |
| region     | r, name, n  | 区域名称    |        |


## 示例
```yaml
  Conditions:
  - notinregion{r=BossZone} true
```
