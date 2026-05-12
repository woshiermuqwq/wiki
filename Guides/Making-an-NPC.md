**难度：初学者**

使用一些基本技巧，你可以通过 MythicMobs 创建高灵活性的 NPC。基本思路是创建一个无 AI/移动且不会消失的生物，然后可以为其附加各种技能和技能，如消息、指令或任何你能想到的技能。

# 第一步 - 基础 NPC

第一步是创建你的生物文件，放在任何位置都可以，本例中我们创建一个 NPC 子文件夹。

使用以下生物为基础，我们可以制作一个简单站立的 NPC。我们使用 [LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/) 让生物看起来像一个玩家。

`plugins/MythicMobs/Mobs/NPC/Steve.yml`

```yaml
NPC_Steve:
  Type: INTERACTION
  Display: 'Steve the Guide'
  Disguise: Player <Inherit> setSkin Steve setDynamicName true
  Options:
    AlwaysShowName: true
    Despawn: persistent
```

- `NPC_Steve` 这是用来生成 NPC 的名称。/mm m spawn NPC_Steve
- `Type: INTERACTION` 你可以使用任何类型，但我们使用交互实体，因为它没有 AI、没有声音等。
- `Display: 'Steve the Guide'` 将显示在 NPC 头顶的内容。
- `Disguise: Player <Inherit> setSkin Steve setDynamicName true` 这使你的 NPC 看起来像玩家。你可以将 "Steve" 替换为任何你想使用的玩家皮肤。必须保留 setDynamicName 为 true，这样 NPC 才能使用 Display 设置。`<Inherit>`（区分大小写）占位符使 NPC 显示其 `Display:` 名称。关于使用自定义皮肤的更多信息，[请阅读此处](/Mobs/Disguises)。
- `AlwaysShowName: true` 让铭牌始终显示在 NPC 上方。
- `Despawn: persistent` 使你的 NPC 在重载、重启和区块卸载时保持存在。


# 第二步 - 添加消息和指令

你可以使用 [Message](/Skills/mechanics/message) 和 [Command](/Skills/mechanics/command) 技能为 NPC 添加消息或指令。在本指南中，我们将使用 @trigger 和 onInteract，使右键点击 NPC 的用户看到消息或运行指令。测试时请确保处于生存模式，因为创造模式玩家无法被定位。

### 消息
此示例在玩家右键点击 NPC 时向其发送一条消息。我们添加了通用属性 `cd=3`，使其在两次点击之间有一个 3 秒的冷却。
```yaml
  Skills:
  - message{m=&b欢迎来到 Hypixel &a<trigger.name>&b!;cd=3} @trigger ~onInteract
```

### 指令
此示例将为右键点击 NPC 的玩家打开一个 DeluxeMenus 菜单。
```yaml
  Skills:
  - command{c="dm open shops-blocks <trigger.name>"} @trigger ~onInteract
```

你可以为 NPC 添加任意数量的技能或技能，不限于消息和指令。你可以运行任何技能和任何元技能。


# 第三步 - ModelEngine（可选）

如果你希望 NPC 使用 ModelEngine 模型，可以移除伪装行，改为使用两个技能来应用模型。我们使用 onSpawn 和 onLoad 确保模型始终应用到生物上，即使重启后也不会丢失。

你还需要在模型中添加一个铭牌骨骼，以便在模型上方显示名称。可以通过在 Blockbench 中打开模型、创建一个空骨骼并命名为 `tag_name`，然后将编辑好的模型上传到 Blueprints 文件夹，再执行 `/meg reload` 来实现。

 `plugins/MythicMobs/Mobs/NPC/Steve.yml`
```yaml
NPC_Steve:
  Type: INTERACTION
  Display: 'Steve'
  Options:
    AlwaysShowName: true
    Collidable: false
    Despawn: persistent
  Skills:
  - model{m=SteveModel;n=name;save=true} @self ~onSpawn
```

model 技能的属性说明：
- `m=SteveModel` 这里填写你的模型名称，例如我们的文件路径为 `plugins/ModelEngine/Blueprints/SteveModel.bbmodel`
- `n=name` 这是创建的[铭牌骨骼](https://git.mythiccraft.io/mythiccraft/model-engine-4/-/wikis/Modeling/Bone-Behaviors#nametag)名称。
- `save=true` 告诉 ModelEngine 该模型应当被保存，即使跨重启也保留。


# 第四步 - 生成 NPC

现在你可以使用 `/mm reload` 重载修改后的文件，并将 NPC 添加到服务器中。只需站在你想要 NPC 出现的位置，使用 `/mm m spawn NPC_Steve`。

现在你就拥有了一个由 MythicMobs 创建的 NPC！
