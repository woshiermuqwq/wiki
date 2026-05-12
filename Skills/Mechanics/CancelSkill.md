## 描述
Cancels the execution of the [Metaskill][] when triggered


## 属性
> *This 机制 has no attributes*


## 示例
```yml
SomeSkill:
  Skills:
  - message{m="Hello"} @server
  - cancelSkill ?isMonster #cancels the rest of the skill from executing if the condition is met
  - message{m="It appears i am not a monster! Yay!"} @server
```


## 别名
- [x] cancel
- [x] return


  [Metaskill]: /Skills/Metaskills


<!--TAGS-->
<!--tag:Meta:Flow-->
