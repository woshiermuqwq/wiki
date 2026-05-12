## 描述
Sets the size of the 目标 `INTERACTION` [Type](/mythiccraft/Mythic生物/-/wikis/生物/生物#type) entity.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| height    | h         | The value to set the height to                                       | 1       |
| width     | w         | The value to set the width to                                        | 1       |


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