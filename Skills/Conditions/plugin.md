## 描述
检查指定插件是否在服务器上运行。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| plugin    | pl, p     | 要检查的插件                                           | MythicMobs |


## 示例
```yml
  Conditions:
  - plugin{p=ThePluginName} true
```


## 别名
- [x] pluginexists
- [x] hasplugin