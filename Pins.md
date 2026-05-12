现在每个[包]都允许包含 `pins.yml` 文件。该文件可以包含一个位置列表，MythicMobs 会以特殊方式处理它们：这些位置将被视为"标点"，使它们能更容易地被定位或检查。


## 指令
| 指令 | 权限 | 描述 |
| ------- | ---------- | ----------- |
| `/mm pins create [包] [名称]` | mythicmobs.command.pins | 将你当前的位置保存为 `[包]` 包中的一个名为 `[名称]` 的标点 |
| `/mm pins list` | mythicmobs.command.pins.list | 列出所有活跃的标点 |
| `/mm pins move [名称]` | mythicmobs.command.pins | 将名为 `[名称]` 的标点移动到当前位置 |
| `/mm pins remove [包] [名称]` | mythicmobs.command.pins | 从 `[包]` 包中移除名为 `[名称]` 的标点 |
| `/mm pins toggleviewing` | mythicmobs.command.pins | 通过文本显示实体展示每个标点的位置 |
| `/mm pins wand [包] [标点名]` | mythicmobs.command.pins | 手持标点魔杖时，左键单击创建多点标点并指向它，右键单击从多点标点中移除最近的点 |


## 机制
- [MovePin](/Skills/Mechanics/MovePin)

## 目标选择器
- [@Pin](/Skills/Targeters/Pin)
- [@BlocksInPinRegion](/Skills/Targeters/BlocksInPinRegion)


## 条件
- [DistanceFromPin](/skills/conditions/DistanceFromPin)
- [inPinRegion](/Skills/Conditions/InPinRegion)
- [OriginDistanceFromPin](/Skills/Conditions/OriginDistanceFromPin)

<!-- LINKS -->
[包]: Packs
