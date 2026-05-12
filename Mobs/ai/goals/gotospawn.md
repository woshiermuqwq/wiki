## 描述
使生物travel to its original 生成 位置。


## 属性
| 属性 | 别名 | Description | 默认 |
|----------------|----------|------------------------------------|:-------:|
| 速度 | s | 移动 速度 modifier | 1 |
| minRange | min, mr | How far the 生物 需要 be from its 生成 位置 to consider 自身 "at the 位置". The 生物 will walk towards its 生成 位置 直到 它是 this 靠近 it. | 2 |
| maxRange | max, r | The maximum 范围 the 生物 can be from its 生成 位置. If the 生物 is further than this 数量 from its 生成 位置, 它将 activate the AI 目标 and walk 朝向 生成 位置 直到 it reaches the minimum 范围. | 16 |
| dropTarget | dt | Whether or not the 生物 should 掉落 its current 目标 when this AI 目标 activates. | true |


## 示例
This zombie将tryto melee 攻击 its 目标 直到 它是 多于 20 方块 from its 生成 位置, then will turn around and walk back to where it spawned。
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - goToSpawn{speed=1;max=20;min=4}
    - meleeattack
```


## 别名
- [x] gotospawnlocation