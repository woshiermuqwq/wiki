## 描述
以all living 实体 in cone with a specified 角度, length and 旋转 relative to facing 方向为目标。


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 角度 | a | The 角度 of the cone | 90 |
| 范围 | r | The length of the cone | 16 |
| 旋转 | rot | The 旋转 of the cone | 0 |
| usepitch | pitch, p | Whether to generate the cone 也 取决于 the 施法者 pitch | false |
| yoffset | yo | The y 偏移 to be added to the generated cone 位置 | 0 |
| living仅 | lo | Whether to 目标 仅 living 实体 | true |


## 示例
```yaml
ExampleSkill:
  Skills:
  - ignite @LivingInCone{a=45;r=20}
```


## 别名
- [x] entitiesInCone
- [x] livingEntitiesInCone
- [x] LEIC
- [x] EIC