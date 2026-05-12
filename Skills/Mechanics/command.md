## 描述
执行 a command for each 目标 supplied.

[Color codes](/Skills/Placeholders#color-codes) and [variables](/Skills/Variables) are allowed.  

The command specified will not function correctly if it contains double
quotes " or curly brackets {} and must be substitued with their
respective [message variables](/skills/Placeholders#special-characters).  
That happens because the double
quotes and curly brackets are reserved for Mythic生物 itself trying to
read the syntax you supplied.


## 属性

| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| command   | c, cmd    | The command to 执行                                               |         |
| asCaster  | ac, 施法者, sudo, as生物| If true the command will 执行 from the 施法者 instead of the console. | false   |
| asOp      | op        | 是否 to 执行 the command with all permissions                  | false   |
| asTarget  | at, 目标, sudotarget| Will 执行 the command as 目标实体          |  false  |
| requireTarget | rt    | Only 执行 if the skill has a 目标                      | asTarget's value|

  

## 示例

### Correctly written command-skills
```yaml
  Skills:
  - command{c="give <target.name> gold_ingot 20"} @trigger ~onInteract
  - command{c="minecraft:tp <target.name> <mob.uuid>"} @self ~onDamaged
  - command{c="say HELLO <target.name>";asTarget=true;asOp=true} @NearestPlayer{r=10}
```

### Invalid command-skills

The below example(s) won't work because certain symbols haven't been
substituted with message variables.  
```yaml
  Skills:
  - command{c="minecraft:summon Zombie ~ ~ ~ {NoAI:true,CustomName:"Summoned Zombie"}"}
```
> In this specific case, the `~` symbol is a problem: while normally, in vanilla, it would just mean "the position of the one that is executing the command", this is not possible with this specific setup, as it is the console that is executing the command, and as such there is no "position" that can be used. A way to fix this would have been to use the `<施法者.l.x>`,`<施法者.l.y>` and `<施法者.l.z>` placeholders


### Making a player 执行 a command
此示例将 执行 the "say" commands for the player that interacted with the 生物
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - command{c="say <target.name>";asTarget=true;asOp=true} @trigger ~onInteract
```
## 别名
- [x] cmd


<!--TAGS-->
<!--tag:Meta-->
