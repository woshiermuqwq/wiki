变量是一套用于存储信息的系统。通过变量系统，你可以存储和操作各种值，以便之后在占位符或条件中使用。这些值可以是永久的，也可以是临时的。

[[_TOC_]]

# 变量类型
变量可以有好几种类型，在使用 [setVariable](/skills/mechanics/setvariable) 技能初始化变量时指定。不同类型之间通常可以互相转换，MythicMobs 会尽量在合适的场景中应用变量，但如果把某个变量类型用于毫无意义的地方，它会报错。

| **类型** | **描述**                          |
|----------|-----------------------------------|
| INTEGER  | 不含小数位的整数。                  |
| FLOAT    | 含小数位的数字。                    |
| DOUBLE   | 含小数位的数字。可表示的数值范围远大于 FLOAT。 |
| STRING   | 一个单词或句子。                    |
| BOOLEAN  | 只能为 true 或 false 的值。          |
| SET      | 一组无序且唯一的值。                 |
| LIST     | 一个有序的条目列表。                 |
| MAP      | 一组键值对列表。                     |
| LOCATION | 服务器中的一个位置。                 |
| VECTOR   | 由 3 个 DOUBLE 值组成的列表。        |
| TIME     | 时间上的某一刻，以自纪元以来的毫秒数表示。 |
| METASKILL | 一段内联元技能，在变量创建时即刻解析。 |
| ITEM     | 一个物品堆，可用于存储和修改物品数据。 |


# 变量作用域
变量的「作用域」指的是该变量**存在于何处**。并非所有场景下都能使用所有作用域（例如条件中可能没有施法者，此时施法者反而是条件的评估目标）。

| **作用域** | **变量存在的范围**                                                                 |
|----------|------------------------------------------------------------------------------------|
| SKILL    | 当前技能树上。始终为临时变量，当前技能队列结束时即消失。                                       |
| CASTER   | 施法者生物上。                                                                            |
| TARGET   | 技能/条件的目标上。                                                                       |
| WORLD    | 当前世界上。                                                                              |
| GLOBAL   | 整个服务器上。                                                                            |


# 用法
所有变量相关的技能和条件都接受 `var=` 和 `scope=` 属性，用于指定你要操作的变量名及其位置。你还可以用 `var=scope.variable_name` 这种简写形式来指定作用域。以下两种写法效果相同：
```yaml
    - setvariable{var=target.somevariable; ...}
    - setvariable{var=somevariable;scope=target; ...}
```

## 各变量类型的行为

### 数字
包括 INTEGER、FLOAT 和 DOUBLE，它们的行为在功能上一致。
```yaml
  # 创建数字变量
  - setvariable{var=skill.example;type=DOUBLE;val=1.5}

  # 为数字增加一个值
  - variableadd{var=skill.example;amount=2}

  # 从数字中减去一个值
  - variablesubtract{var=skill.example;amount=1}

  # 输出数字
  - message{m=<skill.var.example>} # 2.5
```

### 字符串
```yaml
  # 创建字符串变量
  - setvariable{var=skill.example;type=STRING;val="oh oh hello"}

  # 向字符串追加一个值
  - variableadd{var=skill.example;amount=" world"}

  # 从字符串中移除所有匹配的子串
  - variablesubtract{var=skill.example;amount="oh "}

  # 输出字符串
  - message{m=<skill.var.example>} # hello world
```

### 布尔值
```yaml
  # 创建布尔变量
  - setvariable{var=skill.example;type=BOOLEAN;val=true} # 也可用 "1" 或 "yes" 表示 "true"，其他值均为 "false"

  # 对布尔值执行逻辑或运算
  - variableadd{var=skill.example;amount=1} # 当前值或新值任一为真值时，结果为 true（或逻辑）

  # 对布尔值执行逻辑与运算
  - variablesubtract{var=skill.example;amount=1} # 只有当前值和新值都为真时，结果才为 true（与逻辑）

  # 输出布尔值
  - message{m=<skill.var.example>} # true
```

### 集合
```yaml
  # 创建集合
  - setvariable{var=skill.example;type=SET;val=1,2,hello}

  # 向集合添加值
  - variableadd{var=skill.example;amount=world}
  - variableadd{var=skill.example;amount=1} # 如果添加的值已存在，集合不会变化

  # 从集合中移除值
  - variablesubtract{var=skill.example;amount=hello}

  # 输出集合
  - message{m=<skill.var.example>} # 1,2,world
```

