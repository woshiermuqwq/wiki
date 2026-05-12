## 描述
Ta以random points in a cone 在...前方 the 施法者为目标。
Note: Cone is fixed on the y-axis, and 不能 be rotated up or down


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 角度 | a | The 角度 of the cone | 90 |
| 范围 | r | The length of the cone | 16 |
| points | p | The number of points that 将 targeted 在...内 cone | 角度\*范围\*0.1|
| slices | s | This 定义 how many layers or subdivisions (slices) the cone is divided into along its length (范围).<br>More slices 结果 in a finer resolution | floor(`range`) |
| minpoints | mp | The minimum number of points to be generated for each slice | 1 |
| 旋转 | rot | The 旋转 of the cone | 0 |
| yoffset | yo, y | The y 偏移 of the cone | 0 |
|| exact | e | Whether to use a precise method to distribute points uniformly 跨过 cone surface 而不是 randomly generating them | false |


## 示例
```yaml
  Skills:
  - effect:particles @Cone{a=45;r=10;p=200}
```