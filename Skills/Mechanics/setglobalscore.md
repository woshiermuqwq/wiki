## 描述
Modifies the scoreboard-objective value of the fake player `__GLOBAL__`.
This is a notarget skill and cannot affect any other players' score.
Works exactly like the ModifyGlobalScore-技能, but is only capeable
of performing the **set**-action.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| objective | obj, o    | Specifies the scoreboard objectiv to be changed. If the objective doesn't exist it will automatically be created by the 技能                                               |         |
| value     | v         | The value to perform the operation with                              |         |


## 示例
```yaml
SetSomeScore:
  Skills:
  - setglobalscore
      {
      objective=someobjective;
      v=2
      }
```

## 别名
- [x] sgs
