## 描述
检测目标实体是否为施法者的主人。

- 如果施法者是可驯服生物，则检查目标实体是否为该生物的「原版」主人
- 如果施法者不是可驯服生物，则目标实体必须通过 [SetOwner](/skills/mechanics/setowner) 技能被设置为主人才能匹配


## 属性
> *此条件没有属性*

## 示例：
```yaml
  TargetConditions:
  - owner true
```

## 别名
- [x] isOwner
