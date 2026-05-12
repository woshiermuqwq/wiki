## 描述
使生物be able to breed with 其他 生物。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| speedmodifier | 速度,s | The 速度 at which to move 朝向 partner | 1 |


## 示例
```yaml
ExampleMob:
  Type: COW
  AIGoalSelectors:
    - clear
    - breed{s=2}
```