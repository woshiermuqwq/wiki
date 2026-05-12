变量是一个用于存储信息的系统。使用变量系统，你可以存储和操作值，以便后续在占位符或条件中使用。这些值可以是永久的或临时的。

[[_TOC_]]

# 变量 类型
变量可以是多种类型之一，类型在使用 [setVariable](/skills/mechanics/setvariable) 技能初始化变量时定义。类型之间通常可以互换，MythicMobs 会尽力将特定变量应用到任何需要的情境中，但如果你尝试将某种变量类型用于无意义的场景，则会抛出错误。

| **类型** | **描述** |
|----------|----------------------------------|
| INTEGER | 没有小数位的数字。 |
| FLOAT | 带小数位的数字。 |
| DOUBLE | 带小数位的数字。可表示比 FLOAT 大得多的数字。 |
| STRING | 一个单词或句子。 |
| BOOLEAN | 值为 true 或 false。 |
| SET | 一组无序且唯一的值。 |
| LIST | 一个有序的条目列表。 |
| MAP | 一系列键值对。 |
| LOCATION | 服务器中的一个位置。 |
| VECTOR | 由 3 个 DOUBLE 值组成的列表。 |
| TIME | 时间中的一个时刻，以自纪元以来的毫秒数表示。 |
| METASKILL | 一个内联元技能，在变量创建时解析。 |
| ITEM | 一个物品堆，可用于存储和修改物品数据。 |

# 变量 作用域
变量的"作用域"是指该变量**存在于哪里**。并非所有作用域都适用于所有情况（例如，条件可能没有施法者，而是施法者是条件的目标）。

| **作用域** | **变量存在的位置** |
|----------|---------------------------------------------------------------------------------------------|
| SKILL | 在当前技能树上。始终是临时的，会在当前技能队列结束时消失。 |
| CASTER | 在施法生物上。 |
| TARGET | 在技能/条件的目标上。 |
| WORLD | 在当前世界上。 |
| GLOBAL | 在服务器上。 |

# 用法
所有变量技能和条件都接受 `var=` 和 `scope=` 属性来确定你要操作的变量及其所在位置。你也可以使用 `var=scope.variable_name` 来简写作用域。以下示例将返回相同的结果：
```yaml
    - setvariable{var=target.somevariable; ...}
    - setvariable{var=somevariable;scope=target; ...}
```

## 变量 类型行为

### Number（数字）
包含 INTEGER、FLOAT 和 DOUBLE，因为它们的行为功能上相同。
```yaml
  # 创建你的数字变量
  - setvariable{var=skill.example;type=DOUBLE;val=1.5}

  # 为数字添加值
  - variableadd{var=skill.example;amount=2}

  # 从数字中减去值
  - variablesubtract{var=skill.example;amount=1}

  # 打印数字
  - message{m=<skill.var.example>} # 2.5
```

### String（字符串）
```yaml
  # 创建你的字符串变量
  - setvariable{var=skill.example;type=STRING;val="oh oh hello"}

  # 向字符串追加值
  - variableadd{var=skill.example;amount=" world"}

  # 从字符串中移除所有匹配的子串
  - variablesubtract{var=skill.example;amount="oh "}

  # 打印字符串
  - message{m=<skill.var.example>} # hello world
```

### Boolean（布尔值）
```yaml
  # 创建你的布尔变量
  - setvariable{var=skill.example;type=BOOLEAN;val=true} # "1" 或 "yes" 也表示 "true"，其他任何值表示 "false"

  # 对布尔值执行 OR 逻辑运算
  - variableadd{var=skill.example;amount=1} # 若当前值或添加的值中任一个是 truthy，则将布尔值设为 true（OR 逻辑）

  # 对布尔值执行 AND 逻辑运算
  - variablesubtract{var=skill.example;amount=1} # 仅当当前值和添加的值都是 truthy 时，才将布尔值设为 true（AND 逻辑）

  # 打印布尔值
  - message{m=<skill.var.example>} # true
```

### Set（集合）
```yaml
  # 创建集合
  - setvariable{var=skill.example;type=SET;val=1,2,hello}

  # 向集合添加值
  - variableadd{var=skill.example;amount=world}
  - variableadd{var=skill.example;amount=1} # 如果添加的值已存在，集合不会改变

  # 从集合中移除值
  - variablesubtract{var=skill.example;amount=hello}

  # 打印集合
  - message{m=<skill.var.example>} # 1,2,world
```

