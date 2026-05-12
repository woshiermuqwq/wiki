## 描述
以a 位置 在...前方 the casting 弹射物, relative to its 方向为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| forward | f, 数量, a | How far ahead should the targeted point be | 1 |
| rotate | rot | The 旋转, 在...周围 弹射物, of the 目标 位置 | 0 |


## 示例
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles{p=flame} @ProjectileForward{f=2}
      - effect:particles @Origin
    ]}
```