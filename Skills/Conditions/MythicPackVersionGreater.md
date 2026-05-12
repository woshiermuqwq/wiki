## 描述
检测服务器上是否存在指定 ID 的[包](/Packs)，且其版本大于或等于指定版本。

## 属性
| 属性         | 别名                | 描述               | 默认值 |
| ------------ | ------------------- | ------------------ | ------ |
| packid       | pack, id, p         | 要检测的包的 ID     |        |
| packversion  | packV, version, v   | 要检测的版本        |        |


## 示例
```yaml
  Conditions:
  - packversiongreater{p="ThePackId";v="1.2.3"} true
```

## 别名
- [x] packversiongreater
- [x] packversionisgreater
