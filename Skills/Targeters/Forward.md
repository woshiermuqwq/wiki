## 描述
以a 位置 在...前方 the 施法者为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| forward | f, 数量, a | How distant should the targeted point be | 5 |
| rotate | rot | The 旋转, 在...周围 施法者, of the 目标 位置 | 0 |
| useeyelocation | uel | If the eye 位置 应为 used as the base of the 目标选择器 | false |
| lockpitch | | If the 位置 应为 targeted as if the 施法者 has a pitch of 0 | false |


## 示例
```yaml
ExampleSkill:
  Skills:
  - effect:particles @Forward{f=3;uel=true;rot=10}
```