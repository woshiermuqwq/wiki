**难度：中级**

有时你可能希望技能只能使用特定次数，比如一只能发射 7 个火球的僵尸。本指南正是为此而生！

我们将使用变量来跟踪技能已使用的次数，一旦达到我们想要的总次数，技能将停止工作。

# 指定使用次数
此示例将累加变量，一旦达到 7，技能将停止工作。
```yaml
FireballSkill:
  Conditions:
  - variableequals{var=caster.fireballs;val=7} false
  Skills:
  - setvariable{var=caster.fireballs;val=<caster.var.fireballs|0>+1}
  - <在此放置你的技能技能>
```
在此示例中，每次技能运行时我们都给变量加 "1"，如果变量不存在则通过[变量回退值](/Skills/Variables#variable-fallback)将其设为 0，然后正常执行我们的技能。

技能设置了 [VariableEquals](/skills/conditions/variableequals) 条件，这意味着一旦变量达到 7，条件将阻止技能继续运行。

如果你想要重置计数器，可以简单地使用 [VariableUnset]() 技能。
```yaml
Skills:
- variableunset{var=caster.fireballs}
```
