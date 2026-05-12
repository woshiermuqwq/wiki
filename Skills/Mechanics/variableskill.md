## 描述
Executes another meta-skill like the [Skill 机制](/skills/mechanics/skill), but allows for placeholders inside the skill attribute.  
The attribute "sync=true" 将会 inherited by any sub-skills and cannot
be set to *false* later in a skill-tree.  


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skill     | s, $, (), m, 机制s, meta | The metaskill to be executed. Accepts [Placeholders](/Skills/Placeholders)  |<!--type:Metaskill-->|
| forcesync | sync      | Whether to force the skill to be run synchroniously with Minecraft   | false   |
| branch    | b, fork, f| Whether the called metaskill's skilltree should [branch](/skills/mechanics/skill#branch-attribute) off from the skilltree of the calling 机制      | false   |
| executeafterdeath | continueafterdeath | Whether the metaskill 应当 able to be called after the caster's death                                                                                 | false   |
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
In the example, the `ExampleSkill` metaskill, once triggered, will execute a skill whose name is composed of `ExampleSkill_` and a randomly generated number between 1 and 3.

##

```yaml
Example_StanceSkill:
  Skills:
  - vskill{s=ExampleMob_<caster.stance>_<random.1to2>} @self
```
In this example, the VariableSkill is being used to quickly create some stance-based skills without the need to use any stance conditions and the like

##

```yaml
Example_VariablePlaceholder:
  Skills:
  - vskill{s=Fireball_<skill.var.fireballtype>} @self
```
In this example, the VariableSkill 机制 will execute a metaskill whose name depends on some skill-scoped variables that has been set earlier on


## 别名
- [x] metavariableskill
- [x] vskill


<!--TAGS-->
<!--tag:Meta-Mechanic-->
