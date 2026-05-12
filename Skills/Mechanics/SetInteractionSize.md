## 描述
Sets the size of the 目标 `INTERACTION` [Type](/mythiccraft/MythicMobs/-/wikis/生物/生物#type) entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| height    | h         | 要设置的值 the height to                                       | 1       |
| width     | w         | 要设置的值 the width to                                        | 1       |


## 示例
The following would set the size of the casting interaction entity to a 2x3 when right clicked
```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - setInteractionSize{height=2;width=3} @self ~onInteract
```


## 别名
- [x] interactionSize