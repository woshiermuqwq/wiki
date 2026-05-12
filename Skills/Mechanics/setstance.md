## 描述
Sets the "stance" attribute of the target Mythic Mob to the given
string. Does nothing if the target is not a Mythic Mob.  

This 可以 used in conjunction with the [Stance condition](/skills/conditions/stance) to create different stances or phases
for a mob, where they use different abilities.  
The stance condition will match the current stance loosely, meaning if you set the stance to
"angry fiery explosive" the stance condition 将会 true 对于stance
"fiery".


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| stance    | s         | The string-name of the stance                                        | default |


## 示例
This skill would change the caster's phase to "bowphase"
```yaml
StanceChangeSkill:
  Skills:
  - setstance{stance=bowphase} @self
```


This skill would only be usable when the caster had the stance
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
