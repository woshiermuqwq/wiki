在[技能]维基页面中，我们可以看到可以通过以下语法让生物执行技能：

```yaml
- mechanic{argument=value} @[targeter] ~on[trigger] [health_modifier] [chance]
```

但如果你想把多条技能「组合」在一起，或者为生物打造更复杂的行为，这种写法就不够用了。这时就需要用到元技能。


目录：

[[_TOC_]]

# 什么是元技能？
本质上，元技能就是一组技能的列表，一旦通过[元技能]调用，就会按顺序执行其中的内容。  
**元技能存放在 `../plugins/MythicMobs/Skills` 目录下的 `.yml` 文件中**，和生物配置文件类似。

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
  FailedConditionsSkill: [若条件未通过，则执行此元技能]
  Cooldown: [秒数]
  OnCooldownSkill: [若此技能处于冷却中，则执行此元技能]
  Skill: [另一个元技能，与此技能异步执行]
  Skills:
  - mechanic1
  - mechanic2
```

配置好元技能后，就可以用[元技能]（比如 [Skill]）从生物或另一个元技能中调用它：
```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=internal_skillname} @self ~onInteract
```

请注意，只有 `internal_skillname` 这个元素是必填的。也就是说，你可以创建一个只含技能列表的元技能，也可以只加冷却时间，或者只加一些条件。

下面将逐一解释每个元素的作用和用法。
另外还有一些相关的[实例]可供参考，如果你想看更实际的应用的话。

# 元技能配置详解

## 内部技能名
这是用来在 MythicMobs 内部标识该元技能的字符串，和生物的[内部名称]概念完全一样。

一个有效的内部技能名必须是唯一的（即不能有两个技能共用同一个名字），并且不能包含空格。

无论以何种方式调用某个元技能，都需要使用它的内部技能名。


## CancelIfNoTargets
当没有符合条件的目标传递给元技能时，是否取消执行。  
默认为 `true`。


## Conditions
元技能的[条件]。这些条件以元技能的施法者为评估对象。

根据每个条件中使用的[条件操作]，可以产生不同的行为：请参阅相关维基页面了解更多。


## TargetConditions
目标[条件]。这些条件以元技能继承到的目标为评估对象，目标可以是实体也可以是位置。

根据每个条件中使用的[条件操作]，可以产生不同的行为：请参阅相关维基页面了解更多。


## TriggerConditions
触发者[条件]。这些条件以触发[技能树]的那个实体为评估对象。该实体也可以通过 [@Trigger] 目标选择器来选中。

根据每个条件中使用的[条件操作]，可以产生不同的行为：请参阅相关维基页面了解更多。


## FailedConditionsSkill
> 别名：`OnFailSkill`
当条件不满足时执行的元技能。
```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill: ExampleSkill2

ExampleSkill2:
  Skills:
  - message{m="So, well, it appears it's not daytime then."} @World
```
或者，也可以这样写：
```yaml
ExampleSkill:
  Conditions:
  - day true
  OnFailSkill:
  - message{m="Oh my, it still isn't daytime?"} @World
  - message{m="That's quite the problem!"} @World
```


## Cooldown
冷却时间，单位为秒。同一施法者两次执行该元技能之间必须间隔的时间。

例如：
```yaml
ExampleCooldownSkill:
  Cooldown: 10
  Skills:
  - ignite @self
```
`ExampleCooldownSkill` 这个元技能对于同一个施法者来说，每 10 秒最多只能触发一次。

冷却时间可以：
- 通过 [SkillOnCooldown] 条件来**检测**
- 通过 [<caster.skill.\[skill_name\].cooldown>] 占位符来**获取**
- 通过 [SetSkillCooldown] 技能来**设置**。


## OnCooldownSkill
如果元技能在冷却中被触发，则会转而执行这里指定的技能。

例如下面的例子：
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
正常施放 FirstSkill 时，聊天框会显示 "First"。在冷却期间再次执行它，聊天框会显示 "Second"；如果 FirstSkill 和 SecondSkill 都处于冷却中时再次执行，则会显示 "Third"。

你也可以直接定义一个技能列表，而不是引用另一个元技能：
```yaml
  OnCooldownSkills:
  - s{s=entity.village.no}
  - particle{p=VILLAGER_ANGRY;y=1.5}
