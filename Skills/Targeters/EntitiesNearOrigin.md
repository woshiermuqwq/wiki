## 描述
Ta以all 实体 in the given 半径 在...周围 原点 of the 元技能为目标。
This 目标选择器 is an extension of the **[EntitiesInRadius 目标选择器](/技能/目标选择器/EntitiesInRadius)** and can, as such, **use any of its 属性**


## 属性
>*This 目标选择器 has no 唯一 属性, but can use the [EntitiesInRadius](/技能/目标选择器/EntitiesInRadius) ones*


## 示例
In this 示例, when the created 弹射物 ends for whatever reason, 它将 伤害 every living 实体 in a 2 方块 半径 around 自身
```yaml
  Skills:
  - projectile{...;
    onTick=[
      - effect:particles @origin
    ];
    onEnd=[
      - damage{a=10} @ENO{r=2}
    ]
    } @target
```


## 别名
- [x] NearOrigin
- [x] ENO