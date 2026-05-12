## 描述
在生物与继承目标之间沿直线选取位置点


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 线段上各点之间的间距                          | 1       |
| fromorigin| fo        | 是否从嵌套技能的原点开始画线         | false   |


## 示例
```yaml
ExampleSkill1:
  Skills:
  - skill{s=ExampleSkill2} @Forward{f=10}

ExampleSkill2:
  Skills:
  - effect:particles @Line{r=0.5}
```
