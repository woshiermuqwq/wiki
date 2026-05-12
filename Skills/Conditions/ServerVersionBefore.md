## 描述
检查服务器版本是否在指定版本之前。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| version | v, sv | 要检查的版本 | 1.19.3 |
| inclusive | i | 条件是否应该检查当前版本是否恰好为指定版本 | true |


## 示例
```yaml
  Conditions:
  - serverBefore{version=1.21.1}
  Skills:
  - message{m="说真的，你们该更新了"} @world
```


## 别名
- [x] serverBefore
- [x] versionBefore