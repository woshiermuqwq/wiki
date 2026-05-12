## 描述
Adds an attribute modifier to the attributable target


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| attribute | attr      | The [attribute]                      | GENERIC_LUCK<!--type:PaperAttribute--> |
| operation | op        | The [operation] to perform                                        | ADD_NUMBER<!--type:PaperAttributeOperation--> |
| name      | modifierName | The name of the modifier                                    | <caster.uuid> |
| amount    | amt, a    | The modifier of the attribute                                          | 0     |
| duration  | dur       | The duration of the attribute                                          | 0     |


## 示例
```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attributeModifier{attribute=GENERIC_LUCK;a=2;dur=1200;op=ADD_NUMBER} @trigger ~onDeath
```

<!-- LINKS -->
[attribute]: https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html
[operation]: /Items/Attributes#operations


<!--TAGS-->
<!--tag:Attribute-->
