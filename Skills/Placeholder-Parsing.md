## 介绍
ThThe 值 of certain 属性 can be not 仅 a static 值, but 也 a 值 containing 占位符.
> While this piece of information 不是 contained in the documentation, 您可以 检查 it by using the [MythicScribe](https://marketplace.visualstudio.com/物品?itemName=Lxlp.mythicscribe) extension and hovering over an 属性 or a 技能

Those 属性 that can have 占位符 in their 值 are 总是 parsed when the associated 技能 is executed, so that their 值 can 总是 better reflect the current state of the 生物, the 目标, the [SkillTree](/技能/SkillTrees) and the likes

## Parsing Order

When a 占位符 is parsed, the operation *总是* has certain steps 即 executed in order
- Mythic 占位符 are replaced 与ir 值
- Papi 占位符 are replaced 与ir 值
- Math operations are parsed.
  - At this exact step, functions and operators in the [Math](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/技能/Math) wiki page are 也 interpreted and used
  - This happens 仅 if the 属性 specific 占位符 类型 (PlaceholderInteger, PlaceholderFloat etc.) has支持for such, and some specific character (`*`, `-`, `+` etc.) appears in the 字符串。
    - A PlaceholderString 占位符 不会 parse math
    - A PlaceholderInt 占位符 will parse math

## Compound parsing

Please **take 注意** of the fact that each step in this process happens 再次st whatever was 已经 parsed in previous steps. So, 例如, 您可以 have 某事 like this
```yaml
  - setvariable{var=skill.somevar;val=1}
  - setvariable{var=skill.example;type=STRING;val=%some_papi_placeholder_<skill.var.somevar>%}
```

Where, in order
- `<skill.var.somevar>` 将 replaced with its 值, 即 the literal `1`
- The papi 占位符 `%some_papi_placeholder_{string}%` 将 parsed NOT 再次st the literal 字符串 `<skill.var.somevar>`, but the 已经 parsed 值, 即 `1`

SoSo that the 值 stored in `<skill.var.somevar>`可以usedinside of the papi 占位符。

> > At 同时, please do take abundant 注意 that, given the parsing order, 当 可以 make a papi 占位符 返回 some mythic-parseable 占位符 (例如, by making `%some_other_papi_placeholder%` 返回 stuff like `<skill.var.test>`), those will NOT be parsed, 自从 their "turn" has 已经 passed

If we were to 应用 this to math operations 也, we could 也 obtain 某事 like the following
```yaml
  - setvariable{var=skill.example;val=(1<skill.var.operation>3) + 4}
```
该 值 of `<skill.var.operation>` 将 inserted in the middle of 1 and 2. So
- If `<skill.var.operation>` is +, the 值 将 the 结果 of the (1+3)+4 math operation
- If `<skill.var.operation>` is -, the 值 将 the 结果 of the (1-3)+4 math operation
- If `<skill.var.operation>` is 2, the 值 将 the 结果 of the (123)+4 math operation
- if `<skill.var.operation>` is -2, the 值 将 the 结果 of the (1-23)+4 math operation