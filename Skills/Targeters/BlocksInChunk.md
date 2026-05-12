## 描述
选取继承目标所在区块内的所有方块

## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| noair     | na        | 是否不选取空气方块                                   | true    |
| onlyair   | oa        | 是否仅选取空气方块                                  | false   |
| nearorigin| no        | 是否同时选取原点                   | false   |


## 示例
以下嵌套技能将选取技能树触发器所在区块内的所有非空气方块
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @trigger

ExampleSkill2:
  Skills:
  - effect:particles @BlocksInChunk
```


## 别名
- [x] BIC
