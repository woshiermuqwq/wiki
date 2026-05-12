## 描述
选取施法弹射物前方（相对于其方向）的一个位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| forward   | f, amount, a | 目标点在前方多远处                        | 1       |
| rotate    | rot       | 目标位置绕弹射物的旋转角度          | 0       |


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