### 列表
```yaml
  # 创建列表
  - setvariable{var=skill.example;type=LIST;val=1,2,hello}

  # 向列表添加值
  - variableadd{var=skill.example;amount=world}

  # 从列表中移除值（按索引）
  - variablesubtract{var=skill.example;amount=0}

  # 输出列表
  - message{m=<skill.var.example>} # 2,hello,world
  - message{m=<skill.var.example.0>} # 2
```

### 映射
```yaml
  # 创建映射
  - setvariable{var=skill.example;type=MAP;val="hello=world;mamma=mia"}

  # 向映射添加值
  - variableadd{var=skill.example;amount="pizza=pasta;please=help"}

  # 从映射中移除值（按键名）
  - variablesubtract{var=skill.example;amount=hello}

  # 输出映射
  - message{m=<skill.var.example>} # mamma=mia;pizza=pasta;please=help
  - message{m=<skill.var.example.please>} # help
```

### 位置
```yaml
  # 创建位置变量
  - setvariable{var=skill.example;type=LOCATION;val=world,1,2,3}
  - setvarloc{var=skill.specialexample;val=@selflocation} # 也可以使用这个专用技能来设置位置变量

  # 增加坐标值
  - variableadd{var=skill.example;amount=1,2,3}

  # 减少坐标值
  - variablesubtract{var=skill.example;amount=1,1,1}

  # 输出位置
  - message{m=<skill.var.example>} # world,1.0,3.0,5.0
```

### 向量
```yaml
  # 创建向量变量
  - setvariable{var=skill.example;type=VECTOR;val=1,2,3}

  # 增加各个分量值
  - variableadd{var=skill.example;amount=1,2,3}

  # 减少各个分量值
  - variablesubtract{var=skill.example;amount=1,1,1}

  # 输出向量
  - message{m=<skill.var.example>} # 1.0,3.0,5.0
```

### 时间
```yaml
  # 创建时间变量
  - setvariable{var=skill.example;type=TIME;val=1234}

  # 增加值
  - variableadd{var=skill.example;amount=2}

  # 减少值
  - variablesubtract{var=skill.example;amount=1}

  # 输出时间
  - message{m=<skill.var.example>} # 1235
```

### 元技能
```yaml
  # 创建元技能变量
  - setvariable{var=skill.example;type=METASKILL;val=[
    - message{m=hello world} @self
    ]}

  # 输出元技能的原始文本
  - message{m=<skill.var.example>}

  # 执行该元技能
  - vskill{variable=skill.example}
```
> 如果元技能中包含元技能类技能（如 skill 或 projectile），需要等待 15~21 刻后再执行，以避免出错。

### 物品
```yaml
  # 创建物品变量
  - setvariable{var=skill.example;type=ITEM;val=<target.item.itemstack.HAND>}

  # 某些前缀可以触发特定行为。可用前缀包括 `mythic:`、`slot:`、`drop` 和 `material:`
  - setvariable{var=skill.example;type=ITEM;val=mythic:BanditTunic}
  - setvariable{var=skill.example;type=ITEM;val=material:STONE}
  - setvariable{var=skill.example;type=ITEM;val=drop:itemvariable{var=caster.otheritem}} # 适用于单个或复数掉落。掉落表将返回从中随机抽取的一件物品
  - setvariable{var=skill.example;type=ITEM;val=slot:HAND}
  - setvariable{var=skill.example;type=ITEM;val=slot:10}


  # 更新物品变量
  - setvariable{var=skill.example;type=ITEM;val=<skill.var.example.withname.test.withlore.hello,world>}

  # 输出物品的物品堆
  - message{m=<skill.var.example>}

  # 给予和取走物品
  - giveitem{variable=skill.example}
  - takeitem{variable=skill.example}

  # 对于所有接受掉落/掉落表作为可选值的技能，也可以通过 itemvariable 掉落类型
  # 来丢弃存储在指定物品变量中的物品
  - equip{item=itemvariable{variable=skill.item} head} @self
  - giveitem{item=itemvariable{variable=skill.item}} @self

```
> 在早于 1.21.7 的某些版本中存在以下问题：
>  - 持久化物品变量（保存在持久化生物或玩家上）
>  - 使用 <target.item.itemstack.HAND> 来设置变量
> 
> 简而言之，在受影响的版本上，当物品堆被序列化为字符串再从该字符串反序列化时，部分数据会丢失。如果你在使用受影响的版本，仍然可以使用此变量，但必须：
> - 只用它来存储**不**需要在服务器重启后保留的临时数据
> - 不要用 <target.item.itemstack.HAND> 占位符来设置变量，而是像上面那样使用 slot: 前缀


