In-Line 条件可以usedon individual 机制 and 目标选择器 to save you from having to create an entire 元技能 for more basic things and to give you more flexibility inside existing 元技能. You can use standard 条件 to 检查 再次st the 施法者, TriggerCondtions to 检查 再次st the 触发器, and TargetConditions to 检查 再次st the 目标。

In-Line 条件可以usedin 生物 文件, 技能 文件 and if you have Crucible, 它们可以 be used in 物品 文件 也。

[[_TOC_]]

# 条件

These 条件 will 检查 再次st the 施法者 自身, they go at the end of a 机制 line and begin with `?`. In the below 示例 the 消息 只会 be sent if 它是 当前 raining.
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me in the rain?"} @trigger ~onDamaged ?raining
```

For the 条件 to be true, 您可以 use `?` and 对于 条件 to be false 您使用 `?!`
- `?raining` - True, if it *is* raining
- `?!raining` - False, if 它是 *not* raining

# TriggerConditions

You can 也 检查 再次st the 触发器 of the 机制. It is the same process as above but 您使用 a `~` 之后 the ?. The below 示例 只会 send a 消息 to the 玩家 who hit the 生物, if that 玩家 is holding a wooden sword.
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword?"} @trigger ~onDamaged ?~holding{m=WOODEN_SWORD}
```

Just like the standard 条件, for true 您可以 use `?~` and 对于 条件 to be false 您使用 `?~!`
- `?~holding{m=WOODEN_SWORD}` - True, if the 玩家 *is* holding a wooden sword
- `?~!holding{m=WOODEN_SWORD}` - False, if the 玩家 is *not* holding a wooden sword

### Multiple 条件

You are able to use as many In-line 条件 and TriggerConditions as 您需要 in your 机制. Just remember that *all* 条件 必须 be met 对于 机制 to run, in this below 示例 the 消息 只会 be sent if 它是 raining, *and* night, *and* the 玩家 who attacked the 生物 is holding a wooden sword.

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword? in the rain?? at night???"} @trigger ~onDamaged ?raining ?night ?~holding{m=WOODEN_SWORD}
```


# TargetConditions
**In-Line TargetConditions are Premium Only!**

IIn-line 目标 条件 allow you to 应用 条件 to your 目标选择器 so that you 仅 目标 the exact 实体 / 位置 you are looking for. First lets look at the formatting of it.

In this 示例 a 生物 would deal 1 伤害 to any 玩家 在...内 10 方块 that have the 光环 ``Plagued`` every second.
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true ]} ~onTimer:20
```

The spacing is crucial for in-line 目标 条件. Notice that there is two spaces between ``conditions=[`` and ``- hasaura{aura=Plagued} true``. You need to have that double space there.
Also notice that there is one space from ``true`` to ``]}`` and that space 需要 be there as well.

You can 也 use multiple 条件 on a single 目标选择器, there is 2 ways of doing this.

示例 of droping down a line and indenting:
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[
                              - hasaura{aura=Plagued} false
                              - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true 
                              ]} ~onTimer:20
```
注意 that there is 仍然 a space 之后 the true at the end of the second 条件.

示例 of keeping multiple 条件 on one line:
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true  - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true ]} ~onTimer:20
```
注意 that there is two spaces between ``conditions=[`` and the first 条件, then 有lso two spaces 在...之间 first 条件 and the second 条件. Finally there is 仍然 one space 之后 the true at the end of the second 条件.