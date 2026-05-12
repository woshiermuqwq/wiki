## 描述
Causes the current skilltree to be delayed by X ticks.  
Delay can also be used as an attribute directly inside of 技能s by adding the `delay=TICKS` [universal attribute](/Skills/Mechanics#universal-attributes). This way, the delay is not applied to the entire skilltree but only to the single 技能.  

Skill-delay and Attribute-delay do not work in the same manner.

> This 技能 can also be used to accomplish [Intratick Scheduling](/Skills/Intratick-Scheduling)

## 示例
```yaml
Skills:
  - ignite{ticks=60}
  - delay 60
  - explode
```

This is an example of using the delay universal attribute. It will work inside any 技能 and will delay it from happening by the specified amount of ticks.
```yaml
Skills:
  - skill{skill=exampleskill;delay=200}
  - explode{delay=80}
```


<!--TAGS-->
<!--tag:Meta:Flow-->
