## 描述
检测全局计分板的值（与虚拟玩家 `__GLOBAL__` 关联的值）。

## 属性

| 属性       | 别名      | 描述             | 默认值 |
| ---------- | --------- | ---------------- | ------ |
| objective  | obj, o    | 计分项名称        |        |
| value      | val, v    | 要匹配的值        |        |


## 示例
```yaml
  Conditions:
  - globalscore{o=KillCount;value=5} true
```

## 别名
- [x] scoreglobal
