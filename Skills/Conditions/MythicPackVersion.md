## 描述
检查指定 ID 的 [Pack](/Packs) 是否在服务器上存在且版本为指定版本。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| packid    | pack, id, p | 要检查的 Pack ID                                           |         |
| packversion | packV, version, v | 要检查的版本                                   |         |


## 示例
```yaml
  Conditions:
  - packversion{p="ThePackId",v="1.2.3"} true
```


## 别名
- [x] packversion
- [x] packversionis