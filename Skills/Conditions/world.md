## 描述
检查目标世界的名称。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| world     | w         | 要检查的世界列表                        | tutorial_world |


## 示例
```yaml
  Conditions:
  - world{w=tutorial_world} true
```
```yaml
  Conditions:
  - world{w=world1,world2} true
```