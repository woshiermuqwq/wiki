## 描述
Ta以all 玩家 in the given 半径 在...周围 原点 of the 元技能为目标。

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |


## 示例
In this 示例, when the created 弹射物 ends for whatever reason, 它将 伤害 every 玩家 in a 2 方块 半径 around 自身
```yaml
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles @origin
    ];
    onEnd=[
      - damage{a=10} @PlayersNearOrigin{r=2}
    ]
    } @target
```


## 别名
- [x] playersnearsource
- [x] PNO