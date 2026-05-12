## 描述
以位置 of the "原点" or "source" of a meta-技能. While 即 通常 the casting 生物, there are special cases where this 不是 true (例如 与 弹射物 技能, 该 "原点" is the 位置 of the 弹射物)为目标。


## 属性
>*This 目标选择器 has no 属性*


## 示例
The 原点 目标选择器 is 极其 versatile. Take the following 元技能, 例如:
```yaml
ExampleSkill:
  Skills:
  - effect:particles @origin
```
IfIf 它是 executed by a 生物 normally, if将显示the 粒子 at its 位置, 自从 the 原点 of the 技能 is 自身. In this aspect, `origin` 不 behave differently from a `self` 目标选择器。

BuBut if the 元技能 is executed inside a meta 技能 or 之后 manually changing a 技能 原点 via the [原点 Universal 属性](/技能/技能#universal-属性), the 原点 of the 技能 will change most of the times, and the 粒子 将 displayed in a different spot.

The exact position of the `origin` changes 基于 the context, and more information regarding this 行为可以foundin wiki pages 对于 various 技能 that *do* make use of this。

## 别名
- [x] source