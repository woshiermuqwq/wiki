## 描述
以位置 of the specified 生物 生成器为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 生成器 | 生成器, s| The 名称 of the 生成器. Can be 也 a simple 名称, a group (`g:groupname`) or contain wildcards (`Spawner*` to 目标 *Spawner1*,*Spawner2*,*Spawner3*...) | |


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