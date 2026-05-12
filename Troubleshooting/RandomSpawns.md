# RandomSpawns not working

- 检查 移除 `Chance` of the randomspawn: if 它是 也 low, that might be the issue, so bring it to `1` 为了 检查 if that was the issue. If it was not, continue 与 steps below 没有 changing it back 直到 the issue is solved.
- 检查 the 世界 difficulty: if you are trying to 生成 an hostile 生物 类型, it 不应 be peaceful!
- 移除 **any limitations**, 例如 `biome` and `conditions`, then see if it works
-- 检查 if 有ny mispelled word 任何地方, 例如:
    - the 生物 internal 名称
    - the 世界 名称
- If the RandomSpawn starts to work 之后 deleting all 条件, start to 添加 them back one by one, and see which one(s) caused the issue in the first place. If you are unable to understand why the 条件 thus found are problematic, ask for help over our [discord]
- If the randomspawn is 仍然 not working, continue debugging by taking the 动作 listed below, 基于 the randomspawn `Action`

### 添加 动作
- Make sure the 插件 spawning configurations are correctly set
  - (Below MM 5.6.1): the 配置 文件 is located at: `/MythicMobs/config.yml`
  - (MM 5.6.1 or above) the 配置 文件 is located at: `/MythicMobs/config/config-spawning.yml`
- Make sure you have 启用 `GeneraSpawnPoints` in the 配置 文件, or else the 添加 动作 不会 work
- Make sure you are in survival or adventure 模式, as 其他 gamemodes 不会 work
- If all of the above fails, ask for help over our [discord]

### REPLACE 动作
-- 检查 the 世界 difficulty: it 不应 be peaceful!
- Make sure the 世界 can 生成 monsters naturally (For instace, by making sure that the `doMobSpawning` gamerule is set to `true` and 其他 such things).
- 检查 区域([世界 Guard](https://dev.bukkit.org/projects/worldguard), [Grief Defender](https://www.spigotmc.org/resources/1-12-2-1-20-4-griefdefender-claim-插件-grief-prevention-protection.68900/) and so on) [标志](https://worldguard.enginehub.org/en/latest/区域/标志/#生物-触发-and-explosions) to see if the 区域 has any [标志 which 方块 生物 spawning](https://worldguard.enginehub.org/en/latest/区域/标志/#生物-触发-and-explosions)


<!-- LINKS -->
[discord]: https://www.mythiccraft.io/discord