## 变量相关技能
变量相关技能是一类操作变量的特殊技能。它们可以以实体、位置或无目标为目标，但目标会影响结果，具体取决于你使用的作用域。例如，在不以实体为目标的情况下尝试获取目标作用域的变量，显然会失败。

| 技能                                                         | 描述                                        |
|--------------------------------------------------------------|---------------------------------------------|
| [SetVariable](/skills/mechanics/setvariable)                 | 初始化并设置一个变量。                           |
| [SetVariableLocation](/skills/mechanics/setvariablelocation) | 设置一个变量，其值取决于目标位置。                  |
| [VariableUnset](/skills/mechanics/variableunset)             | 删除变量。                                      |
| [VariableAdd](/skills/mechanics/variableadd)                 | 为变量增加值。                                   |
| [VariableSubtract](/skills/mechanics/variablesubtract)       | 从变量中减去值。                                 |
| [VariableMath](/skills/mechanics/variablemath)               | 允许你用数值变量进行计算。                        |

## 变量相关条件
| 条件                                                    | 描述                                        |
|---------------------------------------------------------|---------------------------------------------|
| [VariableEquals](/skills/conditions/variableequals)     | 检查变量是否等于指定值。                        |
| [VariableIsSet](/skills/conditions/variableisset)       | 检查变量是否已设置。                             |
| [VariableInRange](/skills/conditions/variableinrange)   | 检查数值变量是否在某个范围内。                    |
| [VariableContains](/skills/conditions/VariableContains) | 检查变量是否包含指定值。                          |

## 变量相关目标选择器
| 目标选择器                                                 | 描述                                        |
|-----------------------------------------------------------|---------------------------------------------|
| @[VariableLocation](/Skills/Targeters/VariableLocation)   | 以存储在指定位置变量中的位置为目标。               |


# 变量占位符
可以在任何支持占位符的 MythicMobs 技能或值中引用变量，通常使用格式 `<scope.var.variable>`。

变量占位符还可以使用元关键词来改变占位符的输出，甚至可以串联多个元关键词来获得「复合」效果。

更多信息请参见[元变量占位符说明](/Skills/Placeholders#meta-variable-placeholders)。

# 变量回退值
在使用占位符变量时，还可以通过 `<scope.var.variable|default>` 语法指定一个「默认值」，当变量未定义时使用该值。

```yaml
    - message{m="Hello there, <target.var.title|wanderer>"} @trigger ~onInteract
```

在这个例子中，如果右键点击 NPC 的人身上没有设置 `title` 变量，NPC 会回复 "Hello there, wanderer"。然而，如果我们之前执行过：

```yaml
    - setVariable{var=target.title;value="Sir"} @trigger ~onInteract
```

……哪怕是通过另一个生物设置的，第一个生物也会说 "Hello there, Sir"。

# 嵌套变量
变量可以无限层嵌套：此时最内层的变量会最先解析，然后由内向外逐层解析。

```yaml
  Skills:
    - setvariable{var=caster.hello;type=STRING;val=example_name} @self
    - setvariable{var=caster.example_name;type=STRING;val=Hello There!} @self
    - message{m="<caster.var.<caster.var.hello>>"} @PIR{r=10}
```
> 在这个例子中，消息最终会显示为 "Hello there!"

> 由于 Mythic 占位符解析器的限制，将同一个占位符既「单独使用」又作为另一个占位符的嵌套值使用时非常危险，极有可能导致嵌套占位符无法正确解析！
> 例如：
> ```yaml
>  - message{m=<skill.var.test> <skill.var.<skill.var.test>>} # 不要这样做！
> ```
> 结果无法预料！要解决这个问题，需要更改变量名或预先解析：
> ```yaml
>  - setvariable{var=skill.segment;type=STRING;val=<skill.var.<skill.var.test>>}
>  - message{m=<skill.var.test> <skill.var.segment>} # 应该这样做！
> ```

# [生物变量](/Mobs/Mobs#variables)
生物可以在生成时就携带一些变量，通过[生物变量](/Mobs/Mobs#variables)字段来配置。
```yaml
VariableZombie:
     Type: ZOMBIE
     Variables:
       SomeVariable: something
       AnIntVariable: int/2
       AFloatVariable: float/420.69
```