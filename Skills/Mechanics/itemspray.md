## 描述 
Causes an explosion of temporary items at the 目标 location.  
Unless otherwise specified with the `allowpickup` option, those items will be packets, only existing on the client of 玩家的 and not on the server.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| items     | item, i   | The list of items to 掉落. This attribute works like the [DropItem](/skills/技能/dropitem)'s one                                                          | iron_sword<!--type:Item-->|
| amount    | a         | How many items will render from the spray                            | 10      |
| duration  | d         | How long (in ticks) the items will exist                             | 20      |
| 半径    | r         | The 半径/spread the items will start in                            | 0       |
| 速度    | v, force, f | The 速度 of the items                                        | 1       |
| yVelocity   | yv, yforce, yf | The Y 速度 of the items                                | `速度` |
| yOffset     | yo, y   | The y offset the items will start at                                 | 1       |
| allowpickup | ap        | 是否 the itemspray's items should be real items, enabling players to pick them up                                                                                        | false   |
| gravity     | g       | 是否 the items should be affected by gravity                      | true    |
| audience    |         | The [audience] of the effect                                         | world<!--type:Audience--> |


## 示例
```yaml
  Skills:
  - itemspray{item=iron_sword;amount=20;velocity=5;d=100} @self
```


## 别名
- [x] effect:itemspray
- [x] e:itemspray


<!-- LINKS -->
[Bukkit]: https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html
[audience]: /Skills/Audience


<!--TAGS-->
<!--tag:Effect-->
<!--tag:Item-->
