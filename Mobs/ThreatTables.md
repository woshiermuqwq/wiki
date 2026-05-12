仇恨表 change how a 生物 tracks its targets. Normally Minecraft 生物 不要 follow any kind of rigid system of what to 目标 - 它们将 仅仅 bounce back and forth between attacking whatever hits them. 仇恨表 change that.

With 仇恨表 启用, 生物 will keep track of how much 伤害 each 玩家 does to them, and will 攻击 the 玩家 that deals the most 伤害. That way 您可以 avoid scenarios where one 玩家 will hit a 生物 and then run away 当 其他s follow behind smacking it forever, trivializing it.

仇恨表 附带 several built-in features to make the 生物 targeting intelligent, and use rules found in common MMORPGs. 玩家 gain 仇恨 by dealing 伤害, and will lose 仇恨 if they kite the Boss, stay outside of the Boss' MaxCombatRange, or stay 从 line of sight for long periods of time. 玩家 还将 掉落 仇恨 if they leave the 世界 or log off.

生物 只会 switch targets if 另一个 玩家 passes `110%` 仇恨 在 current 目标.

>注意 that activating 仇恨表 will 略微 change the [AI 目标选择器](/生物/自定义-AI#ai-目标-selectors) you specified 对于 生物. A 生物 with activated 仇恨表将attemptto 攻击 any 实体 that deals 伤害 to it - 即使 such entites are not listed in the AI 目标选择器 or 即使 the AI 目标选择器 列表 对于 生物 已被 swiped clean and the 生物 不 naturally 攻击 任何事物 or 任何人。

## Enabling 仇恨表

Turning on 仇恨表 for a 生物 is easy. Just 添加 Modules.ThreatTable: true to your 生物, like this:

```yaml
BigScaryBoss:
  Type: zombie
  Display: '&6Zombie'
  Health: 20000
  Modules:
    ThreatTable: true
```

You can 也 enable 仇恨表 using the [生物 选项 section](/生物/选项#usethreattable)

That it!

## Manipulating 仇恨 等级

若a 生物 has 仇恨表 启用，it将will总是 目标 the 实体 与 highest 仇恨 等级 on its own 仇恨表. This process is fully automated and 基于 which 实体 does how much 伤害 to the 生物. Naturally, the 实体 (通常 a 玩家) dealing the most 伤害, will gain the most 仇恨 and become the 目标 of the 生物。

However if you would like to manually make your 生物 目标 specific entites, or 仅 throw in some tweaks that make your 生物 targeting even smarter, 您可以 do so using the [仇恨 机制](/技能/机制/仇恨).

仇恨表 也 附带 an API, 包括 a “taunt” method and 仇恨 altering method if 另一个 插件 author ever wanted to have 技能 or abilities that interact with 仇恨.