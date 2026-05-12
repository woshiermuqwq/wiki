Audience 属性可以usedto 显示 an 效果 仅 to a specific group of 玩家, 而不是 the entire 服务器, by using the `audience=<audience type>` 属性 in a 技能 that supports audiences and specifying an audience 类型 to use. This can be useful in preventing 也 many 粒子 from being displayed to 每个人 unnecessarily, and can reduce client-side lag to some extent。

The audience 类型 are:
- `self`/`caster`: the 施法者 of the 技能
- `nonSelfWorld`/`nonSelf`: every 玩家 in the 世界 其他 than the 施法者 of the 技能
- `target`: the 目标 of the 技能
- `world`: every 玩家 in the 世界
- `tracked`/`trackedplayers`/: every 玩家 whose client can render the 施法者
- `nearby`/`nearbyplayers`: every nearby 玩家 (closer than `65536` 方块)
- `@Targeter`: every 玩家 that the 目标选择器 targets

> The 默认 值 is `tracked`

Of particular relevance is the `audience=@Targeter` 属性, that 允许 any 实体 目标选择器 to be used as the audience of the 效果
```yaml
    Skills:
    - effect:particles{particle=reddust;y=2;audience=@Owner} @self
```