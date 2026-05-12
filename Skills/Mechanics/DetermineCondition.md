## 描述
Determines the outcome of a Metaskill that is used as a 条件 via the [Metaskill条件](/Skills/条件/Metaskill条件) 条件


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| determination | det | Modifies 是否 the associated 条件 should return or not. Can be `true` or `false` | true |
| mode |  | How the determination value is modified. Can be `SET`, `OR`, `AND`, `NOT`. Works like you would expect a [boolean operation](https://en.wikipedia.org/wiki/Boolean_algebra#Boolean_operations) to, apart from SET that simply overrides any already defined determination value | SET<!--type:SET,AND,NOT,OR-->|


## 示例
```yaml
  Skills:
  - determinecondition{determination=true} @self
```


## 别名
- [x] detCond