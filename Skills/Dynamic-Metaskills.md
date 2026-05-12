<!--
To the 其他 wiki editors: 不要 touch my 子级.
- Lxlp
-->

Normally, to 执行 a 技能 or a 元技能, 您需要 to have that 技能 or 元技能 written physically down in the 配置.
But with Dynamic 元技能 this you are now able to:
- 执行 single 技能 or entire 元技能 即使 they 永不 existed 之前 by dynamically constructing them.
- bypass missing 占位符支持in 技能/内联 条件。
- store entire 元技能 into 变量 or NBTs, enabling you to dynamically call them later

[[_TOC_]]

# DISCLAIMER
ThThis 不是 an intended 技能. It 仅 a side-效果 that consistently works 因为 of how the `vskill` 技能 operates

Since 这是 pretty much uncharted territory, if you have any information useful to further expand this page and, by proxy, the knowledge available to every 其他 MythicMobs user, let me know: [Lxlp Discord Profile](https://discord.com/users/353257382811533322)

Also, 当 这也是repeated later on in the page, 它是 EXTREMELY important for you to understand that, if this feature is used in conjunction with *any* 字符串 sourced from a 玩家, that *will* allow the 玩家 to use *any* mythic 技能 (**指令 技能 included**) in a trivially easy way. So, to reiterate: make sure 一切 that ends up in a dynamic 元技能 已被 made by a developer and 不是 dependent on user input or user-controlled 值, or make sure the user controller 值 is validated and sanitized

# How does this work?
Basically, it all boils down to two things:
- The usage of the [variableskill 技能]
- The existence of [内联 元技能]

By combining those two things, 它是 now possible to do 某事 like this
```yaml
Testmob:
  Type: pig
  Skills:
  - skill{s=
    [
      - setvariable{var=skill.temp;type=STRING;val=glow} @self
      - setvariable{var=skill.testskill;type=STRING;
        val=
        [
          - message{m=hello} @World
          - message{m=world} @World
          - message{m=<skill.var.temp>} @World
        ]} @self
      - vskill{s=<skill.var.testskill>}
      - vskill{s=
        [
          - particle{p=<skill.var.temp>} @selflocation{y=2}
        ]} @self
    ]} @self ~onInteract
```
![2024-08-17_17.54.14](uploads/81ec8a247b38cc3eba7daca275b46b03/2024-08-17_17.54.14.png)

# What is happening?
The variableskill 技能 is a very interesting one: it 执行 the 元技能 it finds in its `skill` 属性 之后 parsing its content. While 这是 normally used 仅 to 执行 元技能 whose 名称 can depend on specifics of the 生物 or environment 此刻 of the execution (making it very useful for templating) this 也 has an unexpected 效果 when combined with 内联 元技能: 只要 它是 written as a 内联 元技能, 您可以 make the variableskill 技能 parse 任何事物 and expect it to get executed


# Dynamic Creation of 元技能
And now, we come to the crux of the matter: you are now able to make 完全 new and 唯一 元技能 on the spot 没有 having to physically configure them
```yaml
Testmob:
  Type: pig
  Skills:
  - skill{s=
    [
      - setvariable{var=skill.temp;type=STRING;val=glow} @self
      
      - setvariable{var=skill.testskill2;type=STRING;val="["}
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2> - message{m=aaa} @World} @self
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2> - message{m=bbb} @World} @self
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2>]} @self
      
      - vskill{s=<skill.var.testskill2>}
      - vskill{s=
        [
          - particle{p=<skill.var.temp>} @selflocation{y=2}
        ]} @self
    ]} @self ~onInteract
```


# Bypassing 占位符支持Limits。
NoNot every 属性 of every 技能, 条件 or 目标选择器 has支持for 占位符. This is 经常 a limiting factor for a lot of advanced projects. But not anymore!。
Let look at the 示例 above: at the time of writing the 粒子 技能 不 have 占位符支持for its 粒子 属性, and 还 that works when used 与 methods described here. How come?。
TThat is 因为 the vskill 技能 自身 is parsing the 值 of that 占位符 *之前* 任何事物 else is executed, and when the 粒子 技能 is called 一切 has 已经 been parsed for it

One must then 注意 that this operation 不是 exclusive to 技能 属性: 您可以 literally use 占位符 for *every single character* of the 字符串 即 being built, and, 只要 结果 之后 parsing can then be considered a proper 内联 元技能, 它将 work!


# Storing Dynamic 元技能
As you 已经 saw, the newly made 元技能 is being stored inside a 变量. The 变量 can have any 作用域 you deem fit, persist for 只要 您想要 and have all the 其他 cool stuff 变量 have. You can 也 store these 技能 inside NBTs, making 物品 of your making being able to have 完全 自定义 技能 对于m

> Please 注意 that storing this 类型 of data inside NBTs can be dangerous if the 玩家 in your 服务器 have some degree of control 在ir 物品. For instance, in a 服务器 with creative 模式 启用, a 玩家 could fetch 物品 从ir saved ones with 自定义 NBTs in them and 执行 arbitrary code at will


# Limitations
Since this 不是 a planned feature, its implementations do have some problems.
- Usage of 其他 "技能" 技能 内联: when using "技能", "sudoskills" or 其他 such 技能 技能 directly 内联 will 结果 in a console 错误 if used 没有 delays, 不 技能 being executed. To solve this, 它是 necessary to do one of two things:
- continue using the vskill 技能 in place of these 其他 ones. For the 技能 技能 a simple replace will work, but to use a sudoskill 您将 need to make a vskill 技能 call a 元技能 that 执行 said sudoskill 技能 自身
-- use a delay of approximately 15 ticks 之前 the execution of 其他 metamechanics
```yaml
ExampleWorkaround:
  Skills:
  - vskill{s=
    [
      - vskill{s=YourOtherMetaskill}
      - vskill{s=SudoskillWrapper;run=TheMetaskillToBeSudoed}
    ]}

SudoskillWrapper:
  Skills:
  - sudoskill{s=
    [
    - vskill{s=<skill.run>}
    ]} 

AnotherWorkaround:
  Skills:
  - vskill{s=
    [
      - vskill{s=YourOtherMetaskill}
      - vskill{s=SudoskillWrapper;run=
        [
        - message{m=<caster.name>} @World
        ]}
    ]}

```

```yaml
DelayWorkaround:
  Skills:
  - setvariable{var=skill.test;type=string;value=message} @self
  - vskill{
      skill=[
        - delay 15
        - randomskill{
            skills=[
              - <skill.var.test>{m=1}
            ],
            [
              - <skill.var.test>{m=2}
            ]} @self
      ]} @self

```

<!-- LINKS -->
[variableskill 技能]: /技能/技能/variableskill
[variableskill]: /技能/技能/variableskill
[内联 元技能]: /技能/元技能#内联-元技能