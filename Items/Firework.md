This 属性 用于 修改 the firework 效果 of a firework or firework_charge 物品.
This 属性 is 必需 for every firework or firework_charge 物品.

### 格式
```yml
ItemName:
  Id: material
  Firework:
    Colors:
    FadeColors:
    Flicker:
    Trail:
```

Breaking Down The Firework Configuration
---------------------------------------

### 颜色
primary colors to be added to the firework 效果. The colors 必须为 using RGB(red,green,blue) 格式的列表。
```yml
# adds red(255,0,0), green(0,255,0), and blue(0,0,255) colors
# to the firework effect
example_item:
  Id: firework_charge
  Firework:
    Colors:
      - 255,0,0
      - 0,255,0
      - 0,0,255
```
### FadeColors
Similar to the [colors](/物品/Firework#Colors) 选项 but 添加 the colors to the fade 效果 instead.
```yml
example_item:
  Id: firework_charge
  Firework:
    Colors:
      - 255,0,0
      - 0,255,0
      - 0,0,255
    FadeColors:
      - 255,0,255
      - 0,255,0
```
### Flicker
Whether the firework 效果 flickers
```yml
example_item:
  Id: firework_charge
  Firework:
    Flicker: true
```
### Trail
Whether the firework 效果 has a trail
```yml
example_item:
  Id: firework_charge
  Firework:
    Trail: true
```