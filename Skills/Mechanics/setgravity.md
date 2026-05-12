## 描述
Sets whether gravity affects the target entity.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| gravity   | g, b, bool, u, use | Sets whether the entity uses gravity                        | true    |

  
## 示例
```yaml
  Skills:
  - setgravity{g=false} @self ~onSpawn
  - setusegravity{g=false} @self ~onSpawn
  - ...
```


## 别名
- [x] setusegravity
