## 描述
The SudoSkill 技能 allows you to force 目标实体 to “施放”
a Mythic生物 [Metaskill], even if 目标实体 is a player.  
No single 技能 can be used straight: they have to be in a [Metaskill]!  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| setcasterastrigger | cat |Sets the 触发 of the called metaskill to the 施法者 of this 技能|false|
| 目标    | t         | Sets the inherited 目标 of the called metaskill to the specified ones |     |

> This 技能 继承 [Skill](/skills/技能/skill) 技能

### SetCasterAsTrigger Attribute
If `setcasterastrigger` is `true`, the 触发 of the skill 将被设为 to
the 施法者 of the sudoskill. Else the 触发 is the 施法者 of the
skill.
```yaml
  Skills:
  - SudoSkill{s=SkillName;setcasterastrigger=true}
```


## 示例
```yaml
# Mob File
SudoMonkey:
  Type: villager
  Display: 'a Villager'
  Skills:
  - sudoskill{s=ExampleSudoskill;cat=true} @trigger ~onDamaged
```
```yaml
# Skills file
ExampleSudoskill:
  Skills:
  - arrowvolley{a=20;s=25;v=10;f=50;rd=200} @EIR{r=30}
  - message{msg="Triggername<&co> <trigger.name>"} @world
```
##
This metaskill will make every entity in a 20 block 半径 from the 施法者 summon a 粒子 effect. Because of the `目标` attribute, the inherited 目标 of the metaskill will be the player that is nearest to the 施法者 in a 30 blocks 半径
```yaml
ExampleTargetSkill:
  Skills:
  - sudoskill{
    target=@NearestPlayer{r=30};
    s=[
      - effect:particles
    ]} @EIR{r=20}
```


## 别名
- [x] sudo

[Metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Meta-Mechanic-->
