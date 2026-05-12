## 描述
检测目标玩家是否拥有某项权限。

## 属性

| 属性        | 别名   | 描述               | 默认值 |
| ----------- | ------ | ------------------ | ------ |
| permission  | p      | 要检测的权限节点     |        |


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
