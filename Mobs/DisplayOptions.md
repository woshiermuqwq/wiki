All available 显示 实体 选项. All of these 选项 go 在...下 `DisplayOptions` sections, like so:
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```
表 Of Contents:

[[_TOC_]]

# Base 选项
These 选项 are available for all 显示 实体 类型.

#### ViewRange
The maximum view 范围/距离. [When the 距离 is 多于 `viewRange x entityDistanceScaling x 64`, the 实体 不是 rendered](https://Minecraft.wiki/w/显示#Entity_data). Defaults to `1`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ViewRange: 1
```

#### 宽度
The 显示 宽度. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Width: 0
```

#### 高度
The 显示 高度. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Height: 0
```

#### ShadowRadius
The 显示 shadow 半径. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowRadius: 0
```

#### ShadowStrength
The opacity of the 显示 实体 shadow. Defaults to `1`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowStrength: 1
```

#### Billboard
Controls 该 显示 实体 pivots when rendered to the 玩家. Defaults to `FIXED`.\
Available constraints:

| Billboard | Description |
|------------|-----------------------------------|
| FIXED | No 旋转 |
| CENTER | Pivots 在...周围 center point |
| HORIZONTAL | Pivots 在...周围 horizontal axis |
| VERTICAL | Pivots 在...周围 vertical axis |

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Billboard: FIXED
```

#### TeleportDuration
Set the teleport 持续时间 in ticks. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    TeleportDuration: 0
```
#### InterpolationDelay
Set the delay 之前 starting interpolation. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDelay: 0
```

#### InterpolationDuration
Set the interpolation 持续时间 in ticks. Defaults to `0`.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDuration: 0
```

#### ColorOverride
Set the glow border color. If `0`, it uses the color of the team the 显示 team is in. Defaults to `0`.\
***Formats**: `a,r,g,b` or an 整数 equivalent.
HHere are sites that 您可以 use: [color-hex](https://www.color-hex.com/), [arg-int-calculator](https://argb-int-calculator.netlify.app/)
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ColorOverride: 0
```

### Brightness
BBoth blocklight and skylight 必须为 set to 覆盖 brightness. 值 必须为 in 范围 of `0` to `15`.
 
Use a 值 of `-1` to make it so the 显示 实体 uses the ambiens blocklight/skylight 没有 overriding them

#### BlockLight & SkyLight
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    BlockLight: 0
    SkyLight: 0
```

### Transformations
#### Translation
Set the 显示 实体 translation. Defaults to `0,0,0`.
**格式**: x,y,z
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Translation: 0,0,0
```

#### Scale
Set the scale of the 显示 实体. Scales the model centered on the 原点. Defaults to `1,1,1`.
**格式**: x,y,z
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Scale: 1,1,1
```

#### LeftRotation
SeSet the left 旋转 using [quaternions](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation) if 4 值 are provided (x,y,z,w).
UsUses euler if 3 are provided (x,y,z).
DeDefaults to `0,0,0,1` (no 旋转).
**格式**: x,y,z,w
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    LeftRotation: 0,0,0,1
```

#### RightRotation
SeSet the left 旋转 using [quaternions](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation) if 4 值 are provided (x,y,z,w).
UsUses eular if 3 are provided (x,y,z).
DeDefaults to `0,0,0,1` (no 旋转).
**格式**: x,y,z,w
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    RightRotation: 0,0,0,1
```

# 方块 显示
This 显示 类型 仅 has one special 选项.
#### 方块
The 方块 state to use.
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: bell[facing=north]
```

# 物品 显示

#### 物品
The 物品 to use.支持mythic 物品。
```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
```

#### Transform
The model transform applied to the 物品. Defaults to `NONE`.

| 类型 |
|:-----------------------:|
| FIRSTPERSON_LEFTHAND |
| FIRSTPERSON_RIGHTHAND |
| FIXED |
| GROUND |
| GUI |
| HEAD |
| 无 |
| THIRDPERSON_LEFTHAND |
| THIRDPERSON_RIGHTHAND |

```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
    Transform: NONE
```

# Text 显示
#### Text
Set the text to show. Defaults to `Give This Poor Dude A Text To Display`.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
```

#### Opacity
Set the text opacity, ranging from `0` to `255`. Defaults to `255`.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Opacity: 255
```

#### DefaultBackground
Set 是否 to render using the 默认 text background color (same as in chat),
overriding the [BackgroundColor](#BackgroundColor) 选项.
Defaults to `false`.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    DefaultBackground: false
```

#### BackgroundColor
Set the text background color.
Defaults to `1073741824`.\
**Formats**: `a,r,g,b` or an 整数 equivalent.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    BackgroundColor: 1073741824
```

#### Alignment
Set the text alignment. Defaults to `CENTER`.

| 类型 | Description |
|:------:|---------------------|
| CENTER | Center aligned text |
| LEFT | Left aligned text |
| RIGHT | Right aligned text |

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Alignment: CENTER
```

#### LineWidth
The maximum line 宽度 used to split lines. Can 也 use `\n` characters to split to 另一个 line. Defaults to `200`.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    LineWidth: 200
```

#### Shadowed
Set 是否 the text 应为 displayed with a shadow. Defaults to `false`.
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Shadowed: false
```

#### SeeThrough
Set 是否 the text 应为 visible 通过 方块. Defaults to `false`
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    SeeThrough: false
```