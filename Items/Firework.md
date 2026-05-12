此属性用于修改烟花火箭或烟花之星物品的烟花效果。
每个烟花火箭或烟花之星物品都必须包含此属性。

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

拆解烟花配置
---------------------------------------

### Colors（主颜色）
要添加到烟花效果中的主颜色列表。颜色必须使用 RGB（红,绿,蓝）格式。
```yml
# 为烟花效果添加红色(255,0,0)、绿色(0,255,0)和蓝色(0,0,255)
example_item:
  Id: firework_charge
  Firework:
    Colors:
      - 255,0,0
      - 0,255,0
      - 0,0,255
```
### FadeColors（渐隐颜色）
与[主颜色](/Items/Firework#Colors)选项类似，但作用于渐隐效果。
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
### Flicker（闪烁）
烟花效果是否闪烁。
```yml
example_item:
  Id: firework_charge
  Firework:
    Flicker: true
```
### Trail（拖尾）
烟花效果是否带有拖尾轨迹。
```yml
example_item:
  Id: firework_charge
  Firework:
    Trail: true
```