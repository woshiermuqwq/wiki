## 描述
检测提供的字符串是否为空。

## 属性
| 属性       | 别名                  | 描述             | 默认值 |
| ---------- | --------------------- | ---------------- | ------ |
| value      | val, v, string, s     | 要检测的字符串    |        |


## 示例
```yaml
  Conditions:
  - stringEmpty{value=<caster.var.examplevariable>}
```
> 检测 `<caster.var.examplevariable>` 占位符的值是否为空字符串。

## 别名
- [x] isEmpty
