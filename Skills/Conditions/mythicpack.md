## 描述
检查指定 ID 的 [Pack](/Packs) 是否在服务器上存在。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| packid    | pack, id, p | 要检查的 Pack ID                                           |         |


## 示例
```yaml
  Conditions:
  - mythicpack{p="ThePackId"} true
```


## 别名
- [x] pack
- [x] haspack