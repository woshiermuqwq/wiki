## 描述
Modifies an *already* applied disguise on the target entity.  
Like the [Disguise](/skills/mechanics/disguise) 技能, [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/) 必须 installed. [Here](/Mobs/Disguises) you can find our documentation on the matter.  
The syntax 对于disguise in this 技能 is completely equivalent to the one used in the `/modifydisguise` command.


## 属性

| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| disguise  | d, type   | The options to modify in the disguise                         | player Ashijin |


## 示例
This will set the displayed item in the disguises's main has as "air"
```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand air"} @self 
```

##
This will set the item displayed in the disguise's main hand as the real one
```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand %held-item%"} @self
```


## 别名
- [x] modifydisguise


<!--TAGS-->
<!--tag:Disguise-->
