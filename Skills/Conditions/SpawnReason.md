## 描述
检查目标的生成原因。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| reason    | r         | 要检查的原因。可以是任何 [Bukkit][] 的生成原因             |<!--type:SpawnReason--> |


## 示例
在此示例中，如果目标实体是因为袭击而生成的，技能将对其应用发光效果。
```yaml
ExampleSkill:
  TargetConditions:
  - spawnReason{reason=RAID} true
  Skills:
  - potion{t=GLOWING;d=100;l=0}
```


  [Bukkit]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html