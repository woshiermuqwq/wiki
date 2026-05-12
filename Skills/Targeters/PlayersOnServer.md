## 描述
以all 玩家 in the 服务器为目标。


## 属性
>*This 目标选择器 has no 属性*


## 示例
```yaml
PlayerCount_ServerWide:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @PlayersOnServer{targetself=true}
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```


## 别名
- [x] 服务器
- [x] 每个人