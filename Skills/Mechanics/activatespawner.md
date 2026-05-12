## 描述
Activates a MythicMobs [spawner](Spawners), causing it to spawn 生物. Will not
override any 条件 or options set on the spawner.

>Best used in conjunction with setting the `useTimer` attribute on
spawners to `false`.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spawners  | spawner, s| The name of the spawner(s) to activate. This can accept groups and wildcards also using the appropriate syntax                                                              | NONE    |


## 示例
This would activate the spawner named "BossAdd"
```yaml
    Skills:
    - activatespawner{spawner=BossAdd}
```
##
此示例将activate all spawners in the group "Castle"
```yaml
    Skills:
    - activatespawner{spawner=g:Castle}
```
##
此示例将activate all spawners starting with
"DungeonBoss1Spawner" (i.e. DungeonBoss1Spawner1, DungeonBoss1Spawner2,
etc)
```yaml
    Skills:
    - activatespawner{spawner=DungeonBoss1Spawner*}
    - ...
```


## 别名
- [x] as