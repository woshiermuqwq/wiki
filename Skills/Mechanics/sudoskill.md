## 描述
The SudoSkill 机制 allows you to force the targeted entity to “cast”
a MythicMobs [Metaskill], even if the targeted entity is a player.  
No single 机制s 可以 used straight: they have to be in a [Metaskill]!  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| setcasterastrigger | cat |Sets the trigger of the called metaskill to the caster of this 机制|false|
| target    | t         | Sets the inherited targets of the called metaskill to the specified ones |     |

> 此机制继承所有[Skill](/skills/mechanics/skill) 机制

### SetCasterAsTrigger Attribute
If `setcasterastrigger` is `true`, the trigger of the skill 将会 set to
the caster of the sudoskill. Else the trigger is the caster of the
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
This metaskill will make every entity in a 20 block radius from the caster summon a particle effect. Because of the `target` attribute, the inherited target of the metaskill 将会 the player that is nearest to the caster in a 30 blocks radius
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
