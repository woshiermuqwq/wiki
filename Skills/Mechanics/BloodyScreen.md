## 描述
Shows the near world border effect.  
Players must enable Fancy Graphics to see the effect.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d         | The time (in ticks) that the effect is active                        | 20      |
| cancel    | c         | If true, it 停止 any existing redscreen                             | false   |


## 示例
```yaml
BloodyEffect:
  Skills:
  - effect:bloodyScreen{d=25} @PIR{r=15} ~onTimer:20
```


## 别名
- [x] effect:bloodyScreen
- [x] e:bloodyScreen
- [x] redScreen
- [x] effect:redScreen
- [x] e:redScreen


<!--TAGS-->
<!--tag:Effect-->