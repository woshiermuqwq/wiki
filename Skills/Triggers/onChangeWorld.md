## 描述
Ex执行 the 技能 when the 施法者 changes 世界.


## 示例
```yaml
WorldJumper:
  Type: WITHER_SKELETON
  Skills:
  - command{c=say The End!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_the_end}
  - command{c=say The Nether!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_nether}
```


## 别名
- [x] onChange_World
- [x] onWorld_Change
- [x] onWorldChange