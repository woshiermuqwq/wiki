## 描述
检测目标生物是否拥有指定的光环。

## 属性

| 属性       | 别名                                                              | 描述                 |
| ---------- | ----------------------------------------------------------------- | -------------------- |
| aura       | auraname, b, buff, buffname, debuff, debuffname, n, name          | 要检测的光环名称      |


## 示例
```yaml
  Conditions:
  - hasaura{aura=firedebuff} true
```

## 别名
- [x] hasbuff
- [x] hasdebuff
