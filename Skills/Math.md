让你可以执行简单或高级的计算。任何返回数字的占位符均受支持。你可以在大多数支持占位符的地方使用数学表达式。

[[_TOC_]]

## 运算符
大部分运算符可在此处查阅：https://www.objecthunter.net/exp4j/#Built-in_operators

### 数学运算符

| 运算符 |    说明    |  示例  |
|:------:|:---------:|:------:|
|   +    |   一元加   | 2 + 2  |
|   -    |   一元减   | 2 - 2  |
|   *    |    乘法    | 2 * 2  |
|   /    |    除法    | 2 / 2  |
|   ^    |    乘方    | 2 ^ 2  |
|   %    |    取余    | 2 % 2  |

### 布尔运算符
| 运算符 |       说明       | 示例  |
|:------:|:---------------:|:----:|
|   \<   |      小于        | 2<5  |
|  \<=   |   小于或等于     | 2<=5 |
|   \>   |      大于        | 5>1  |
|  \>=   |   大于或等于     | 5>=0 |
|  \==   |      等于        | 0==0 |

*布尔运算符表达式为真时返回 `1`，为假时返回 `0`。*


## 函数
大部分函数可在此处查阅：https://www.objecthunter.net/exp4j/#Built-in_functions

|     函数        | 说明                                                   |
|:---------------:|:------------------------------------------------------|
|     abs(x)      | x 的绝对值                                              |
|    acos(x)      | 反余弦                                                  |
|    asin(x)      | 反正弦                                                  |
|    atan(x)      | 反正切                                                  |
|    cbrt(x)      | 立方根                                                  |
|    ceil(x)      | 向上取整                                                |
|     cos(x)      | 余弦                                                    |
|    csch(x)      | 双曲余割                                                |
|     exp(x)      | 欧拉数的 x 次幂（e^x）                                   |
|    floor(x)     | 向下取整                                                |
|     log(x)      | 自然对数（以 e 为底）                                    |
|    log2(x)      | 以 2 为底的对数                                          |
|    log10(x)     | 以 10 为底的对数                                         |
|    logb(x)      | 以 b 为底的对数                                          |
|     sec(x)      | 正割                                                    |
|    sech(x)      | 双曲正割                                                |
|     sin(x)      | 正弦                                                    |
|    sinh(x)      | 双曲正弦                                                |
|    sqrt(x)      | 平方根                                                  |
|     tan(x)      | 正切                                                    |
|    tanh(x)      | 双曲正切                                                |
|   signum(x)     | 符号函数                                                |
|  toradian(x)    | 角度转弧度                                              |
|  todegree(x)    | 弧度转角度                                              |
|   min(x, y)     | 取最小值                                                |
|   max(x, y)     | 取最大值                                                |
|  atan2(y, x)    | y/x 反正切的主值，以弧度表示                              |
| random(min, max) | 指定范围内的随机数                                      |
| clamp(value, min, max) | 将数值限制在给定的最小值和最大值之间。如果提供的数值小于最小值，返回最小值；大于最大值，返回最大值；在范围内则原样返回 |

注意：如需请求添加更多运算符和函数，可在我们的[问题页面](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/issues)提交建议。


## 使用示例
```yml
MyCoolMob:
  Type: HUSK
  AIGoalSelectors:
    - clear
  AITargetSelectors:
    - clear
  Skills:
    - skill{s=[
      - setvar{var=skill.test;type=FLOAT;val="<caster.hp> <= <caster.mhp>"} # 如果生物生命值小于或等于最大生命值则返回 1，否则返回 0
      - message{m=<skill.var.test>} # 向玩家发消息以查看值
      ]} @trigger ~onInteract
```

```yml
MyCoolItem:
  Id: STICK
  Skills:
    - skill{s=[
        - setvar{var=skill.test;type=FLOAT;val="1>=0"} # 表达式为真，返回 1
        - message{m=<skill.var.test>} # 向玩家发消息以查看值
      ]} @Self ~onUse
```