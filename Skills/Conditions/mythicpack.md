## 描述
检测服务器上是否存在指定 ID 的[包](/Packs)。

## 属性
| 属性       | 别名         | 描述               | 默认值 |
| ---------- | ------------ | ------------------ | ------ |
| packid     | pack, id, p  | 要检测的包的 ID     |        |


## 示例
```yaml
  Conditions:
  - mythicpack{p="ThePackId"} true
```

## 别名
- [x] pack
- [x] haspack
