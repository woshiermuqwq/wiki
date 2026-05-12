## 描述
选取世界中的指定坐标


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| location  | loc, l, c | 完整坐标，格式为 `x,y,z,yaw,pitch`                   |         |
| x         |           | 若未设置 `location`，则为目标位置的 X 坐标 | 0     |
| y         |           | 若未设置 `location`，则为目标位置的 Y 坐标 | 0     |
| z         |           | 若未设置 `location`，则为目标位置的 Z 坐标 | 0     |
| yaw       |           | 若未设置 `location`，则为目标位置的偏航角         | 0      |
| pitch     |           | 若未设置 `location`，则为目标位置的俯仰角       | 0      |
| world     | w         | 目标所在的世界。若不设置，则使用施法者所在的世界    |        |


## 示例
```yaml
ExampleSkill:
  Skills:
  - setblock{m=DIAMOND_BLOCK} @Location{location=100,70,-120,0,0}
  - setblock{m=EMERALD_BLOCK} @Location{x=100;y=71;z=-120}
```


## 别名
- [x] l
- [x] loc
