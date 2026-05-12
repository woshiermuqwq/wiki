技能是 MythicMobs 的核心功能。
所有生物（如果你安装了 [Crucible] 扩展，物品也可以）都能配备不同类型的技能，这些技能可以在各种情境下触发，并受到不同条件的约束。MythicMob 的技能系统上手后非常直观，无论是制作简单的生物还是极其复杂的 Boss，都能用它来完成。

一条技能由以下几个部分构成：

-   [技能]
-   [目标选择器]
-   [触发器]
-   [条件]


# 入门指南

那么，一条技能到底是什么？

技能由[技能][技能]（也叫「基础技能」）组成，技能是 MythicMobs 自带的最基本单位。每条技能都在生物的 **Skills** 部分中调用。让我们看一个例子：

```yaml
FieryZombie:
  Type: ZOMBIE
  Display: 'Fiery Zombie'
  Health: 50
  Skills:
  - mechanic1
  - skill{skill=Skill1}
  - skill{s=Skill2}
  - skill:Skill3
  - etc
```

每条技能像上面这样以列表形式分配给生物。但一条真正的技能长什么样呢？这里有个实际例子：

```yaml
FieryZombie:
  Type: ZOMBIE
  Display: 'Fiery Zombie'
  Health: 50
  Skills:
  - ignite{ticks=100} @target ~onAttack <50% 0.5
```

看着有点吓人！这些东西都代表什么？让我们拆开来看：

```yaml
Skills:
- mechanic{argument=value} @[targeter] ~on[trigger] [health_modifier] [chance]
```

虽然看起来还是有些复杂，但每个部分单独拿出来都很简单，有些甚至不是必须的。下面我们逐个拆解！


## 技能

技能是技能行的第一部分，也是最重要的部分——它决定了「你要让什么发生」，是你所执行的基础技能。它可以造成伤害，可以将目标点燃，或者召唤闪电。[有很多种不同的技能][技能]可供选择，大体上可以分为两类：以实体为目标的技能，以及以位置为目标的技能。部分技能可以同时以两者为目标，或者两者皆不。

大多数技能还有参数。参数紧跟在技能名后面，用花括号 `{}` 括起来。多个参数之间用分号 `;` 分隔。每个技能都有自己的一套参数，全部列在[技能]维基页面上。

```yaml
Skills:
- mechanic{option1=value;option2=value;option2=value;...}
```

假如你更看重可读性，也可以换一种展开的写法，但缩进必须正确，否则 YAML 会报错。下面是个人推荐的一种格式，既清晰又整洁：

```yaml
Skills:
- mechanic{option=value;
           option=value;
           option=value}
```

配置一条技能，其实就是找到你想用的技能，然后填入你需要的选项。大部分选项都有默认值，不填也没关系。假如你想把某个目标点燃 5 秒钟，那就可以用点燃（ignite）技能，然后把 `ticks` 选项设为 100（每秒等于 20 刻）：

```yaml
Skills:
- ignite{ticks=100}
```


## 目标选择器

目标选择器是技能实现的另一个核心部分。目标选择器表示「你希望技能瞄准谁」。目标选择器的类型很多，大多可以分为「实体」和「位置」两类。选对目标选择器很重要。[这里是所有目标选择器的列表。]

目标选择器紧跟在技能名称后面，始终以 `@` 符号开头。部分目标选择器也可以有自身的选项，同样用花括号括起来。

```yaml
Skills:
- mechanic{option=value} @targeter{option1=value;option2=value;...}
```

回到之前的例子：假设你想让技能点燃生物当前的目标，那这样写就行……

```yaml
Skills:
- ignite{ticks=100} @target
```

或者，你想点燃周围所有玩家，例如半径 5 格范围内……

```yaml
Skills:
- ignite{ticks=100} @PlayersInRadius{radius=5}
```

简单来说，目标选择器决定了「技能会打在谁身上」。


## 触发器

触发器同样是技能中非常重要的一部分。触发器决定了「什么事件会引发这条技能」。

触发器紧跟在目标选择器后面，一般以 **~on** 开头，后接触发器名称。

```yaml
Skills:
- mechanic{option=value} @targeter{option=value} ~onTrigger
```

继续沿用前面的例子：假设你想让生物每次近战攻击时都额外附加火焰效果，就这样写：

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack
```

部分目标选择器和特定的触发器配合得天衣无缝。比如 `@Trigger` 这个目标选择器会选中触发技能的那个实体。下面的例子里，右键点击生物（与之交互）的玩家会被点燃，因为他就是 `@Trigger`。

```yaml
Skills:
- ignite{ticks=100} @Trigger ~onInteract
```

**注意：物品有一套不同的触发器。[点此查看适用于 Crucible 的触发器。]**


## 生命值修饰符

生命值修饰符是一种特殊的条件，写在触发器后面。它可以让你方便地设定技能在哪些生命值区间内执行，属于可选内容。生命值修饰符有几种简单的形式，下面列举一些例子：

-   **=90%** — 技能仅在生物生命值低于 90% 时触发。请注意，使用这种写法时，技能只会触发一次。
-   **&lt;50%** — 技能仅在生物生命值低于 50% 时触发。
-   **=30%-50%** — 技能仅在生物生命值位于 30% 到 50% 之间时触发。
-   **&lt;2000** — 技能仅在生物生命值低于 2000 时触发。
-   **&gt;500** — 技能仅在生物生命值高于 500 时触发。

生命值修饰符紧跟在触发器后面，前缀为 **=**、**&lt;** 或 **&gt;**，取决于你要使用的区间。

```yaml
Skills:
- mechanic{option=value} @targeter{options=value} ~onTrigger =/</> HealthModifier
```

继续前面的例子：假设你希望技能仅在生命值低于 50% 时才生效：

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack <50%
```

## 概率

概率是另一个简单且可选的技能行条件。概率永远放在技能行的最后，是一个简单的十进制小数：1.0 表示 100%，0.5 表示 50%，0 表示 0%。

为这个例子收个尾：假设你想让生物在生命值低于 50% 时，只有一半的近战攻击会附加火焰效果：

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack <50% 0.5
```

# 总结

可以看到，原始的技能行虽然看起来复杂，但拆开后每个部分都很清晰。

在掌握了单个基础技能的用法之后，你可以通过元技能将它们组合成更复杂的技能。这将在后续文章中介绍。

  [Crucible]: https://git.mythiccraft.io/mythiccraft/mythiccrucible
  [技能]: /Skills/Mechanics/
  [目标选择器]: /Skills/Targeters/
  [触发器]: /Skills/Triggers/
  [条件]: /Skills/conditions/
  [这里是所有目标选择器的列表。]: /Skills/Targeters/
  [点此查看适用于 Crucible 的触发器。]: https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers

# 速查表
![image](uploads/ebf67740e7bc604db56a95cf62397030/image.png)
> 你可以使用这张由 [ShenKuro](https://discord.com/users/695202854134218763) 制作的精美图表