基础飞行药水
--------------
* 一瓶带有附魔光泽的简单药水，饮用后给予饮用者 1 分钟的飞行能力。

关于"basicflypot"技能的使用方式，请参见[此处](/examples/Consumable-Skills#drink-flight-potion-skill)。

```yaml
basicflypot:
  Id: potion
  Display: '&f&l基础&6 药水 &b&l飞行&r'
  Options:
    Color: 89,255,230
  Lore:
  - '&9飞行 (1:00)'
  Enchantments:
  - MENDING
  Hide:
  - ENCHANTS
  Skills:
  - skill{s=basicflypot} ~onConsume
```
