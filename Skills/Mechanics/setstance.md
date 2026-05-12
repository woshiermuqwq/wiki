## 描述
Sets the "stance" attribute of the 目标 Mythic 生物 to the given
string. Does nothing if the 目标 is not a Mythic 生物.  

This 可用于 conjunction with the [Stance 条件](/skills/条件/stance) to create different stances or phases
for a 生物, where they use different abilities.  
The stance 条件 will match the current stance loosely, meaning if you set the stance to
"angry fiery explosive" the stance 条件 will be true for the stance
"fiery".


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stance    | s         | The string-name of the stance                                        | 默认值： |


## 示例
This skill would change 施法者的 phase to "bowphase"
```yaml
StanceChangeSkill:
  Skills:
  - setstance{stance=bowphase} @self
```


This skill would only be usable when the 施法者 had the stance
"bowphase"
```yaml
AnotherSkill:
  Conditions:
  - stance bowphase
  Skills:
  - ...some bow skills
```


## 别名
- [x] stance