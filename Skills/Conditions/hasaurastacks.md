## 描述
测试目标光环的叠加层数是否在给定范围内。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| aura      | auraname, b, buff, buffname, debuff, debuffname, n, name | 要检查的光环名称 
| stacks    | s         | 要检查的叠加层数/范围                              | 1       |


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