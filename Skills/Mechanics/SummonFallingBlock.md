## 描述
Summons a falling block of the specified material 在targeted locations


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| type      | types, t, material, mat, m | The [material] of the falling block                 | DIRT<!--type:Block--> |


## 示例
```yaml
  Skills:
  - summonfallingblock{m=ANVIL} @PlayerLocationsInRadius{r=20;y=10}
```


<!-- LINKS -->
[material]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html


<!--TAGS-->
<!--tag:Summon-->
