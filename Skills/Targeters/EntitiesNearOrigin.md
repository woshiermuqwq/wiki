## 描述
选取嵌套技能原点周围指定半径内的所有实体。  
此目标选择器是 **[EntitiesInRadius 目标选择器](/Skills/Targeters/EntitiesInRadius)** 的扩展，因此**可以使用它的所有属性**


## 属性
>*此目标选择器没有独有属性，但可以使用 [EntitiesInRadius](/Skills/Targeters/EntitiesInRadius) 的属性*


## 示例
在此示例中，当创建的弹射物以任何方式结束时，都会对自身周围 2 格半径内的所有活体实体造成伤害
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
