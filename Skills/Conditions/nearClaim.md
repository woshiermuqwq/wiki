## 描述
检测目标位置是否在任何支持插件的领地附近。

支持的插件：
- GriefPrevention
- Lands
- CrashClaim

## 属性
| 属性       | 别名   | 描述               | 默认值 |
| ---------- | ------ | ------------------ | ------ |
| radius     | r      | 检测范围            | 16     |


## 示例
```yaml
  Conditions:
  - nearclaim{r=20} false
```

## 别名
- [x] nearClaims
