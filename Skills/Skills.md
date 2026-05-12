技能是 MythicMobs 的核心功能。
所有生物（如果你安装了 [Crucible] 扩展，物品也一样）都可以拥有多种类型的技能，它们可以在不同情况下被不同类型的触发器激活，
并附带不同的条件。MythicMobs 的技能系统一旦上手就非常直观，可以用来创建从简单生物到极其复杂的 Boss 等各种内容。

技能由几个不同的部分组成：

-   [技能]
-   [目标选择器]
-   [触发器]
-   [条件]

# 入门

那么，什么构成一个技能？

技能由[技能技能][技能]（或称为"基础技能"）组成，这些是 MythicMobs 自带的基础技能。每个技能技能在生物的 **Skills** 部分中调用。让我们来看一个例子：

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

每个技能技能以列表形式分配给生物。但一个真正的技能是什么样子？来看一个实际例子：
```yaml
FieryZombie:
  Type: ZOMBIE
  Display: 'Fiery Zombie'
  Health: 50
  Skills:
  - ignite{ticks=100} @target ~onAttack <50% 0.5
```

哇！这些都代表什么？让我们拆解一下构成这个技能的各个部分：

```yaml
Skills:
- mechanic{argument=value} @[targeter] ~on[trigger] [health_modifier] [chance]
```

这可能看起来有点吓人，但每个部分单独来看都非常简单，而且有些甚至是可选的。让我们逐个分解！

## 技能

技能的第一个、也是最重要的部分，是技能。它定义了你想做什么，是你正在执行的基础技能。它可能是造成伤害、点燃目标、或者释放闪电。[有大量不同的技能][技能]可供使用，主要分为两种类型：以实体为目标的技能，和以位置为目标的技能。有些可以同时针对两者，也有些两者都不需要。

大多数技能也有参数。它们紧跟在技能名称之后，用花括号 {} 包裹。每个参数用分号（;）分隔。每种技能都有自己独特的参数，全部可以在[技能]维基页面查阅。

```yaml
Skills:
- mechanic{option1=value;option2=value;option2=value;...}
```

你也可以扩展语法使其更易读，但必须保持正确的缩进，否则 YAML 会报错。以下是我个人推荐的格式，兼顾清晰和整洁：

```yaml
Skills:
- mechanic{option=value;
           option=value;
           option=value}
```

设置一个技能很简单：确定你想使用的技能，然后填入你需要的选项。大多数选项都有默认值且是可选的。所以如果你想把人点燃 5 秒，你可以使用 ignite 技能并将 "ticks" 选项设为 100（每秒 20 tick）：

```yaml
Skills:
- ignite{ticks=100}
```

## 目标选择器

目标选择器是实现技能的另一个核心部分。目标选择器定义了"你想让技能瞄准什么"。目标选择器有很多类型，大多数可以归类为以"实体"为目标或以"位置"为目标。选择正确的目标选择器对你想要达成的效果至关重要。[这里列出了所有目标选择器]。

目标选择器直接跟在技能后面的技能行中，始终以 @ 符号为前缀。有些还可以有自己的选项，同样用花括号跟在目标选择器后面。

```yaml
    Skills:
    - mechanic{option=value} @targeter{option1=value;option2=value;...}
```

回到我们之前的例子，假设你想让生物的攻击目标着火。你只需这样做：

```yaml
Skills:
- ignite{ticks=100} @target
```

或者你想让附近所有玩家都着火。假设在 5 格半径内：

```yaml
Skills:
- ignite{ticks=100} @PlayersInRadius{radius=5}
```

本质上，目标选择器就是你想让技能命中的对象。

## 触发器

触发器也是技能中非常重要的部分。触发器决定了"什么事件导致此技能触发"。

触发器直接跟在目标选择器后面，通常以 **~on** 开头，后面跟触发器名称。

```yaml
Skills:
- mechanic{option=value} @targeter{option=value} ~onTrigger
```

回到之前的例子，假设你想让此触发器在生物攻击其目标时触发，这样它的近战攻击也会附带火焰。

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack
```

有些目标选择器还与特定触发器配合使用。例如，@Trigger 目标选择器以触发该技能的实体为目标。在下面的例子中，右键点击生物（与生物互动）的玩家会被点燃，因为他就是 @Trigger。

```yaml
Skills:
- ignite{ticks=100} @Trigger ~onInteract
```

**注意：物品有一套不同的触发器。[点击此处查看 Crucible 支持的触发器]。**

## 血量修正

血量修正是一种特殊类型的条件，跟在触发器后面。这让你可以方便地设置技能执行的血量范围，而且是完全可选的。血量修正有几种简单的形式，以下是一些示例：

-   **=90%** - 技能仅在生物血量低于 90% 时触发。请注意，使用此修正会导致技能只触发一次。
-   **&lt;50%** - 技能仅在生物血量低于 50% 时触发。
-   **=30%-50%** - 技能仅在生物血量在 30% 到 50% 之间时触发。
-   **&lt;2000** - 技能仅在生物血量低于 2000 时触发。
-   **&gt;500** - 技能仅在生物血量高于 500 时触发。

血量修正在触发器之后，以 **=**、**&lt;** 或 **&gt;** 为前缀，取决于你想使用的范围。

```yaml
Skills:
- mechanic{option=value} @targeter{options=value} ~onTrigger =/</> HealthModifier
```

回到我们之前的例子，假设你想让技能仅在生物血量低于 50% 时生效：

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack <50%
```

## 概率

概率是你可以添加到技能行上的另一个简单且可选的条件。概率始终是技能行的最后一项，是一个简单的小数：1.0 表示 100%，0.5 表示 50%，0 表示 0%。

总结这个示例，假设你想让此触发器在血量低于 50% 时，以 50% 的概率在近战攻击时触发：

```yaml
Skills:
- ignite{ticks=100} @target ~onAttack <50% 0.5
```

# 总结

如你所见，虽然原始技能行看起来令人望而生畏，但分解成各个部分后，事情就变得简单多了。

当你掌握了使用单个基础技能的技巧后，就可以使用元技能将它们组合成更复杂的技能。这将在后续文章中介绍。

  [Crucible]: https://git.mythiccraft.io/mythiccraft/mythiccrucible
  [技能]: /Skills/Mechanics/
  [目标选择器]: /Skills/Targeters/
  [触发器]: /Skills/Triggers/
  [条件]: /Skills/conditions/
  [这里列出了所有目标选择器]: /Skills/Targeters/
  [点击此处查看 Crucible 支持的触发器]: https://git.mythiccraft.io/mythiccraft/mythiccrucible/-/wikis/Skills/Triggers

# 速查表
![image](uploads/ebf67740e7bc604db56a95cf62397030/image.png)
> 你可以使用这张由 [ShenKuro](https://discord.com/users/695202854134218763) 制作的精美速查表。
