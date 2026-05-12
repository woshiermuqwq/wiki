## 描述
Stops the targeted living entity from using an item, i.e. blocking with a shield.
> If you want to do some sort of cooldown, try using this 技能 in an aura


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
