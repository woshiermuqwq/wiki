## 描述
Removes a scoreboard tag from the target.

This is used in conjunction with the **hastag condition** (see
[Conditions](/conditions/start)). You can also use the vanilla command
`/scoreboard players tag <player name> remove [Tag Name]` to do
the same thing.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | The string-name of the tag                                           | default |


## 示例
This skill would give the casting mob the tag "Test".
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
