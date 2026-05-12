## 描述
以位置 of a [Pin]为目标。
IfIf the Pin is a Multi-Pin made via a Pin Wand, this targets all of the associated 位置.


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 名称 | n, pin, p, key, k | The 名称 of the [pin] to 目标 |<!--类型:Pin--> |
| random | r |Whether to select a single and random 位置, if the specified pin is a Multi-Pin| false |


## 示例
```yaml
  Skills:
  - teleport @Pin{p=mypin}
```


<!-- LINKS -->
[pin]: /Pins