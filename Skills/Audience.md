受众属性用于控制效果只展示给特定的玩家群体，而不是全服所有玩家。在支持受众的技能中使用 `audience=<受众类型>` 属性并指定一种受众类型即可。这对于避免过多粒子效果不必要地展示给所有人非常有用，也能在一定程度上减轻客户端卡顿。

受众类型包括：
- `self`/`caster`：技能的施法者
- `nonSelfWorld`/`nonSelf`：当前世界中除施法者外的所有玩家
- `target`：技能的目标
- `world`：当前世界中的所有玩家
- `tracked`/`trackedplayers`：客户端能渲染施法者的所有玩家
- `nearby`/`nearbyplayers`：附近的所有玩家（距离小于 65536 格）
- `@Targeter`：目标选择器所选中目标的所有玩家

> 默认值为 `tracked`

其中 `audience=@Targeter` 属性尤为实用，它允许使用任意实体目标选择器来作为效果的受众。
```yaml
    Skills:
    - effect:particles{particle=reddust;y=2;audience=@Owner} @self
```