## 描述
检测[起点]是否在给定位置。

## 属性
| 属性       | 别名        | 描述                                           | 默认值 |
| ---------- | ----------- | ---------------------------------------------- | ------ |
| location   | loc, l, c   | 要匹配的位置，格式为 `x,y,z`                     |        |
| x          |             | 位置的 X 坐标。若设置了 location 属性则忽略此值   | 0      |
| y          |             | 位置的 Y 坐标。若设置了 location 属性则忽略此值   | 0      |
| z          |             | 位置的 Z 坐标。若设置了 location 属性则忽略此值   | 0      |
| exact      | e           | 是否精确匹配位置                                  | false  |


## 示例
```yaml
  Conditions:
  - originLocation{loc=10,20,30} true
```


<!-- LINKS -->
[起点]: /Skills/Targeters/Origin
