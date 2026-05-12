## 描述
 
Causes an explosion of temporary items 在target location.  
Unless otherwise specified with the `allowpickup` option, those items 将会 packets, only existing on the client of the players and not on the server.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| items     | item, i   | The list of items to drop. This attribute works like the [DropItem](/skills/mechanics/dropitem)'s one                                                          | iron_sword<!--type:Item-->|
| amount    | a         | How many items will render from the spray                            | 10      |
| duration  | d         | How long (in ticks) the items will exist                             | 20      |
| radius    | r         | The radius/spread the items will start in                            | 0       |
| velocity    | v, force, f | The velocity of the items                                        | 1       |
| yVelocity   | yv, yforce, yf | The Y velocity of the items                                | `velocity` |
| yOffset     | yo, y   | The y offset the items will start at                                 | 1       |
| allowpickup | ap        | Whether the itemspray's items 应当 real items, enabling players to pick them up                                                                                        | false   |
| gravity     | g       | Whether the items 应当 affected by gravity                      | true    |
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
