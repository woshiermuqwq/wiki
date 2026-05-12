## 描述
Sets the text component of 目标 Text Display entity


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| text      | t         | The text to use. If not set, the 技能 will remove the text from the entity instead                                                                                        |         |


## 示例
```yaml
ExampleTextDisplayEntity:
  Type: TEXT_DISPLAY
  DisplayOptions:
    Text: I am but a humble example, nothing to see here
  Skills:
  - settextdisplay{text="MUHAHAHA! YOU FELL FOR MY TRICKERY!";delay=100} @self ~onSpawn
```


## 别名
- [x] setText