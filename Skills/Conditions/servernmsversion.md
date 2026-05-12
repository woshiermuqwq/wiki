## 描述
检测服务器是否运行特定的 Minecraft NMS 版本。

## 属性
| 属性       | 别名      | 描述               | 默认值       |
| ---------- | --------- | ------------------ | ------------ |
| version    | sv, v     | 要检测的版本        | v1_19_R1_2   |


## 示例
```yaml
  Conditions:
  - nmsversion{v="v1_19_R1"}
```

## 别名
- [x] servernms
- [x] nmsversion
