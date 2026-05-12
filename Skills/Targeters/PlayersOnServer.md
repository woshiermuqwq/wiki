## 描述
选取服务器上的所有玩家


## 属性
>*此目标选择器没有属性*


## 示例
```yaml
PlayerCount_ServerWide:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @PlayersOnServer{targetself=true}
  - message{m="当前世界已加载 <skill.var.count> 个实体"} @self
```


## 别名
- [x] server
- [x] everyone
