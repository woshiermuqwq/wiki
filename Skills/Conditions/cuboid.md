## 描述
检查目标是否在由 `location1` 和 `location2` 作为对角顶点的长方体内。


## 属性

| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| location1 | loc1, l1, a | 第一个点的 x,y,z 坐标。                               |         |
| location2 | loc2, l2, b | 第二个点的 x,y,z 坐标。                               |         |
| relative  | r           | 坐标是否相对于施法者    | false   |


## 示例
```yaml
  TargetConditions:
  - cuboid{location1=x,y,z;location2=x,y,z;relative=true}
```


## 别名
- [x] incuboid