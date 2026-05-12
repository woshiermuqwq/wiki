所有可用的展示实体选项。这些选项均放在 `DisplayOptions` 区块下，示例如下：
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
```
目录：

[[_TOC_]]

# 基础选项
以下选项适用于所有展示实体类型。

#### ViewRange
最大可视范围/距离。[当距离超过 `viewRange × entityDistanceScaling × 64` 时，实体将不再渲染](https://minecraft.wiki/w/Display#Entity_data)。默认为 `1`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ViewRange: 1
```

#### Width
展示实体的宽度。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Width: 0
```

#### Height
展示实体的高度。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Height: 0
```

#### ShadowRadius
展示实体阴影的半径。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowRadius: 0
```

#### ShadowStrength
展示实体阴影的不透明度。默认为 `1`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ShadowStrength: 1
```

#### Billboard
控制展示实体面向玩家渲染时的旋转基准点。默认为 `FIXED`。
可选约束：

| Billboard   | 说明                 |
|------------|----------------------|
| FIXED      | 不旋转                |
| CENTER     | 围绕中心点旋转          |
| HORIZONTAL | 围绕水平轴旋转          |
| VERTICAL   | 围绕垂直轴旋转          |

```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Billboard: FIXED
```

#### TeleportDuration
设置传送过渡时长（刻）。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    TeleportDuration: 0
```

#### InterpolationDelay
设置插值开始前的延迟。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDelay: 0
```

#### InterpolationDuration
设置插值过渡时长（刻）。默认为 `0`。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    InterpolationDuration: 0
```

#### ColorOverride
设置发光边框颜色。设为 `0` 时，使用展示实体所在队伍的颜色。默认为 `0`。
**格式**：`a,r,g,b` 或等效整数值。
可参考以下网站：[color-hex](https://www.color-hex.com/)、[arg-int-calculator](https://argb-int-calculator.netlify.app/)
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    ColorOverride: 0
```

### 亮度
方块光照和天空光照必须同时设置才能覆盖亮度。取值范围为 `0` 到 `15`。

使用 `-1` 表示不覆盖，使展示实体使用环境中的方块光照/天空光照。

#### BlockLight 和 SkyLight
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    BlockLight: 0
    SkyLight: 0
```

### 变换
#### Translation
设置展示实体的偏移。默认为 `0,0,0`。
**格式**：x,y,z
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Translation: 0,0,0
```

#### Scale
设置展示实体的缩放比例。以原点为中心缩放模型。默认为 `1,1,1`。
**格式**：x,y,z
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    Scale: 1,1,1
```

#### LeftRotation
使用[四元数](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)设置左乘旋转（提供 4 个值 x,y,z,w 时）。
提供 3 个值（x,y,z）时使用欧拉角。
默认为 `0,0,0,1`（无旋转）。
**格式**：x,y,z,w
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    LeftRotation: 0,0,0,1
```

#### RightRotation
使用[四元数](https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation)设置右乘旋转（提供 4 个值 x,y,z,w 时）。
提供 3 个值（x,y,z）时使用欧拉角。
默认为 `0,0,0,1`（无旋转）。
**格式**：x,y,z,w
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: grass_block
    RightRotation: 0,0,0,1
```

# 方块展示
此展示类型只有一个特殊选项。

#### Block
要使用的方块状态。
```yml
cool_display:
  Type: block_display
  DisplayOptions:
    Block: bell[facing=north]
```

# 物品展示

#### Item
要使用的物品。支持 Mythic 物品。
```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
```

#### Transform
应用于物品的模型变换。默认为 `NONE`。

|            类型            |
|:-------------------------:|
|  FIRSTPERSON_LEFTHAND     |
|  FIRSTPERSON_RIGHTHAND    |
|          FIXED            |
|         GROUND            |
|           GUI             |
|          HEAD             |
|          NONE             |
|  THIRDPERSON_LEFTHAND     |
|  THIRDPERSON_RIGHTHAND    |

```yml
cool_display:
  Type: item_display
  DisplayOptions:
    Item: stick
    Transform: NONE
```

# 文本展示
#### Text
设置要显示的文本。默认为 `Give This Poor Dude A Text To Display`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
```

#### Opacity
设置文本不透明度，取值范围 `0` 到 `255`。默认为 `255`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Opacity: 255
```

#### DefaultBackground
设置是否使用默认文本背景色渲染（与聊天框中相同），此选项会覆盖 [BackgroundColor](#BackgroundColor) 选项。
默认为 `false`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    DefaultBackground: false
```

#### BackgroundColor
设置文本背景色。
默认为 `1073741824`。
**格式**：`a,r,g,b` 或等效整数值。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    BackgroundColor: 1073741824
```

#### Alignment
设置文本对齐方式。默认为 `CENTER`。

|  类型  | 说明       |
|:-----:|------------|
| CENTER | 居中对齐文本 |
|  LEFT  | 左对齐文本   |
| RIGHT  | 右对齐文本   |

```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Alignment: CENTER
```

#### LineWidth
用于分割行的最大行宽。也可以使用 `\n` 字符来换行。默认为 `200`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    LineWidth: 200
```

#### Shadowed
设置文本是否显示阴影。默认为 `false`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    Shadowed: false
```

#### SeeThrough
设置文本是否可以透视方块显示。默认为 `false`。
```yml
cool_display:
  Type: text_display
  DisplayOptions:
    Text: Give This Poor Dude A Text To Display
    SeeThrough: false
```
