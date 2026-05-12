## 描述
测试目标的实体类型是否为指定类型。  
有效的实体类型列表可在 [Spigot Javadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html) 中找到。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | types, t  | 要匹配的实体类型列表                                      |<!--type:EntityType--><!--list--> |


## 示例
```yaml
Conditions:
- entitytype{t=ZOMBIE} true
```

```yaml
TargetConditions:
- entitytype{t=WITCH} true
```

```yaml
TriggerConditions:
- entitytype{t=PLAYER} true
```

## 别名
- [x] mobtype