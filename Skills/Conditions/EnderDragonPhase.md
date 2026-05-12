## 描述
检测目标末影龙的当前阶段。
有效阶段列表可在 [Spigot Phase 文档](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EnderDragon.Phase.html) 中找到。

## 属性

| 属性       | 别名   | 描述                 | 默认值 |
| ---------- | ------ | -------------------- | ------ |
| phase      | p      | 要匹配的阶段列表      |        |


## 示例
```yaml
  Conditions:
  - enderdragonphase{phase=CIRCLING} true
```
```yaml
Conditions:
- enderdragonphase{phases=FLY_TO_PORTAL,LEAVE_PORTAL} true
```

## 别名
- [x] edragonPhase
