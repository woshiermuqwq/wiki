## 描述
检查目标是否在某个维度内。  
有效的维度列表可在 [Spigot Environment javadoc](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/World.Environment.html) 中找到。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| dimension | d, environment, env | 要检查的维度列表                              | THE_END<!--type:WorldEnviroment--><!--list--> |


## 示例
```yaml
  Conditions:
  - dimension{d=NORMAL} true
```


## 别名
- [x] environment