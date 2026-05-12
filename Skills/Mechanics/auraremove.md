## 描述
移除目标的光环.  

You can decide if the aura executes its `onEnd` metaskill via the `DoEndSkillOnTerminate` attribute of the [Aura](/skills/mechanics/aura) 机制.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraName  | aura, b, buff, buffname, debuff, debuffname, n, name | The name of the aura      | default |
| stacks    | s                        | The amount of stacks                               | Max stacks |

### Aura Attribute
You can specify `ANY` as the value of the attribute in order to remove every aura on the target


## 示例
```yaml
  Skills:
  - auraremove{aura=Ice;stacks=10} @self ~onTimer:200
```


## 别名
- [x] removeaura
- [x] removebuff
- [x] removedebuff


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->
