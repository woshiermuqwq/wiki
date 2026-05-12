## 描述
以nearest 玩家 in a 半径为目标。

## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径 | r | The 半径 of the 目标选择器 | 5 |


## 示例
```yaml
ExampleSkill:
  Skills:
  - settarget @NearestPlayer{r=10}
```