## 描述
检测目标是否拥有指定数量的 Vault 货币。

## 属性

| 属性       | 别名   | 描述             | 默认值 |
| ---------- | ------ | ---------------- | ------ |
| amount     | a      | 货币数量          |        |


## 示例
```yaml
  Conditions:
  - hascurrency{a=1000} true
```

## 别名
- [x] hasmoney