```


## Skill
注意不要和 [Skills](#skills) 选项混淆。这个选项允许元技能在触发时同时执行另一个元技能中的技能列表。
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

这种执行方式有一些特定的行为：
- 另一个元技能中的技能列表会在当前元技能的 [Skills](#skills) 之前执行
- 另一个元技能的条件和冷却时间会被忽略（如果存在的话）
- 所有技能都在同一个[技能树]中执行

因此，上面的例子本质上等价于：

```yaml
example2:
  Skills:
  - skill{s=example1}
  - message{m="test2 - <skill.var.test>"} @self
  - message{m=4} @self
```

唯一的区别在于 example1 的冷却时间和条件被忽略了。


## Skills
元技能真正的核心。它是该元技能触发后将要执行的技能列表。这里也可以使用其他[元技能]，从而让元技能能够触发另外的元技能。

```yaml
ExampleSkill:
  Skills:
  - message{m="Hello there!"}
  - skill{s=ExampleSkill_2}

ExampleSkill_2:
  Skills:
  - message{m="How are you doing?"}
```

这里也可以使用延迟，让列表中排在延迟之后的每条技能都推迟执行。

```yaml
ExampleSkill:
  Skills:
  - message{m="Message 1"}
  - delay 20
  - message{m="Message 2"}
```

技能默认按列表从上到下的顺序依次执行。如果使用了某个[元技能]，它内部的技能会先执行完，然后再回到原始元技能继续执行后续技能。如果被调用的元技能内部有延迟，那么原始元技能会先继续执行后续技能，而被调用元技能中排在延迟之后的技能则在延迟结束后才执行。

![](https://i.imgur.com/ZiHWeBQ.png)
> 上图展示了上述行为的一个示例。如果执行 `ExampleSkill_First`，各条技能将按照它们的编号顺序执行，从 mechanic1 到 mechanic9，其中 mechanic7 与 mechanic8、mechanic9 之间间隔 20 刻的延迟。


# 目标继承与覆盖
元技能的一个特别之处在于，它能够「记住」调用它的[元技能]传入的目标。这一特性有很多用途。

## 继承
元技能内部没有自身目标选择器的技能会**继承**那些目标，并作用于它们。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#SKILL FILE
ExampleSkill:
  Skills:
  - ignite
```
在这个例子中，`ignite` 技能没有目标选择器，因此它会「继承」元技能调用时使用的目标选择器，并对那些实体生效——也就是点燃半径 10 格内的所有玩家。


## 覆盖
如果元技能内部*确实*指定了一个目标选择器，我们就说原始目标选择器被**覆盖**了，新的目标选择器会取而代之。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#SKILL FILE
ExampleSkill:
  Skills:
  - ignite
  - message{m="Why are you so close?"} @NearestPlayer{r=1}
```
在这个例子中，所有玩家仍然会被点燃，但只有距离该生物 1 格以内的最近玩家会收到消息。


## 后续元技能的执行
当你从一个元技能中调用另一个元技能时，也可以不为其指定目标选择器，此时它会继承调用它的那个元技能所继承的目标。

```yaml
#MOB FILE
ExampleMob:
  Type: ZOMBIE
  Skills:
  - skill{s=ExampleSkill} @PIR{r=10} ~onInteract
