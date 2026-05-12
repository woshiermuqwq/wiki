## 描述
Pick up the targeted item, if the caster is a player.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| fakelooting | fl      | Whether a fake looting animation 应当 played                    | true    |
| onpickup  | pickup, then | 要执行的[元技能] once the item is picked up             |<!--type:Metaskill-->|

### OnPickup Attribute
The called metaskill will have some of its linked data overriden/set to be the following
| Data     | Value  |
| -------- | ------ |
| Location | The position of the picked up item |
| Origin   | The position of the picked up item |
| Item     | The picked up item                 |


## 示例
```yaml
  Skills:
  - pickupitem @ItemsInRadius{r=10}
```


<!--TAGS-->
<!--tag:Item-->
<!--tag:World-->
<!--tag:Meta-Mechanic-->
