## 描述
Moves an already created variable across names and/or registries. By 默认值：, no new variable is created, so this 可用于 make two different registries reference the exact same variable, allowing the modifications on one to reflect on the other


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| from      |           | The variable to move, in the `scope.name` format                     |         |
| to        |           | Where the variable should end up, in the `scope.name` format         |         |
| removeOld |           | 是否 the moved variable should be removed from the old variable registry | false |
| createNew |       | 是否 a new variable should be created at the 目标 variable registry | false   |
| inheritExpirationTime |  | If `createNew` is true, 是否 the new variable should inherit the expiration time from the old one | true |


## 示例
```yaml
  Skills:
  - setVar{name=caster.item;type=ITEM;value=slot:HAND} @self
  - movevariable{from=caster.item;to=skill.item} @self
  - equip{item=itemvariable{variable=skill.item} head} @self
```


## 别名
- [x] moveVariable
- [x] moveVar
- [x] varMove