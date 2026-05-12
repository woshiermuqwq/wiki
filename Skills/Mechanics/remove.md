## 描述
移除目标实体 from existence. Does not work on players.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onRemoveSkill | onRemove, then | The Metaskill to execute once an entity is removed          |<!--type:Metaskill-->|


## 示例
This mob would despawn 10 seconds after spawning:
```yaml
  Skills:
  - remove{delay=200} @self ~onSpawn
```
This skill despawns the mob immediately when it is right clicked.
```yaml
  Skills:
  - remove @self ~onInteract
```


## 别名
- [x] delete


<!--TAGS-->
<!--tag:Meta-->
<!--tag:Meta-Mechanic:Thenable-->