### List（列表）
```yaml
  # 创建列表
  - setvariable{var=skill.example;type=LIST;val=1,2,hello}

  # 向列表添加值
  - variableadd{var=skill.example;amount=world}

  # 从列表中移除值（使用索引）
  - variablesubtract{var=skill.example;amount=0}

  # 打印列表
  - message{m=<skill.var.example>} # 2,hello,world
  - message{m=<skill.var.example.0>} # 2
```

### Map（映射表）
```yaml
  # 创建映射表
  - setvariable{var=skill.example;type=MAP;val="hello=world;mamma=mia"}

  # 向映射表添加值
  - variableadd{var=skill.example;amount="pizza=pasta;please=help"}

  # 从映射表中移除值（使用键名）
  - variablesubtract{var=skill.example;amount=hello}

  # 打印映射表
  - message{m=<skill.var.example>} # mamma=mia;pizza=pasta;please=help
  - message{m=<skill.var.example.please>} # help
```

### Location（位置）
```yaml
  # 创建你的位置变量
  - setvariable{var=skill.example;type=LOCATION;val=world,1,2,3}
  - setvarloc{var=skill.specialexample;val=@selflocation} # 你也可以通过此特殊技能设置位置变量

  # 增加坐标值
  - variableadd{var=skill.example;amount=1,2,3}

  # 减少坐标值
  - variablesubtract{var=skill.example;amount=1,1,1}

  # 打印位置
  - message{m=<skill.var.example>} # world,1.0,3.0,5.0
```

### Vector（向量）
```yaml
  # 创建你的向量变量
  - setvariable{var=skill.example;type=VECTOR;val=1,2,3}

  # 增加分量值
  - variableadd{var=skill.example;amount=1,2,3}

  # 减少分量值
  - variablesubtract{var=skill.example;amount=1,1,1}

  # 打印向量
  - message{m=<skill.var.example>} # 1.0,3.0,5.0
```

### Time（时间）
```yaml
  # 创建你的时间变量
  - setvariable{var=skill.example;type=TIME;val=1234}

  # 增加值
  - variableadd{var=skill.example;amount=2}

  # 减少值
  - variablesubtract{var=skill.example;amount=1}

  # 打印时间
  - message{m=<skill.var.example>} # 1235
```

### MetaSkill（元技能）
```yaml
  # 创建你的元技能变量
  - setvariable{var=skill.example;type=METASKILL;val=[
    - message{m=hello world} @self
    ]}

  # 打印元技能的原始文本
  - message{m=<skill.var.example>}

  # 执行元技能
  - vskill{variable=skill.example}
```
> 如果元技能包含元技能（如 skill 或 projectile），你必须在执行前等待 15~21 tick 以防止错误。

### Item（物品）
```yaml
  # 创建你的物品变量
  - setvariable{var=skill.example;type=ITEM;val=<target.item.itemstack.HAND>}

  # 可以使用一些前缀来引发特定行为。有效的前缀有 `mythic:`、`slot:`、`drop` 和 `material:`
  - setvariable{var=skill.example;type=ITEM;val=mythic:BanditTunic}
  - setvariable{var=skill.example;type=ITEM;val=material:STONE}
  - setvariable{var=skill.example;type=ITEM;val=drop:itemvariable{var=caster.otheritem}} # 适用于单个和多个掉落。掉落表将返回从中随机抽取的一个物品
  - setvariable{var=skill.example;type=ITEM;val=slot:HAND}
  - setvariable{var=skill.example;type=ITEM;val=slot:10}


  # 更新你的物品变量
  - setvariable{var=skill.example;type=ITEM;val=<skill.var.example.withname.test.withlore.hello,world>}

  # 打印物品的 ItemStack
  - message{m=<skill.var.example>}

  # 给予和取走物品
  - giveitem{variable=skill.example}
  - takeitem{variable=skill.example}

  # 对于所有接受 drop/droptable 作为可选值的技能，也可以使用 itemvariable 掉落类型
  # 来掉落存储在指定物品变量中的物品
  - equip{item=itemvariable{variable=skill.item} head} @self
  - giveitem{item=itemvariable{variable=skill.item}} @self

```
> 在某些低于 1.21.7 的版本中，存在以下问题：
>  - 持久保存物品变量（在持久生物或玩家上）
>  - 使用 <target.item.itemstack.HAND> 设置变量
>
> 简而言之，在受影响的版本中，当 ItemStack 序列化为字符串并随后从该字符串反序列化时，会丢失某些数据。如果你使用的是受影响的版本之一，仍然可以使用此变量，但必须：
> - 仅用它存储不打算跨服务器重启持久保存的临时数据
> - 不要使用 <target.item.itemstack.HAND> 占位符设置变量，而是使用上面展示的 slot: 前缀


