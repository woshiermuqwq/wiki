如[技能]维基页面所示，可以通过以下语法从生物执行机制：

```yaml
- mechanic{argument=value} @[targeter] ~on[trigger] [health_modifier] [chance]
```

但如果想要"组合"多个机制，并总体上为生物创建更高级的行为，这种方式并不合适。这可以通过使用元技能来解决。

目录：

[[_TOC_]]

# 什么是元技能？
元技能本质上是一个机制列表，当通过[元机制]调用元技能时执行。
**它们位于 `../plugins/MythicMobs/Skills` 目录下的 `.yml` 文件中**，与生物配置类似。

元技能的语法如下：
```yaml
internal_skillname:
  CancelIfNoTargets: [true/false]
  Conditions:
  - condition1
  - condition2
  TargetConditions:
  - condition3
  - condition4
  TriggerConditions:
  - condition5
  - condition6
  FailedConditionsSkill: [如果条件检查失败要执行的元技能]
  Cooldown: [秒]
  OnCooldownSkill: [如果此技能处于冷却中要执行的元技能]
  Skill: [与此技能异步执行的附加元技能]
  Skills:
  - mechanic1
  - mechanic2
```

配置好元技能后，你可以使用[元机制]（如 [Skill]）从生物或元技能中执行它：
```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=internal_skillname} @self ~onInteract
```

请注意只有 `internal_skillname` 元素是必需的。例如，你可以创建一个只有技能列表的元技能，或只有冷却的元技能，或只有一些条件的元技能。

以下段落将解释每个元素的作用及如何使用。
还有一些相关的[示例]可供参考，如果你想看更实际的用法。

# 元技能配置详解

## Internal SkillName
这是在 MythicMobs 内部标识元技能的字符串，就像生物的 [Internal Name] 一样。

有效的 Internal SkillName 必须是唯一的（即不能有两个技能共享相同的 skillname），且不能包含空格字符。

如果你想以任何方式执行特定的元技能，都必须以某种方式使用其 Internal SkillName。

## CancelIfNoTargets
如果元技能没有获得有效的目标，是否取消其执行。
默认为 `true`。

## Conditions
元技能的[条件]。这些条件评估的是元技能的施法者。

根据每个条件中使用的[条件动作]，可以产生不同的行为：请阅读相关维基页面了解更多信息。

## TargetConditions
元技能的目标[条件]。这些条件评估的是元技能继承的目标，可以是实体或位置。

根据每个条件中使用的[条件动作]，可以产生不同的行为：请阅读相关维基页面了解更多信息。

## TriggerConditions
元技能的触发器[条件]。这些条件评估的是触发[技能树]的实体。此实体也可以通过 [@Trigger] 目标选择器来定位。

根据每个条件中使用的[条件动作]，可以产生不同的行为：请阅读相关维基页面了解更多信息。

## FailedConditionsSkill
> 别名：`OnFailSkill`
当条件检查失败时要执行的元技能。
```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill: ExampleSkill2

ExampleSkill2:
  Skills:
  - message{m="看来现在不是白天呢。"} @World
```
或者，也可以这样写：
```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill:
  - message{m="天啊，还不是白天吗？"} @World
  - message{m="这真是个问题！"} @World
```

## Cooldown
冷却时间是为同一施法者的元技能两次执行之间必须经过的时间（秒）。

例如：
```yaml
ExampleCooldownSkill:
  Cooldown: 10
  Skills:
  - ignite @self
```
`ExampleCooldownSkill` 元技能对于同一施法者每 10 秒只能触发一次。

冷却可以：
- 通过 [SkillOnCooldown] 条件**检查**
- 通过 [<caster.skill.\[skill_name\].cooldown>] 占位符**获取**
- 通过 [SetSkillCooldown] 机制**设置**。

## OnCooldownSkill
如果元技能在冷却中被触发，将改为执行此处指定的技能。

例如：
```yaml
FirstSkill:
  Cooldown: 10
  OnCooldownSkill: SecondSkill
  Skills:
  - command{c="say First"}

SecondSkill:
  Cooldown: 5
  OnCooldownSkill: ThirdSkill
  Skills:
  - command{c="say Second"}

ThirdSkill:
  Skills:
  - command{c="say Third"}
```
正常执行 FirstSkill 会在聊天中显示 "First"。在冷却中再次执行会显示 "Second"，而当 FirstSkill 和 SecondSkill 都在冷却中时再次执行则会显示 "Third"。

你也可以定义一个机制列表来替代另一个元技能：
```yaml
  OnCooldownSkills:
  - s{s=entity.village.no}
  - particle{p=VILLAGER_ANGRY;y=1.5}
```

