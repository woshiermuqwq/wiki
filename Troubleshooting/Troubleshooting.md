如果你在使用某个功能时遇到了问题，可以在下方查找相关条目：点击对应链接，你将被引导至一个逐步排查问题的页面。如果仍然无法解决问题，可以到我们的 [Discord] 寻求帮助。

## 通用指南
#### 创造模式
无论如何都不要在创造模式下测试。这会导致大多数功能异常。请在生存模式下进行测试。

#### 最大生命值
Spigot 默认将生物的最大生命值限制为 2048。你可以在 `spigot.yml` 文件中修改 `maxHealth` 为一个更大的值来提升此限制。

#### 控制台日志中的死亡消息
如果你在控制台中看到了类似 "Skeletal Knight was slain by PlayerName" 的消息而你不想看到这些，可以前往 `/spigot.yml`，将 `log-named-deaths` 设为 false，然后重启服务器。

## 特定功能
### MythicMobs
- [随机生成](./RandomSpawns)

### ModelEngine
- [ModelEngine 模型消失](./ModelEngine-Model-Vanishes)

<!-- LINKS -->
[discord]: https://www.mythiccraft.io/discord
