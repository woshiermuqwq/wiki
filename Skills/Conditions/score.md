## 描述
检测目标实体的计分板数值。

## 属性

| 属性       | 别名      | 描述             | 默认值 |
| ---------- | --------- | ---------------- | ------ |
| objective  | obj, o    | 计分项名称        |        |
| entry      | ent, e    | 计分项条目        |        |
| value      | val, v    | 要匹配的值        |        |


## 示例
```yaml
  Conditions:
  - score{o=PlayerKills;e=Akim91;v=10} true
```
