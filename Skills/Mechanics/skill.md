## 描述

Executes another [MetaSkill](/Skills/Metaskills), which 必须 located in
*/MythicMobs/Skills*. The executed skill will inherit any targets if no
targeter is specified.


## 属性

| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skill     | s, $, (), m, 机制s, meta, spell | The metaskill to be executed                      |<!--type:Metaskill-->|
| forcesync | sync      | Whether to force the skill to be run synchroniously with Minecraft   | false   |
| branch    | b, fork, f | Whether the called metaskill's skilltree should branch off from the skilltree of the calling 机制. The branch will originally clone the skilltree, but any changes made to the branch 将不会 reflect on the original skilltree                                              | false   |
| executeafterdeath | continueafterdeath | Whether the metaskill 应当 able to be called after the caster's death                                                                                 | false   |
| snapshotcasterstats | snapshotstats, scs | Whether the caster's stats 在moment of the skill execution 应当 "saved in memory", so that every subsequent check/fetch operation made against them returns the saved amount. This 可以 useful if the metaskill includes somewhat big delays and the caster's stats can change during the metaskill execution | false |
### Branch Attribute
Every time a skill is triggered from the mob file via a trigger, a `SkillTree` is generated. The `SkillTree` holds many informations, and among them there are the [Skill-Scoped Variables](/Skills/Variables#variable-scopes) and the [Skill Parameters](/Skills/Metaskills#skill-parameters-premium-feature) and their value.  

This makes their value accessible from any 机制 or metaskill that is being called from the same skilltree they are in, but it also makes them **unique**: there can exist only one `Skill Scoped Variable` or one `Skill Parameter` with the same name in the `SkillTree`, and setting more than one will override the value.

## 

```yaml
TestSkill_1:
  Skills:
  - setvariable{var=skill.sharedvalue;val=1}
  - skill{s=TestSkill_2}
  - skill{s=TestSkill_3}
  - message{m="<skill.var.sharedvalue>"} @World

TestSkill_2:
  Skills:
  - setvariable{var=skill.sharedvalue;val=2}

TestSkill_3:
  Skills:
  - setvariable{var=skill.sharedvalue;val=3}
```
> In this instance you can see how this all works out: the value of the skill scoped variable is set on all called metaskills, but since the skilltree is only one, the value is overridden multiple times, until, 在end, the value "3" is returned

## 

The `branch` Attribute, meanwhile, makes this no longer true: 如果设置 to true on a skill 机制, it makes the called metaskill have a brand new `SkillTree`, without it sharing any skill scoped variable or skill parameter

```yaml
TestSkill_1:
  Skills:
  - setvariable{var=skill.sharedvalue;val=1}
  - skill{s=TestSkill_2}
  - skill{s=TestSkill_3;branch=true}
  - message{m="<skill.var.sharedvalue>"} @World

TestSkill_2:
  Skills:
  - setvariable{var=skill.sharedvalue;val=2}

TestSkill_3:
  Skills:
  - setvariable{var=skill.sharedvalue;val=3}
```
> This example pans out like the previous one, except 对于line in which the TestSkill_3 MetaSkill is called: since the branch attribute is set to true, the variable is set on another skilltree, without the original one have "any knowledge" of it. So, the final value printed would be "2"

## 示例
```yaml
  Skills:
  - skill{skill=AnotherSkill} @Target ~onAttack
  - skill{s=AnotherSkill} @Trigger ~onSpawn
  - skill:OtherSkill @Trigger ~onDeath
```

The attribute "sync=true" 将会 inherited by any sub-skills and cannot
be set to *false* later in a skill-tree.

## 

```yaml
  Skills:
  - skill{s=AnotherSkill;sync=true} @Target ~onAttack
  - skill{s=ice_bolt;sync=true} @Target ~onTimer:100
  - skill{sync=true;s=flamethrower} @TargetLocation ~onTimer:200
  - skill:Onemechainc @Target ~onDamaged
  - skill{
      skill=leafs;
      sync=true
      }
```


## 别名
- [x] metaskill
- [x] meta


<!--TAGS-->
<!--tag:Meta-Mechanic-->
