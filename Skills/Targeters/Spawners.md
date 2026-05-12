## 描述
选取指定生物刷怪器的位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| spawners  | spawner, s| 刷怪器名称。可以是简单名称、组名（`g:groupname`）或包含通配符（`Spawner*` 可匹配 *Spawner1*、*Spawner2*、*Spawner3*……）                |         |


## 示例
```yaml
ExampleSkill_SingleSpawner:
  Skills:
  - effect:particles @Spawner{s=TestSpawner}
```
```yaml
ExampleSkill_Group:
  Skills:
  - effect:particles @Spawner{s=g:ExampleSpawnerGroup}
```
```yaml
ExampleSkill_WildCard:
  Skills:
  - effect:particles @Spawner{s=ForestSpawner_*}
```
