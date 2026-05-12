## 描述
Sets the item component of Item Display entities


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| item      | i, type, t, material, mat, m | The item to use. If not set, the 技能 will remove the item from the entity instead | AIR<!--type:Item--> |


## 示例
```yaml
ExampleMob:
  Type: ITEM_DISPLAY
  Skills:
  - setDisplayEntityItem{i=MyMythicItem} @self ~onSpawn
```


<!--TAGS-->
<!--tag:Item-->
