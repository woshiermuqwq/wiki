## 描述
此条件检查目标玩家是否拥有某个权限。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| permission| p         | 要检查的权限。                                         |         |


## 示例

```yaml
  Conditions:
  - haspermission{p=permission.node.here} true
```
```yaml
  TargetConditions:
  - haspermission{p=permission.node.here} true
```
```yaml
  TriggerConditions:
  - haspermission{p=permission.node.here} true
```


## 别名
- [x] permission