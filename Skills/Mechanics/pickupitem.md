## 描述
Pick up the targeted item, if the 施法者 is a player.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| fakelooting | fl      | 是否 a fake looting animation should be played                    | true    |
| onpickup  | pickup, then | The [metaskill] to 执行 once the item is picked up             |<!--type:Metaskill-->|

### OnPickup Attribute
The called metaskill will have some of its linked data overriden/set to be the following
| Data     | Value  |
| -------- | ------ |
| Location | The position of the picked up item |
| 原点   | The position of the picked up item |
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
