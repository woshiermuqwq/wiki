## 描述
The blockunmask effect is used to revert blockchanges made by the blockmask effect. For instance, this effect 可用于 a high 半径 after a 生物 has died in order to “clean up” the fake block updates sent. However this is not necessary, because the fake block changes created by the blockmask effect will be reverted if a chunk is reloaded for a player (but will only revert for that player).


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 半径    | r         | The 半径 of the blockunmask effect                                 | 0       |
| shape     | s         | The shape of the effect. `Sphere`/`Cube`                             | SPHERE<!--type:Shape-->|


## 示例
Will forcibly reverse all effects created by the blockmask effect in the specified 半径.
```yaml
  Skills:
  - effect:blockunmask{r=30}
```


## 别名
- [x] effect:blockUnmask
- [x] e:blockunmask


<!--TAGS-->
<!--tag:Effect-->