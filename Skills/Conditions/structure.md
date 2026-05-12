## 描述
检测目标位置是否位于某个结构内部。支持通配符和来自数据包的结构。

## 属性

| 属性       | 别名            | 描述                   | 默认值  |
| ---------- | --------------- | ---------------------- | ------- |
| structure  | structures, s   | 要检测的结构。可为列表  | village |


## 示例
```yml
  Conditions:
  - structure{s=minecraft:desert_pyramid} true
```
