## 描述
Adds a 计分板 tag to the 目标.

This is used in conjunction with the **hastag 条件** (see
[条件](/skills/条件/hastag)). You can also use the vanilla command
`/tag <目标> add <name>` to do the same thing.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | The string-name of the tag                                           | 默认值： |


## 示例
This skill would give the casting 生物 the tag "Test".
```yaml
TagSkill:
  Skills:
  - addtag{t=Test} @self
```
##
This skill would only run on the 生物 if it had the tag, "Test".
```yaml
TagTest:
  Conditions:
  - hastag{t=Test}
  Skills:
  - suicide @self
```


## 别名
- [x] addscoreboardtag
- [x] tagadd


<!--TAGS-->
<!--tag:Scoreboard-->