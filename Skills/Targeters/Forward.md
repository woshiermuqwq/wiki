## 描述
选取施法者面前的一个位置


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| forward   | f, amount, a | 目标点距离施法者多远                          | 5       |
| rotate    | rot       | 目标位置绕施法者的旋转角度              | 0       |
| useeyelocation | uel  | 是否使用眼睛位置作为目标选择器的基点       | false   |
| lockpitch |           | 是否以施法者俯仰角为 0 来计算目标位置 | false   |


## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @Forward{f=3;uel=true;rot=10}
```
