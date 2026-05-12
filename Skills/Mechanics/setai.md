## 描述
Toggles the target AI


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| ai        | state, value | Sets the new mob AI. `true` enables it, `false` disables it       | false   |


## 示例
This example will turn off the ai of the mob for 5 seconds
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
