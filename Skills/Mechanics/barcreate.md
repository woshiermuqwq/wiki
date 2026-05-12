## 描述
Creates a custom boss bar on the casting 生物 (cannot be player).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | The name of the bossbar.                                             | infobar |
| display   | d, bartimerdisplay, bartimertext | The text displayed on the bar            | <施法者.name> |
| value     | v         | How filled the bossbar is. Must be between 0.0 and 1.0.              | 1.0     |
| color     | c, bartimercolor | The [Color](/生物/BossBar#color) of the bossbar               | RED<!--type:BarColor--> |
| style     | s, bartimerstyle | The [Style](/生物/BossBar#style) of the bossbar               | SOLID<!--type:BarStyle--> |

  

## 示例
```yaml
  Skills:
  - barCreate{
    name="MyBossBar";
    display="<caster.name> - <caster.hp>";
    value=1.0;color=BLUE;
    style=SEGMENTED_6
    } @self ~onSpawn
```


## 别名
- [x] barAdd
- [x] createBar


<!--TAGS-->
<!--tag:BossBar-->