**难度：初学者**

大多数生物类型在 Minecraft 中都有自己的默认行为，其中许多可以通过 [CancelEvent](/skills/mechanics/cancelevent) 机制来阻止，让你能够用自定义操作替换原版行为！

一个常见的例子是用 ~onAttack 取消生物的攻击，然后用你自己的攻击技能代替。

请记住，CancelEvent 需要原始机制上的 `sync=true` 通用属性，且并非所有触发器都受支持。可用触发器列表见 [CancelEvent](/skills/mechanics/cancelevent) 机制页面。你还可能遇到一些特殊情况，如取消死亡事件来创建自定义死亡效果，或取消伤害事件来自定义伤害但陷入死循环的情况，以下是针对这些情况的技巧。

# 攻击
这是一个取消生物攻击并创建自己的攻击技能代替的示例。

在你的生物上运行此机制：

`- skill{s=FireAttack;sync=true} @target ~onAttack`

在你的技能文件中创建一个如下所示的元技能：
```yaml
FireAttack:
  Skills:
  - cancelevent
  - damage{a=5}
  - ignite @target
```

你也可以对远程生物使用 onShoot 触发器，因为它们的默认射击无法被修改，你可以先取消它，然后用 [Projectile](/skills/mechanics/projectile) 或 [Shoot](/skills/mechanics/shoot) 等机制创建自己的射击！

以下示例，如果应用到骷髅上，会使其发射多支造成更多伤害的箭，而不是标准的单箭攻击。

`- skill{s=ArrowVolley;sync=true} @target ~onShoot`

```yaml
ArrowVolley:
  Skills:
  - cancelevent
  - volley{type=EGG;velocity=5;damage=10;amount=20}
```

# 伤害

你可以取消生物的伤害事件，无论是让生物无敌，还是修改其承受伤害的方式。

使用此方法让生物无敌非常简单，只需将其添加到生物的 skills 部分：

`- cancelevent{sync=true} @self ~onDamaged`

你可以配合条件使用，使生物仅在特定情况下无敌。以下示例将使生物只在玩家用钻石剑攻击时才无敌。此示例使用了[内联触发器条件](/Skills/Inline-Conditions#conditions-triggerconditions)

`- cancelevent{sync=true} @self ~onDamaged ?~holding{m=DIAMOND_SWORD}`

以下示例将取消生物受到的所有伤害，并用 damage 机制替代，使生物始终受到固定数值的伤害，无论使用什么武器。由于我们取消了伤害然后直接对生物造成伤害，会导致死循环，因此我们使用 damageTag 来检查标签是否存在——如果标签存在，则不取消伤害，生物将正常受伤。

`- skill{s=SelfDamage;sync=true} @self ~onDamaged`

```yaml
SelfDamage:
  Conditions:
  - damageTag{tag=SELFDAMAGE} false
  Skills:
  - cancelevent
  - damage{a=10;tag=SELFDAMAGE} @self
```

# 死亡

你可能想取消死亡事件来创建带有华丽效果的自定义死亡。我们需要使用 remove 机制移除生物，而不是让它因伤害自然消失。所以如果取消死亡，请注意 onDeath 技能将不起作用，需要将它们合并到这里，比如发放奖励等内容。

`- skill{s=DeathSkill;sync=true} @self ~onDeath`

```yaml
DeathSkill:
  Skills:
  - cancelevent
  - delay 10
  - fakeexplosion @self
  - particlesphere{particle=flame;amount=200;radius=5;repeat=5;repeatinterval=5} @self
  - delay 20
  - remove @self
```
