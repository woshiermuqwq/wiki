## 描述
以施法者朝向为基准，在指定角度、长度和旋转的锥形区域内选取所有活体实体


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| angle     | a         | 锥形的角度                                                | 90      |
| range     | r         | 锥形的长度                                               | 16      |
| rotation  | rot       | 锥形的旋转角度                                             | 0       |
| usepitch  | pitch, p  | 锥形的生成是否也取决于施法者的俯仰角    | false   |
| yoffset   | yo        | 要添加到生成的锥形位置的 Y 轴偏移            | 0       |
| livingonly | lo       | 是否仅选取活体实体                               | true    |


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
