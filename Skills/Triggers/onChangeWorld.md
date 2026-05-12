## 描述
施法者切换世界时执行技能。  


## 示例
```yaml
WorldJumper:
  Type: WITHER_SKELETON
  Skills:
  - command{c=say 末地！} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_the_end}
  - command{c=say 下界！} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_nether}
```


## 别名
- [x] onChange_World
- [x] onWorld_Change
- [x] onWorldChange
