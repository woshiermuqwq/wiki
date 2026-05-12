## 描述
Ex执行 the 技能 when the cow is milked or when an 实体 is stored in a bucket (axolotl and the 其他 bucketable ones).
> The associated [@触发器](/技能/目标选择器/触发器) is the 施法者 自身


## 示例
```yaml
ANormalCow:
  Type: Cow
  Skills:
  - skill{s=[
    - message{m="HOW DARE YOU?!?"} @trigger
    - sound{s=entity.creeper.primed}
    - explosion{yield=5;delay=30}
    ];cd=2} @self ~onBucket
```


## 别名
- [x] onUseBucket
- [x] onFillBucket
- [x] onBucketFill
- [x] onMilk
- [x] onMilked