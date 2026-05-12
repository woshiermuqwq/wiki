Kill 消息 allow you to customize what is displayed when a 玩家 is killed by your 生物. Normally when 某人 is killed, 它将 仅 print “玩家 was slain by Zombie” or “玩家 burned to death”, Etc. Giving your 生物 自定义 kill 消息 with MythicMobs is easy and can 添加 new depth to… dying.

Syntax
------

The syntax for adding Kill 消息 is simple. You can even have multiple 消息 defined for each 生物 (a random one is then chosen).
```yaml
Souleater:
  Type: SKELETON
  Display: 'Soul Eater'
  Health: 666
  KillMessages:
  - '<target.name> had their soul completely devoured'
  - '<target.name><&sq>s soul was feasted upon by <caster.name>'
  Skills:
  ...
````
It that easy! Any 玩家 killed by the Soul Eater 生物 would have one of those two 自定义 death 消息 displayed to the 服务器. [占位符](/技能/占位符) can 也 be used in the 消息, the important one being <目标.名称> 对于 名称 of the dead 玩家.

For more customization, 您可以 也 edit your `config-mobs.yml` 文件 and change KillMessagePrefix. This 允许 put a simple prefix 在...前方 all kill 消息 (占位符 不要 work in the prefix).