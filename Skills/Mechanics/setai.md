## 描述
切换目标的 AI 状态


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ai        | state, value | Sets the new 生物 AI. `true` enables it, `false` disables it       | false   |


## 示例
此示例将 turn off the ai of the 生物 for 5 seconds
```yaml
TemporaryAISwitcher:
  Skills:
  - setAI{ai=false} @self
  - delay 100
  - setAI{ai=true} @self
```


## 别名
- [x] ai


<!--TAGS-->
<!--tag:AI-->
