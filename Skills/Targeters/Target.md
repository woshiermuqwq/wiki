## 描述
以施法者 目标为目标。

- If the 施法者 is a 生物, targets its 目标
- If the 施法者 is a 玩家, targets the 实体 the 玩家 is looking at, if close enough

注意 that some 类型 of 实体, 例如 the Ghast, 因为 of their hardcoded ai, 永远不会 结果 to have a 目标, making this 目标选择器 useless on them

## 属性
>*This 目标选择器 has no 属性*


## 示例
```yaml
ExampleSkill:
  Skills:
  - ignite @Target
```


## 别名
- [x] T