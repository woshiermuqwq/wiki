内联条件可以用于单独的技能和目标选择器上，让你不必为一些较基础的需求而创建完整的元技能，同时也能在已有的元技能中提供更大的灵活性。你可以使用标准条件来检查施法者，使用触发者条件检查触发者，以及使用目标条件检查目标。

内联条件可以用在生物文件、技能文件中，如果你有 Crucible 扩展，也可以用在物品文件中。

[[_TOC_]]

# 条件（内联）

这些条件检查施法者本身，它们写在技能行的末尾，以 `?` 开头。在下面的例子中，消息只会下雨时发送。
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me in the rain?"} @trigger ~onDamaged ?raining
```

条件为真时使用 `?`，条件为假时使用 `?!`：
- `?raining` — 如果*正在下雨*则为真
- `?!raining` — 如果*没有下雨*则为真

# 触发者条件（内联）

你也可以检查技能的触发者。用法与上面相同，但在 `?` 后面需要加 `~`。下面的例子只有当攻击生物的玩家手持木剑时，才会向该玩家发送消息。
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword?"} @trigger ~onDamaged ?~holding{m=WOODEN_SWORD}
```

与标准条件一样，为真时使用 `?~`，为假时使用 `?~!`：
- `?~holding{m=WOODEN_SWORD}` — 如果玩家*手持*木剑则为真
- `?~!holding{m=WOODEN_SWORD}` — 如果玩家*没有手持*木剑则为真

### 多个条件

你可以在技能中使用任意数量的内联条件和触发者条件。只需记住，**所有**条件都必须满足，技能才会运行。在下面的例子中，消息只有同时满足正在下雨、是夜晚、且攻击生物的玩家手持木剑这三个条件时才会发送。

```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - message{m="You hit me with a wooden sword? in the rain?? at night???"} @trigger ~onDamaged ?raining ?night ?~holding{m=WOODEN_SWORD}
```


# 目标条件（内联）
**内联目标条件仅高级版可用！**

内联目标条件允许你将条件应用在目标选择器上，从而精确锁定你想要的目标实体/位置。先来看看它的格式。

下面的例子中，生物会每秒对所有 10 格范围内拥有 `Plagued` 光环的玩家造成 1 点伤害。
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true ]} ~onTimer:20
```

内联目标条件的空格至关重要。注意 `conditions=[` 和 `- hasaura{aura=Plagued} true` 之间有两个空格，你必须要保留这个双空格。
还要注意 `true` 到 `]}` 之间有一个空格，这个空格也必须保留。

你也可以在单个目标选择器上使用多个条件，有两种写法。

缩进换行写法示例：
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[
                              - hasaura{aura=Plagued} false
                              - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true 
                              ]} ~onTimer:20
```
注意第二条条件末尾的 `true` 之后仍然有一个空格。

单行写法示例：
```yaml
SkeletalKnight:
  Type: WITHER_SKELETON
  Skills:
  - damage{a=1} @PIR{r=10;conditions=[  - hasaura{aura=Plagued} true  - haspotioneffect{type=WITHER;d=1to999999;l=0to254} true ]} ~onTimer:20
```
注意 `conditions=[` 与第一条条件之间有两个空格，第一条条件与第二条条件之间也有两个空格。最后，第二条条件末尾的 `true` 之后仍然有一个空格。