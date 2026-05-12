## 描述
Adds a scoreboard tag to the target.

This is used in conjunction with the **hastag condition** (see
[Conditions](/skills/conditions/hastag)). You can also use the vanilla command
`/tag <targets> add <name>` to do the same thing.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| tag       | t         | The string-name of the tag                                           | default |


## 示例
This skill would give the casting mob the tag "Test".
```yaml
TagSkill:
  Skills:
  - addtag{t=Test} @self
```
##
This skill would only run on the mob if it had the tag, "Test".
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
