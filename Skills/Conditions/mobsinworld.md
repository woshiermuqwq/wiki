## 描述
匹配目标世界中的生物数量范围。

## 属性
| 属性       | 别名   | 描述               | 默认值 |
| ---------- | ------ | ------------------ | ------ |
| amount     | a      | 要匹配的数量范围     | 0      |


## 示例
```yaml
  Conditions:
  - mobsinworld{a=20to50} true
```

```yaml
  Conditions:
  - mobsinworld{a=<50} true
```
