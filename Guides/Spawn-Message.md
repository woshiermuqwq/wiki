**难度：初学者**

你可能有一个特殊生物生成时（如 Boss）想让服务器上的玩家知道。可以使用 [Message 机制](/skills/mechanics/message) 结合 [onSpawn 触发器](/Skills/Triggers/onSpawn) 来实现。

值得注意的是，对于从当前未加载区块中的生成器生成的生物，此方法可能不起作用。

在这个基础示例中，我们简单地向 [@server](/Skills/Targeters/PlayersOnServer) 发送消息，通知他们生物已生成。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Skills:
  - message{m="&6骷髅王已生成！"} @server ~onSpawn
```

效果不错，但你也许还想让生物向玩家显示其坐标！可以使用[施法者占位符](/Skills/Placeholders)来实现。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Skills:
  - message{m="&6骷髅王已生成！你可以在以下坐标找到它：&aX<&co>&b<caster.l.x> &aY<&co>&b<caster.l.y> &aZ<&co>&b<caster.l.z>"} @server ~onSpawn
```

我们使用了以下占位符：
- `<&co>` 插入一个 `:` 符号，直接使用冒号会干扰语法。
- `<caster.l.x>` 显示施法者的 X 坐标
- `<caster.l.y>` 显示施法者的 Y 坐标
- `<caster.l.z>` 显示施法者的 Z 坐标
