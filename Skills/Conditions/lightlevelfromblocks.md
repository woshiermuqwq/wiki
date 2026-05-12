## 描述
检测目标位置处来自发光方块的亮度等级。

## 属性
| 属性       | 别名   | 描述               | 默认值 |
| ---------- | ------ | ------------------ | ------ |
| level      | l      | 要匹配的亮度范围     | 0      |


## 示例
```yaml
  Conditions:
  - lightlevelfromblocks{l=10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=>10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=1to10} true
```

## 别名
- [x] blocklightlevel
