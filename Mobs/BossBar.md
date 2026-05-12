Boss血条功能用于给你的自定义生物添加生命条，样式与末影龙和凋灵使用的相同，但提供了更多的自定义选项。

## 语法

```yaml
internal_mobname:
  Type: <mobtype>
  BossBar:
    Enabled: [true/false]
    Title: '[name]'
    Range: [range]
    Color: [color]
    Style: [style]
    CreateFog: [true/false]
    DarkenSky: [true/false]
    PlayMusic: [true/false]
```

### 颜色
Color 的可用颜色（区分大小写）：PINK, BLUE, RED, GREEN, YELLOW, PURPLE, WHITE。

### 样式
Style 的可用样式（区分大小写）：SOLID, SEGMENTED_6, SEGMENTED_10, SEGMENTED_12, SEGMENTED_20。

### 范围
范围是 Boss血条 向生物周围的玩家显示的距离。

### 额外选项
CreateFog 在 Boss血条 定义的半径范围内为玩家视野添加雾状效果。

DarkenSky 在 Boss血条 定义的半径范围内使天空变暗，类似于凋灵生成时产生的效果。

<!--
我不太确定 PlayMusic 的作用，但我推测它会在 Boss血条 定义的半径范围内播放 Boss 音乐。
-->

## 示例
```yaml
SuperCreeper:
  Type: creeper
  Display: '&cTest'
  Health: 20
  BossBar:
    Enabled: true
    Title: 'Test'
    Range: 20
    Color: RED
    Style: SOLID
```
