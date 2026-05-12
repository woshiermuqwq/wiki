## 描述
执行命令 为每个提供的目标.

[Color codes](/Skills/Placeholders#color-codes) and [variables](/Skills/Variables) are allowed.  

The command specified 将不会 正常工作 if it contains double
quotes " or curly brackets {} and 必须 替换 with their
respective [message variables](/skills/Placeholders#special-characters).  
That happens because the double
quotes and curly brackets are reserved for MythicMobs itself trying to
read the syntax you supplied.


## 属性

| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| command   | c, cmd    | 要执行的命令                                               |         |
| asCaster  | ac, caster, sudo, asmob| 如果为 true，命令将从施法者而非控制台执行. | false   |
| asOp      | op        | 是否以所有权限执行命令                  | false   |
| asTarget  | at, target, sudotarget| 以目标实体身份执行命令          |  false  |
| requireTarget | rt    | 仅当技能有目标时才执行                      | asTarget's value|

  

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
> In this specific case, the `~` symbol is a problem: while normally, in vanilla, it would just mean "the position of the one that is executing the command", this is not possible with this specific setup, as it is the console that is executing the command, and as such there is no "position" that 可以 used. A way to fix this would have been to use the `<caster.l.x>`,`<caster.l.y>` and `<caster.l.z>` placeholders


### Making a player execute a command
This example will execute the "say" commands 对于player that interacted with the mob
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
