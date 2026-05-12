## 描述
检测目标是否处于某个维度中。
有效维度列表可在 [Spigot Environment 文档](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/World.Environment.html) 中找到。

## 属性

| 属性       | 别名                  | 描述               | 默认值    |
| ---------- | --------------------- | ------------------ | --------- |
| dimension  | d, environment, env   | 要检测的维度列表    | THE_END<!--type:WorldEnviroment--><!--list--> |


## 示例
```yaml
  Conditions:
  - dimension{d=NORMAL} true
```

## 别名
- [x] environment