## 变量 技能
变量技能是利用变量的特殊技能。它们可以以实体、位置为目标，也可以没有目标，但目标可能会影响结果，具体取决于你使用的作用域。例如，如果你没有以实体为目标，尝试获取目标作用域的变量显然会失败。

| 技能 | 描述 |
|--------------------------------------------------------|--------------------------------------------------|
| [SetVariable](/skills/mechanics/setvariable) | 初始化并设置变量。 |
| [SetVariableLocation](/skills/mechanics/setvariablelocation) | 设置变量，其值取决于目标位置。 |
| [VariableUnset](/skills/mechanics/variableunset) | 取消设置变量。 |
| [VariableAdd](/skills/mechanics/variableadd) | 向变量添加值。 |
| [VariableSubtract](/skills/mechanics/variablesubtract) | 从变量中减去值。 |
| [VariableMath](/skills/mechanics/variablemath) | 允许用数字变量进行计算。 |

## 变量 条件
| 条件 | 描述 |
|--------------------------------------------------|------------------------------------------------|
| [VariableEquals](/skills/conditions/variableequals) | 检查变量是否等于给定值。 |
| [VariableIsSet](/skills/conditions/variableisset) | 检查变量是否已设置。 |
| [VariableInRange](/skills/conditions/variableinrange) | 检查数字变量是否在指定范围内。 |
| [VariableContains](/skills/conditions/VariableContains) | 检查变量是否包含给定值。 |

## 变量 目标选择器
| 目标选择器 | 描述 |
|--------------------------------------------------|------------------------------------------------|
| @[VariableLocation](/Skills/Targeters/VariableLocation) | 以指定 Location 变量中存储的位置为目标。 |

# 变量 占位符
变量可以在任何允许占位符的 MythicMobs 技能或值中引用。通常使用格式 `<scope.var.variable>`。

变量占位符还可以使用元关键词来改变占位符的输出，甚至可以链式使用多个元关键词来获得"复合"效果。

更多信息请参阅[元变量占位符说明](/Skills/Placeholders#meta-variable-placeholders)

# 变量 默认值
使用占位符变量时，你可以使用语法 `<scope.var.variable|default>` 指定一个"默认"值，在变量未定义时使用。

```yaml
    - message{m="Hello there, <target.var.title|wanderer>"} @trigger ~onInteract
```

在此示例中，如果右键点击 NPC 的人没有设置 "title" 变量，NPC 会回复 "Hello there, wanderer"。
但是，如果我们这样做：

```yaml
    - setVariable{var=target.title;value="Sir"} @trigger ~onInteract
```

...在之前的某个环节（即使是不同的生物设置的），第一个生物就会说 "Hello there, Sir"。

# 嵌套 变量
变量也可以无限嵌套：如果这样做，最内层的变量将首先被解析，然后从内向外依次解析每个变量。

```yaml
  Skills:
    - setvariable{var=caster.hello;type=STRING;val=example_name} @self
    - setvariable{var=caster.example_name;type=STRING;val=Hello There!} @self
    - message{m="<caster.var.<caster.var.hello>>"} @PIR{r=10}
```
> 在此示例中，消息将显示 "Hello there!"

> 由于 Mythic 占位符解析器的限制，将同一个占位符同时"单独"使用*并且*作为嵌套值在另一个占位符中使用是非常危险的，很可能会导致嵌套占位符无法被正确解析！
> 例如，这样
> ```yaml
>  - message{m=<skill.var.test> <skill.var.<skill.var.test>>} # 不要这样做！
> ```
> 会有不确定的结果！要解决此问题，需要更改变量名称或提前解析它：
> ```yaml
>  - setvariable{var=skill.segment;type=STRING;val=<skill.var.<skill.var.test>>}
>  - message{m=<skill.var.test> <skill.var.segment>} # 改为这样做！
> ```

# [生物变量](/Mobs/Mobs#variables)
生物可以在生成时通过[生物变量](/Mobs/Mobs#variables)字段预设一些变量。
```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```
