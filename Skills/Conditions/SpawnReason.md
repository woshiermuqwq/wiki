## 描述
检测目标的生成原因。

## 属性
| 属性       | 别名   | 描述                                       | 默认值              |
| ---------- | ------ | ------------------------------------------ | ------------------- |
| reason     | r      | 要检测的生成原因。可使用任何 [Bukkit][] 枚举值 |<!--type:SpawnReason--> |


## 示例
在此例中，如果目标生物是因掠夺者袭击事件生成的，则施加发光效果。
```yaml
ExampleSkill:
  TargetConditions:
  - spawnReason{reason=RAID} true
  Skills:
  - potion{t=GLOWING;d=100;l=0}
```


  [Bukkit]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html
