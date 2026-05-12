## 描述
Sets the sitting state of the target wolf.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| state     | sit, value | The state the wolf is in. True = sitting and False = standing       | true    |


## 示例
```yaml
# Standing
- wolfSit{state=false} @self ~onInteract
```

```yaml
# Sitting
- wolfSit{state=true} @self ~onInteract
```


<!--TAGS-->
<!--tag:AI-->
