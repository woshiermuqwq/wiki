## 描述
检测目标生物是否继承（扩展）了指定的[模板](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Templates)。

## 属性
| 属性       | 别名         | 描述                                                             | 默认值 |
| ---------- | ------------ | ---------------------------------------------------------------- | ------ |
| templates  | template, t  | 要匹配的模板。可以指定多个模板，此时只要匹配任一模板即通过          |        |


## 示例
```yaml
  Conditions:
  - templatetype{template=NetherMob,EndMob}
```

## 别名
- [x] template
- [x] instanceOf
