## 描述
Undoes a previous paste done via the [fawePaste] 技能, based on its id or on the schematic used


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| pasteID   | pid, id   | The id of the paste that needs to be undone                          |         |
> This 技能 inherits every *inheritable* attribute of the [Aura](/Skills/Mechanics/Aura) 技能


## 示例
```yaml
ExampleMob:
  Skills:

  # With ID
  - fawePaste{s=cgym.schem;id=abc} @self ~onSpawn
  - undoPaste{id=abc} @self ~onDamaged

  # Without ID
  - fawePaste{s=lab.schem} @self ~onSpawn
  - undoPaste{id=lab.schem} @self ~onDamaged
```


## 别名
- [x] undoschem
- [x] undoschematic


<!-- LINKS -->
[fawePaste]: /skills/mechanics/fawepaste/


<!--TAGS-->
<!--tag:World-->
