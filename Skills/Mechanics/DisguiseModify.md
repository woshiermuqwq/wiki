## 描述
Modifies an *already* applied 伪装 on the 目标 entity.  
Like the [伪装](/skills/技能/伪装) 技能, [LibsDisguises](https://www.spigotmc.org/resources/libs-伪装-free.81/) must be installed. [Here](/生物/伪装) you can find our documentation on the matter.  
The syntax for the 伪装 in this 技能 is completely equivalent to the one used in the `/modifydisguise` command.


## 属性

| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 伪装  | d, type   | The options to modify in the 伪装                         | player Ashijin |


## 示例
This will set the displayed item in the 伪装's main has as "air"
```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand air"} @self 
```

##
This will set the item displayed in the 伪装's main hand as the real one
```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand %held-item%"} @self
```


## 别名
- [x] modifydisguise


<!--TAGS-->
<!--tag:Disguise-->