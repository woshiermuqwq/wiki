## ⚠️ 警告：一旦生成器配置文件加载到运行中的服务器上，只能通过游戏内指令编辑。如果你想在文本编辑器中编辑已经加载的生成器配置文件，必须先停止服务器再进行编辑。

生成器允许你定义世界中生成自定义生物的特定点位。它们可配合多种有用的选项使用，如：条件、内置计时器、冷却和预热。

你可以通过[指令](/commands and permissions)在游戏中直接创建生成器，或在文件夹 */MythicMobs/Spawners* 中创建配置文件。

### 生成器的优点

-   不需要启用自然生物生成即可工作。
-   对生成实现有更多控制，可精确指定每只生物在何时何地生成。
-   支持计时器、牵引等功能。
-   非常适合填充小型竞技场或地下城。

### 生成器的缺点

-   设置可能耗时，尤其是大型实现。
-   若没有提前规划好，管理可能变得非常困难。
-   生物需要合理配置。

示例配置
--------------
```yaml
SpawnerName:
  MobName: mobTypeName
  World: worldname
  SpawnerGroup: GroupName
  X: 0
  Y: 0
  Z: 0
  Radius: 0
  RadiusY: 0
  UseTimer: true
  MaxMobs: 1
  MobLevel: 1
  MobsPerSpawn: 1
  Cooldown: 0
  CooldownTimer: 0
  Warmup: 0
  WarmupTimer: 0
  CheckForPlayers: true
  ActivationRange: 40
  LeashRange: 32
  HealOnLeash: false
  ResetThreatOnLeash: false
  ShowFlames: false
  Breakable: false
  Conditions: []
  ActiveMobs: 1
```
选项
-------
| 选项             | 描述                      |用法                       |默认值|
|--------------------------|-----------------------|-----------------------|-----------------------|
|**mobtype: &lt;mobtype&gt;** 或 **mobname: &lt;mobtype&gt;:**|此生成器将生成的生物类型。只能设置为内部的 MythicMobs 生物。支持带权重的生物数组。|/mm s set [名称] mobtype 25%Mob1,25%Mob2,50%mMob2| 无 |
|**world: &lt;worldname&gt;:**|生成器所在世界的文件名|/mm s set \<名称\> world \<世界\>|创建时的世界|
|**spawnergroup: &lt;组名&gt;**|设置生成器的组名。对于大型配置（如填充地下城），你可以将所有生成器分组，然后一次性更改它们的所有设置。|/mm s set g:\<组\> \<设置\> \<值\>|无|
|**X: / Y: / Z:**|生成器的坐标||创建位置|
|**radius: &lt;数字&gt;**|生物可在生成器周围生成的半径。|/mm s set \<名称\> radius \<半径\>|0|
|**radiusY: &lt;数字&gt;**|生物可在生成器上方或下方生成的垂直半径|/mm s set \<名称\> radiusy \<半径\>|0|
|**usetimer: &lt;true/false&gt;**|生成器是否按计时器触发。|/mm s set \<名称\> usetimer <true/false>|True|
|**maxmobs: &lt;数字&gt;**|此生成器在世界中同时存在的最大生物数量。**必须大于或等于 mobsperspawn**|/mm s set \<名称\> maxmobs \<数量\>|1|
|**moblevel: &lt;数字&gt;**|此生成器生成生物时应使用的等级。生物必须在配置中设置了等级才能生效。|/mm s set \<名称\> moblevel \<等级\>|1|
|**mobsperspawn: &lt;数字&gt;**|每次生成器触发时生成的生物数量。|/mm s set <名称> mobsperspawn \<数量\>|1|
|**cooldown: &lt;数字&gt;**|生成器在生成生物后等待下一次生成的时间（秒）。|/mm s set <名称> cooldown <时间>|0|
|**cooldowntimer: &lt;数字&gt;**|由生成器自动设置，用于在服务器重启后衔接冷却时间。|*不需要用户设置*||
|**warmup: &lt;数字&gt;**|生成器开始冷却前的等待时间（秒）。预热在激活时开始，且在达到 maxmobs 并有生物死亡时触发。|/mm s set <名称> warmup <持续时间>|0|
|**warmuptimer: &lt;数字&gt;**|由生成器自动设置，用于在服务器重启后衔接预热时间。|*不需要用户设置*||
|**checkforplayers: &lt;true/false&gt;**|是否需要有玩家在附近生成器才会"激活"||true（推荐用于性能优化）|
|**activationrange: &lt;数字&gt;**|玩家必须处于多远半径内才能使生成器激活。||40 方块|
|**leashrange: &lt;数字&gt;**|生物可移动的最大距离，超出后会被传送回生成点。|/mm s set \<名称\> leashrange \<距离\>|-1（无限制）|
|**healonleash: &lt;true/false&gt;**|当生物被牵引回生成器时是否回复满血|/mm s set \<名称\> healonleash <true/false>|false|
|**resetthreatonleash: &lt;true/false&gt;**|当生物被传送回生成器时重置仇恨表（如果启用）||false|
|**showflames: &lt;true/false&gt;**|设为 true 可在生成器周围显示火焰。|/mm s set \<名称\> showflames <true/false>|false|
|**breakable: &lt;true/false&gt;**|决定生成器是否随其所在的方块被破坏而一起破坏||false|
|**conditions:**|生成器激活所需满足的条件。|/mm s addcondition \<名称\> \<条件\> \<操作\>|无|
| **SpawnConditions**| 生物尝试生成的生成位置所需满足的条件 || 无 |
|**activemobs: &lt;数字&gt;**|用于跟踪连接至（由此生成器生成的）生物的数量。|*不需要用户设置*||

**关于生成时序的说明：** ```时序：预热 -> 生成生物 -> 冷却 -> 生成生物*>```
