## 描述
检查目标生物是否继承自指定的[模板](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Mobs/Templates)。


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| templates | template, t | 要匹配的模板。可以指定模板列表，这种情况下只要匹配到列表中任意一个模板，条件即通过                              |         |


## 示例
```yaml
  Conditions:
  - templatetype{template=NetherMob,EndMob}
```


## 别名
- [x] template
- [x] instanceOf