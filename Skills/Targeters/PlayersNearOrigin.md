## 描述
选取嵌套技能原点周围指定半径内的所有玩家。  

## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |


## 示例
在此示例中，当创建的弹射物以任何方式结束时，都会对自身周围 2 格半径内的所有玩家造成伤害
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
