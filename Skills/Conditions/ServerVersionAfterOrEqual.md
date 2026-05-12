## 描述
检测服务器版本是否在指定版本之后（或等于）。

## 属性
| 属性       | 别名      | 描述                                       | 默认值  |
| ---------- | --------- | ------------------------------------------ | ------- |
| version    | v, sv     | 要检测的版本                                | 1.19.3  |
| inclusive  | i         | 是否同时匹配等于指定版本的情况                | true    |


## 示例
```yaml
  Conditions:
  - serverAfter{version=1.21.1} false
  Skills:
  - message{m="讲真你们该更新了"} @world
```

## 别名
- [x] serverAfterEq
- [x] serverAfter
- [x] versionAfterEq
- [x] versionAfter
