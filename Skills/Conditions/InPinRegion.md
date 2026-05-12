## 描述
检测目标位置是否在由两个[标记点]界定的区域内。

## 属性
| 属性       | 别名   | 描述               | 默认值          |
| ---------- | ------ | ------------------ | --------------- |
| pin1       | p1     | 第一个[标记点]      |<!--type:Pin-->  |
| pin2       | p2     | 第二个[标记点]      |<!--type:Pin-->  |


## 示例
```yaml
  TargetConditions:
  - inpinregion{p1=mypin;p2=anotherpin}
```


<!-- LINKS -->
[标记点]: /Pins