## Skill
不要与 [Skills](#skills) 混淆。此选项允许元技能在触发时执行另一个元技能的机制。
```yaml
example1:
  Conditions:
  - night true
  Skills:
  - setvariable{var=skill.test;val=0} @self
  - message{m=1} @self
  - message{m=2} @self
  - delay 20
  - message{m=3} @self

example2:
  Skill: example1
  Skills:
  - message{m="test2 - <skill.var.test>"} @self
  - message{m=4} @self
```

此执行的行为非常特殊：
- 另一个元技能的机制在当前元技能的 [Skills](#skills) 之前执行
- 另一个元技能的条件和冷却（如果存在）被忽略
- 所有机制在同一个[技能树]中执行

因此，上述示例本质上等同于：

```yaml
example2:
  Skills:
  - skill{s=example1}
  - message{m="test2 - <skill.var.test>"} @self
  - message{m=4} @self
```

唯一的区别是 example1 的冷却和条件被忽略。

## Skills
元技能的真正核心。这是元技能触发时将执行的机制列表。其他[元机制]也可以在此使用，允许元技能触发其他元技能。

```yaml
ExampleSkill:
  Skills:
  - message{m="Hello there!"}
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  Skills:
  - message{m="How are you doing?"}
```

延迟也可以在此使用，允许用户在延迟机制之后的列表中的每个机制之间设置延迟。

```yaml
ExampleSkill:
  Skills:
  - message{m="Message 1"}
  - delay 20
  - message{m="Message 2"}
```

技能通常从列表中的第一个到最后一个依次执行。如果使用了[元机制]，其机制将在原始元技能的机制继续执行之前执行。如果被调用的元技能中包含延迟，则原始元技能的机制继续执行，而被调用元技能中的机制将在延迟之后执行。

![](https://i.imgur.com/ZiHWeBQ.png)
> 在这张图片中，展示了上述行为的示例。如果执行 `ExampleSkill_First`，机制将按照编号从 mechanic1 到 mechanic9 的顺序执行，mechanic7、mechanic8 和 mechanic9 之间有 20 tick 的延迟。

# 目标继承与覆盖
元技能的一个特性是能够"记住"调用它的[元机制]传递给它的目标。此行为有许多用途和应用。

## 继承
元技能中没有自己的目标选择器的机制将**继承**这些目标，并以它们为目标。

```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#技能文件
ExampleSkill:
  Skills:
  - ignite
```
在此示例中，`ignite` 机制没有目标选择器，因此它"继承"了元技能中使用的目标选择器，转而瞄准那些实体，使其点燃 10 格半径内的所有玩家。

## 覆盖
同时，如果元技能中*指定了*目标选择器，我们说原始目标选择器被**覆盖**，改用新的目标选择器。

```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#技能文件
ExampleSkill:
  Skills:
  - ignite
  - message{m="Why are you so close?"} @NearestPlayer{r=1}
```
在此示例中，所有玩家仍然会被点燃，但只有距离生物一格半径内最近的玩家会收到消息。

## 后续元技能执行
当你从一个元技能调用另一个元技能时，仍然可以不为它指定目标选择器，它将继承调用它的元技能所继承的目标。

```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#技能文件
ExampleSkill:
  Skills:
  - skill{s=Example_Ignite}
  - skill{s=Example_Message} @NearestPlayer{r=1}

Example_Ignite:
  Skills:
  - ignite

Example_Message:
  Skills:
  - message{m="Why are you so close?"}
```
执行此技能将获得与[上一个示例](/Skills/Metaskills#override)相同的结果。

## 目标过滤
目标继承的另一个重要应用是跨多个元技能过滤继承的目标，使用元技能的 TargetConditions。

```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill_1} @PIR{r=10} ~onInteract
```
```yaml
ExampleSkill_1:
  Skills:
  - message{m="Hello there!"}
  - delay 1
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  TargetConditions:
  - distance{d=<5} true
  Skills:
  - message{m="...You are pretty close, aren't you?"}
  - delay 1
  - skill{s=ExampleSkill_3}

ExampleSkill_3:
  TargetConditions:
  - distance{d=<1} true
  Skills:
  - message{m="AHHHHHH, GET AWAY FROM ME!"}
  - throw{v=10;vy=2}
```
以上技能将向 10 格半径内的所有玩家显示一条消息，然后向其中距离小于 5 格的玩家显示另一条消息。之后，向距离小于 1 格的每个玩家显示第三条消息并将其推开。

再看一个更反直觉的示例：
```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill_1} @PIR{r=10} ~onInteract
```
```yaml
ExampleSkill_1:
  Skills:
  - message{m="Hello there!"}
  - delay 100
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  TargetConditions:
  - distance{d=>10} true
  Skills:
  - message{m="...You truly don't like me, don't you?"}
  - delay 20
  - message{m="Don't worry, it's fine."}
  - delay 20
  - message{m="I'm used to it."}
  - delay 20
  - message{m="T.T"}
```
在此情况下，生物将首先向 10 格半径内的每个玩家发送消息，然后在 5 秒后，向其中在此期间移动到超过 10 格远的玩家发送额外消息。

## 元目标选择器
另一个相关主题是[元目标选择器]。简单来说，这些目标选择器会评估继承的目标是什么，并根据此返回其他合适的目标。

```yaml
#生物文件
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
ExampleSkill:
  Skills:
  - effect:particles @Line{r=0.2}
```
以上示例将在施法者和 10 格半径内的玩家之间生成一条粒子线。如果目标选择器不是 `@PIR` 而是其他，则粒子线将在施法者和使用的目标选择器之间生成。

# 内联元技能
元技能也可以使用特定的内联语法编写，无需完全创建另一个元技能。

以这种方式编写的元技能将失去对普通元技能所有字段（Conditions、OnCooldownSkill 等）的访问权限，需要使用不同的方法来获得类似结果（例如使用 `cooldown` [通用属性]而不是 Cooldown 字段）。

内联元技能中的机制不能用普通方式注释掉以禁用它们，因为这会导致整个元技能停止工作。必须使用 `<#>` 或 `<&nm>` 等字符在机制前以获得相同效果。

内联元技能语法可用在所有需要普通元技能内部名称的元机制中。

## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=[
    - message{m="Feeling cold? Don't you worry!"}
    - delay 40
    - ignite
    ]} @trigger ~onInteract
```
> 在此示例中，你可以看到内联元技能的写法以及普通元技能的一些特性（目标继承、延迟的使用）。
##
```yaml
  Skills:
  - skill{s=[
    - message{m="Hello there! A pleasure to meet you!"}
    - setvariable{var=skill.examplename;type=STRING;val=<target.name>}
    - skill{s=[
      - message{m="OHI, OHI! WHO IS THAT GUY OVER THERE NAMED <skill.var.examplename>?!?"}
      ]} @Owner
    ]} @target
```
> 在此示例中，你可以看到内联元技能可以嵌套，以及它们共享相同的[技能树]，允许它们使用技能作用域变量。
##
```yaml
  Skills:
  - skill{branch=true;s=[
    - message{m="1"}
    <#>- message{m="2"}
    - message{m="3"}
    ];executeafterdeath=true} @trigger
```
> 在此示例中，你可以看到如何在内联元技能中注释掉一个机制，以及如何在调用元机制时正常使用普通属性。

# 技能参数 [高级功能]

技能参数是一项功能，允许你更轻松地创建通用技能并从其他技能向它们传递参数。如果这听起来令人困惑，来看一个例子！

目前大多数人有许多相似的伤害技能，只是为不同的生物稍作调整以适应伤害的细微变化，但除此之外它们做的基本相同。

**旧的做法：**
```yaml
#技能文件
ShadowDamage20:
  Skills:
  - damage{amount=20}
  - some shadowy effect

#生物文件
Mob1:
  Skills:
  - skill{s=ShadowDamage20} ~onAttack
```

**使用技能参数，我们可以将它们全部合并为一个技能！新的做法：**
```yaml
#技能文件
ShadowDamage:
  Skills:
  - damage{amount=<skill.damage>}

#生物文件
Mob1:
  Skills:
  - skill{s=ShadowDamage;damage=20} ~onAttack
```

在上面的示例中，技能仍然会对目标造成 20 点伤害，我们只是使技能通用化，以便在任何生物上随意更改伤害。
"技能参数"系统会将 **skill/metaskill** 机制中的**任何**选项（除其专属选项外）沿着技能树传递，你可以在后面引用它们。如果后续技能传递了相同的参数，它会覆盖之前的值。这些参数可以在任何支持占位符的地方使用。

> 技能参数可以从 [skill](/Skills/Mechanics/skill) 和 [variableskill](/Skills/Mechanics/variableskill) 机制中使用。

## 保留参数名称
以下名称（不区分大小写）*不能*用作技能参数：
- `skill`
- `s`
- `meta`
- `m`
- `mechanics`
- `cooldown`
- `cd`
- `delay`
- `repeat`
- `targetinterval`
- `targeti`
- `repeatinterval`
- `repeati`
- `power`
- `powersplitbetweentargets`
- `powersplit`
- `splitpower`
- `forcesync`
- `sync`
- `targetisorigin`
- `sourceisorigin`
- `castfromorigin`
- `fromorigin`
- `fo`
- `origin`
- `branch`
- `fork`
- `snapshotcasterstats`
- `snapshotstats`
- `scs`
- `snapshottriggerstats`
- `sts`
- `targetcreative`

<!-- 通用 -->
[Skills]: /Skills/Skills
[Meta Mechanic]: /Skills/Mechanics#meta-mechanics
[Examples]: /examples/Common-Examples#skills
[Skill]: /skills/mechanics/skill
[Meta Targeter]: /Skills/Targeters#special-targeters
[Skilltree]: /Skills/SkillTrees

<!-- INTERNAL SKILLNAME -->
[Internal MobName]: /Mobs/Mobs#internal_name

<!-- 冷却 -->
[SkillOnCooldown]: /conditions/skilloncooldown
[<caster.skill.\[skill_name\].cooldown>]: /Skills/Placeholders#caster-placeholders
[SetSkillCooldown]: /skills/mechanics/setskillcooldown

<!-- 条件 -->
[Conditions]: /Skills/conditions
[Condition Action]: /Skills/conditions#condition-actions
[@Trigger]: /Skills/Triggers#the-trigger-targeter
