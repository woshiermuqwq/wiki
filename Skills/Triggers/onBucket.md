## 描述
牛被挤奶或将实体装入桶时执行技能（如美西螈及其他可装桶生物）。  
> 关联的 [@trigger](/Skills/Targeters/Trigger) 为施法者自身


## 示例
```yaml
ANormalCow:
  Type: Cow
  Skills:
  - skill{s=[
    - message{m="大胆！"} @trigger
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
