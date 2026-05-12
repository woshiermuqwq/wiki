## 描述
检测目标是否拥有指定范围的光环层数。

## 属性

| 属性       | 别名                                                              | 描述                 | 默认值 |
| ---------- | ----------------------------------------------------------------- | -------------------- | ------ |
| aura       | auraname, b, buff, buffname, debuff, debuffname, n, name          | 要检测的光环名称      |        |
| stacks     | s                                                                 | 要检测的层数范围      | 1      |


## 示例
```yaml
  Conditions:
  - hasaurastacks{n=firedebuff;s=>3} true
```

## 别名
- [x] hasbuffstacks
- [x] hasdebuffstacks
- [x] aurastacks
- [x] buffstacks
- [x] debuffstacks
