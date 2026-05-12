## 描述
执行 another meta-skill like the [Skill 技能](/skills/技能/skill), but allows for placeholders inside the skill attribute.  
The attribute "sync=true" will be inherited by any sub-skills and cannot
设为 *false* later in a skill-tree.  


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skill     | s, $, (), m, 技能, meta | The metaskill to be executed. Accepts [Placeholders](/Skills/Placeholders)  |<!--type:Metaskill-->|
| forcesync | sync      | 是否 to force the skill to be run synchroniously with Minecraft   | false   |
| branch    | b, fork, f| 是否 the called metaskill's skilltree should [branch](/skills/技能/skill#branch-attribute) off from the skilltree of the calling 技能      | false   |
| executeafterdeath | continueafterdeath | 是否 the metaskill should be able to be called after 施法者的 death                                                                                 | false   |
| variable  | var       | The MetaSkill variable whose value is to be executed. When set, `skill` is ignored |


## 示例
```yaml
ExampleSkill:
  Skills:
  - vskill{s=ExampleSkill_<random.1to3>} @self

ExampleSkill_1:
  Skills:
  - effect:particles{particle=reddust;color=#FF0000;amount=10}
ExampleSkill_2:
  Skills:
  - effect:particles{particle=reddust;color=#FFFFFF;amount=10}
ExampleSkill_3:
  Skills:
  - effect:particles{particle=reddust;color=#00FF00;amount=10}
```
In the example, the `ExampleSkill` metaskill, once triggered, will 执行 a skill whose name is composed of `ExampleSkill_` and a randomly generated number between 1 and 3.

##

```yaml
Example_StanceSkill:
  Skills:
  - vskill{s=ExampleMob_<caster.stance>_<random.1to2>} @self
```
In this example, the VariableSkill is being used to quickly create some stance-based skills without the need to use any stance 条件 and the like

##

```yaml
Example_VariablePlaceholder:
  Skills:
  - vskill{s=Fireball_<skill.var.fireballtype>} @self
```
In this example, the VariableSkill 技能 will 执行 a metaskill whose name depends on some skill-scoped variables that has been set earlier on


## 别名
- [x] metavariableskill
- [x] vskill


<!--TAGS-->
<!--tag:Meta-Mechanic-->