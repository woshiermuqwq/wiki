## 描述
使生物flee 从 sun and hide in shade。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 速度 | s | The 速度 at which to move towards shade | 1 |

## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  AIGoalSelectors:
    - clear
    - fleesun{s=2}
```