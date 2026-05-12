## 描述
Modifies a custom boss bar on the casting mob (cannot be player).


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| name      | n         | The name of the bossbar to modify/set                                | infobar |
| display   | d, bartimerdisplay, bartimertext | The text displayed on the bar           | <caster.name> |
| value     | v         | How filled the bossbar is. Must be between 0.0 and 1.0.              | 1.0     |
| color     | c, bartimercolor | Boss 血条的[颜色]               | RED<!--type:BarColor--> |
| style     | s, bartimerstyle | Boss 血条的[样式]               | SOLID<!--type:BarStyle--> |


## 示例
```yaml
  Skills:
  - barSet{
    name="MyBossBar";
    display="<caster.name> - <caster.hp>";
    value=1.0;
    color=RED;
    style=SEGMENTED_6
    } @self ~onDamaged
```


<!--TAGS-->
<!--tag:BossBar-->
