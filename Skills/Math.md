Lets you make simple or advanced calculations. Any 占位符 that 返回 a number is 支持.
You can use math in most places that支持占位符。

[[_TOC_]]

## Operators
大部分se operators可以foundhere https://www.objecthunter.net/exp4j/#Built-in_operators。
### Math Operators

| Operator | Description | 示例 |
|:--------:|:----------------:|:---------:|
| + | Unary plus | 2 + 2 |
| - | Unary minus | 2 - 2 |
| * | Multiplication | 2 * 2 |
| / | Division | 2 / 2 |
| ^ | 战力 | 2 ^ 2 |
| % | Remainder | 2 % 2 |

### 布尔值 Operators
| Operators | Description | 示例 |
|:---------:|:------------------------:|:-------:|
| \< | Less than | 2<5 |
| \<= | Less than or 等于 | 2<=5 |
| \> | Greater than | 5>1 |
| \>= | Greater than or 等于 | 5>=0 |
| \== | Equals | 0==0 |

*布尔值 operators将返回`1` if the expression is true and `0` if 它是 false.*。


## Functions
大部分se functions可以foundhere https://www.objecthunter.net/exp4j/#Built-in_functions。

| Function | Description |
|:----------------:|:----------------------------------------------------------------|
| abs(x) | the absolute 值 of (x) |
| acos(x) | arc cosine |
| asin(x) | arc sine |
| atan(x) | arc tangent |
| cbrt(x) | cubic root |
| ceil(x) | nearest upper 整数 |
| cos(x) | cosine |
| csch(x) | hyperbolic cosecant |
| exp(x) | euler number raised to the 战力 (e^x) |
| floor(x) | nearest lower 整数 |
| log(x) | logarithmus naturalis (base e) |
| log2(x) | logarithm to base 2 |
| log10(x) | logarithm to base 10 |
| logb(x) | logarithm to base b |
| sec(x) | secant |
| sech(x) | hyperbolic secant |
| sin(x) | sine |
| sinh(x) | hyperbolic sine |
| sqrt(x) | square root |
| tan(x) | tangent |
| tanh(x) | hyperbolic tangent |
| signum(x) | signum of a 值 |
| toradian(x) | converts from degrees to radians |
| todegree(x) | converts from radians to degrees |
| min(x, y) | minimum |
| max(x, y) | maximum |
| atan2(y, x) | principal 值 of the arc tangent of y/x, expressed in radians |
| random(min, max) | random with limits |
| clamp(值, min, max) | Clamps a number between a given minimum and maximum. If the number you provide is 小于 the minimum, it将返回the minimum. If 它是 大于 the maximum, it 返回 the maximum. If 它是 在...之间 minimum and maximum, it 返回 the number unchanged |。

NOTE: You can request to 添加 more operators and functions by making a suggestion ticket in our [issues page](https://git.mythiccraft.io/mythiccraft/MythicMobs/-/issues)


## 示例 Usage
```yml
MyCoolMob:
  Type: HUSK
  AIGoalSelectors:
    - clear
  AITargetSelectors:
    - clear
  Skills:
    - skill{s=[
      - setvar{var=skill.test;type=FLOAT;val="<caster.hp> <= <caster.mhp>"} #returns 1 or 0 if the mob's health is less than or equal to its max health
      - message{m=<skill.var.test>} #sends the player a message to see the value
      ]} @trigger ~onInteract
```

```yml
MyCoolItem:
  Id: STICK
  Skills:
    - skill{s=[
        - setvar{var=skill.test;type=FLOAT;val="1>=0"} #returns 1 since the expression evaluates to true
        - message{m=<skill.var.test>} #sends the player a message to see the value
      ]} @Self ~onUse
```