## 描述
选取施法生物的所有者。  
所有者可通过 [SetOwner](/Skills/mechanics/setowner) 技能设置。


## 属性
>*此目标选择器没有属性*


## 示例
此嵌套技能将向施法生物的所有者发送一条消息
```yaml
ExampleSkill:
  Skills:
  - message{m="你好！"} @Owner
```
