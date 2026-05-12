## 描述
以last 实体 that attacked the 施法者, if the 施法者 is of the `INTERACTION` [类型](/生物/生物#类型)为目标。


## 属性
> *This 条件 has no 属性*


## 示例
The following 示例 would ignite the last 实体 that attacked the 施法者 一旦 every 100 ticks
```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - ignite @interactionLastAttacker ~onTimer:100
```


## 别名
- [x] lastAttacker