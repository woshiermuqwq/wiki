## 描述
Removes an 光环 from the 目标.  

You can decide if the 光环 执行 its `onEnd` metaskill via the `DoEndSkillOnTerminate` attribute of the [光环](/skills/技能/光环) 技能.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| auraName  | 光环, b, buff, buffname, debuff, debuffname, n, name | The name of the 光环      | 默认值： |
| stacks    | s                        | The amount of stacks                               | Max stacks |

### 光环 Attribute
You can specify `ANY` as the value of the attribute in order to remove every 光环 on the 目标


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