## 描述
以all living 实体 in the 施法者 世界为目标。


## 属性
>*This 目标选择器 has no 属性*


## 示例
```yaml
EntityCount:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @LivingInWorld
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```


## 别名
- [x] EIW
- [x] allinworld
- [x] livingentitiesinworld
- [x] entitiesinworld