# 随机生成不工作

- 检查随机生成的 `Chance`（概率）：如果它太低，可能就是问题所在，将其设为 `1` 来验证是否是概率问题。如果不是，继续按以下步骤排查，在问题解决前不要恢复原值。
- 检查世界难度：如果你在尝试生成敌对类型的生物，难度不应设为和平！
- 移除**所有限制条件**，例如 `biome` 和 `conditions`，看看是否能够正常生成。
- 检查是否有任何地方拼写错误，例如：
    - 生物的内部名称
    - 世界名称
- 如果删除所有条件后随机生成开始工作，逐一重新添加条件，看看是哪个（些）条件最初导致了问题。如果你无法理解为什么这些条件会有问题，可以到我们的 [Discord] 寻求帮助。
- 如果随机生成仍然不工作，根据随机生成的 `Action` 类型继续按以下步骤调试：

### ADD 动作
- 确保插件的生成配置已正确设置
  - （MM 5.6.1 以下版本）：配置文件位于 `/MythicMobs/config.yml`
  - （MM 5.6.1 及以上版本）：配置文件位于 `/MythicMobs/config/config-spawning.yml`
- 确保你已在配置文件中启用了 `GenerateSpawnPoints`，否则 ADD 动作不会生效
- 确保你在生存或冒险模式下，其他游戏模式不会生效
- 如果以上所有方法都失败了，到我们的 [Discord] 寻求帮助

### REPLACE 动作
- 检查世界难度：不应设为和平！
- 确保世界可以自然生成生物（例如，确保 `doMobSpawning` 游戏规则设为 `true` 等）。
- 检查区域（[World Guard](https://dev.bukkit.org/projects/worldguard)、[Grief Defender](https://www.spigotmc.org/resources/1-12-2-1-20-4-griefdefender-claim-plugin-grief-prevention-protection.68900/) 等）的[标志](https://worldguard.enginehub.org/en/latest/regions/flags/#mobs-fire-and-explosions)，看该区域是否有[阻止生物生成的标志](https://worldguard.enginehub.org/en/latest/regions/flags/#mobs-fire-and-explosions)。

<!-- LINKS -->
[discord]: https://www.mythiccraft.io/discord
