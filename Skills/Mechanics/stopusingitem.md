## 描述
Stops the targeted living entity from using an item, 即 blocking with a 护盾.
> If you want to do some sort of 冷却, try using this 技能 in an 光环


## 属性
> *This 技能 has no attributes*


## 示例
```yaml
Skills:
  # basic example
  - stopusingitem @NearestPlayer
  
  # with an aura to prevent the player from using a shield
  - aura{onTick=[ - stopusingitem ?isBlocking ];duration=500} @NearestPlayer
```


## 别名
- [x] releaseitem


<!--TAGS-->
<!--tag:Item-->
