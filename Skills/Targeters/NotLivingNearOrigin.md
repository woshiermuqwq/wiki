## 描述
以all non living 实体 in a 半径 near the 原点为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |


## 示例
This 机制 will say in the global chat the UUID of every non living 实体 in a 10 方块 半径 from 自身 一旦 it ends
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - command{c="say <target.uuid>"} @NotLivingNearOrigin{r=10}
    ]}
```

## 别名
- [x] nonLivingNearOrigin
- [x] NLNO