```
```yaml
#SKILL FILE
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
执行这个技能得到的结果，和[上一个例子](/Skills/Metaskills#override)完全一样。


## 目标过滤
目标继承的另一个绝佳用途是，利用元技能的 TargetConditions 在多个元技能之间层层过滤继承到的目标。

```yaml
#MOB FILE
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
上面的技能会先向 10 格范围内的所有玩家显示一条消息，然后向其中距离在 5 格以内的玩家显示另一条消息。最后，再向距离在 1 格以内的玩家显示第三条消息并将他们推开。

再来看一个不那么直观的例子：
```yaml
#MOB FILE
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
在这个例子中，生物会先向 10 格范围内的所有玩家发一条消息，然后 5 秒后，向其中那些在此期间已经移动到 10 格以外的玩家发送后续消息。


## 元目标选择器
另一个相关的话题是[元目标选择器]。简单来说，这类目标选择器会评估继承到的目标，并基于这些目标自行返回其他合适的目标。

```yaml
#MOB FILE
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
比如上面的例子会在施法者与 10 格范围内的每一位玩家之间生成一条粒子线。如果使用的目标选择器不是 `@PIR` 而是其他选择器，这条线就会在施法者和对应目标选择器选中的目标之间生成。


# 内联元技能
元技能也可以通过一种特殊的内联语法来编写，无需单独创建一个元技能文件。

用这种方式编写的元技能会失去普通元技能所拥有的全部字段（如 Conditions、OnCooldownSkill 等），想要实现类似效果需要用不同的方法（比如用 `cooldown` [通用属性]来代替 Cooldown 字段）。

内联元技能中的技能无法通过普通的注释方式禁用它，因为那样会导致整个元技能失效。必须在该技能前面使用 `<#>` 或 `<&nm>` 这类字符才能达到同样的效果。

内联元技能语法可以用在任何预期填写元技能内部名称的地方。

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
> 这个例子同时展示了内联元技能的语法以及普通元技能的某些特性（目标继承、延迟的使用）。
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
> 这个例子展示了内联元技能如何嵌套，以及它们如何共享同一个[技能树]，从而可以使用技能作用域内的变量。
##
```yaml
  Skills:
  - skill{branch=true;s=[
    - message{m="1"}
    <#>- message{m="2"}
    - message{m="3"}
    ];executeafterdeath=true} @trigger
```
> 这个例子展示了如何注释掉内联元技能中的某条技能，以及调用元技能时如何正常使用属性。


# 技能参数 [高级版功能]

技能参数是一项让你可以更方便地创建通用技能，并从其他技能向它们传递参数的功能。如果听起来有点绕，来看个例子！

目前大多数人在拥有很多相似的伤害技能时，会为不同的生物分别做一些微调（比如伤害值稍有不同），但除此之外它们的本质是一样的。

**旧的做法：**
```yaml
#SKILL FILE
ShadowDamage20:
  Skills:
  - damage{amount=20}
  - some shadowy effect

#MOB FILE
Mob1:
  Skills:
  - skill{s=ShadowDamage20} ~onAttack
```

**使用技能参数后，我们可以把这些合进一个技能里！新的做法：**
```yaml
#SKILL FILE
ShadowDamage:
  Skills:
  - damage{amount=<skill.damage>}

#MOB FILE
Mob1:
  Skills:
  - skill{s=ShadowDamage;damage=20} ~onAttack
```

在上面的例子中，技能仍然会对目标造成 20 点伤害，但我们把它做成了通用的，可以随意在不同生物上调整伤害值。  
「技能参数」系统会将 **skill/metaskill** 技能调用时的**所有**选项（除了该技能自身的特定选项外）沿着技能树向下传递，你可以在后面的环节中引用它们。如果后续技能传递了同名参数，它会被覆盖。这些参数可以在任何支持占位符的地方使用。

> 技能参数可通过 [skill](/Skills/Mechanics/skill) 和 [variableskill](/Skills/Mechanics/variableskill) 技能来使用。

## 保留参数名
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

<!-- GENERIC -->
[技能]: /Skills/Skills
[元技能]: /Skills/Mechanics#meta-mechanics
[实例]: /examples/Common-Examples#skills
[Skill]: /skills/mechanics/skill
[元目标选择器]: /Skills/Targeters#special-targeters
[技能树]: /Skills/SkillTrees

<!-- INTERNAL SKILLNAME -->
[内部名称]: /Mobs/Mobs#internal_name

<!-- COOLDOWN -->
[SkillOnCooldown]: /conditions/skilloncooldown
[<caster.skill.\[skill_name\].cooldown>]: /Skills/Placeholders#caster-placeholders
[SetSkillCooldown]: /skills/mechanics/setskillcooldown

<!-- CONDITIONS -->
[条件]: /Skills/conditions
[条件操作]: /Skills/conditions#condition-actions
[@Trigger]: /Skills/Triggers#the-trigger-targeter