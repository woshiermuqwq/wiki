## 描述
Displays a "title" and/or "subtitle" message to all targeted players.
Does nothing if the 目标 is not a player.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| title     | t         | The title string to send. Must be in double-quotes                   |         |
| subtitle  | st        | The subtitle string to send. Must be in double-quotes                |         |
| duration  | d         | How long the title will display (in ticks)                           | 1       |
| fadeIn    | fi        | The fade-in time for the title (in ticks)                            | 1       |
| fadeOut   | fo        | The fade-out time for the title (in ticks)                           | 1       |


## 示例
```yaml
  Skills:
  - sendtitle{title="Beware!";subtitle="A dangerous spell is being cast!";d=20} @PlayersInRadius{r=10}
  - ...
```


## 别名
- [x] title


<!--TAGS-->
<!--tag:Message-->
