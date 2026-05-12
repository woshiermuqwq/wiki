## 描述
Toggles the sitting state for cats, dogs, foxes, and parrots.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| setSitting| state     | Sets the sitting state                                               | false   |


## 示例
让狼坐下 when right clicked.
```yaml
ExampleDog:
  Type: Wolf
  Skills:
  - sit{state=true} @Self ~onInteract
```

## 别名
: 
- [x] sit


<!--TAGS-->
<!--tag:AI-->
