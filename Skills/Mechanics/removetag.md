## 描述
Removes a 计分板 tag from the 目标.

This is used in conjunction with the **hastag 条件** (see
[条件](/条件/start)). You can also use the vanilla command
`/计分板 players tag <player name> remove [Tag Name]` to do
the same thing.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | The string-name of the tag                                           | 默认值： |


## 示例
This skill would give the casting 生物 the tag "Test".
```yaml
UntagSkill:
  Skills:
  - removetag{t=Test} @self
```


## 别名
- [x] removescoreboardtag
- [x] tagremove


<!--TAGS-->
<!--tag:Scoreboard-->
