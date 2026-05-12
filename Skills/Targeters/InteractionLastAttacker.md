## 描述
选取最后一个攻击施法者的实体，前提是施法者的 [Type](/Mobs/Mobs#type) 为 `INTERACTION`。


## 属性
> *此条件没有属性*


## 示例
以下示例每 100 刻点燃一次最后一个攻击了施法者的实体
```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - ignite @interactionLastAttacker ~onTimer:100
```


## 别名
- [x] lastAttacker
