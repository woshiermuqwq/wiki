## 描述
Changes the skybox for the 目标 players.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| skybox    | sky, s, type, t, environment, env, e | What skybox should be shown to the player | 0       |

### Skybox Attribute
| Value | 描述 |
| ----- | ----------- |
| Any Integer Below 1 | Cancel the modified skybox |
| Any Integer Above 0 | Rainy |


## 示例
Makes every player in a 20 blocks 半径 see the "rainy" skybox
```yaml
  Skills:
  - skybox{s=1} @PIR{r=20}
```


## 别名
- [x] effect:skybox
- [x] e:skybox


<!--TAGS-->
<!--tag:Effect-->
