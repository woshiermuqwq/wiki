## 描述
以all 物品 in a 半径 在...周围 原点 of the 元技能为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |

## 示例
In this 示例, a 弹射物 launched by a 玩家 will make the 施法者 pick up every 物品 in a 5 方块 半径 在...周围 弹射物 every execution of the onTick 元技能
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onTick=[
      - pickupitem @ItemsNearOrigin{r=5}
    ]}
```


## 别名
- [x] INO