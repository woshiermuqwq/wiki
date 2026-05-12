## 描述
选取最后一个与施法者交互的实体，前提是施法者的 [Type](/Mobs/Mobs#type) 为 `INTERACTION`。


## 属性
> *此条件没有属性*


## 示例
以下示例每 100 刻点燃一次最后一个与施法者交互的实体
```yaml
ExampleInteractionEntity:
  Type: INTERACTION
  Skills:
  - ignite @interactionLastInteract ~onTimer:100
```


## 别名
- [x] lastInteract
