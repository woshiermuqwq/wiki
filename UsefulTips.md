以下是一些可能有用的技巧列表。

目录：

[[_TOC_]]

## 通用规则
- 绝对不要在创造模式下测试任何东西
- 始终深入阅读你所用功能的 Wiki 页面
- 始终保持插件更新
- 确保你运行在受支持的版本上。可通过 `/mm version` 检查
- 使用 ChatGPT 获取配置是个*真的非常糟糕*的主意。绝对不要这样做。

## 生物

### 覆盖
<details><summary>我的 PILLAGER 覆盖没有给予不祥之兆效果</summary>
<br>
这是一个常见问题。要修复它，请考虑在你的 PILLAGER 生物覆盖中添加以下技能：
&emsp;

```yaml
  Skills:
  - skill{s=[
    - potion{t=BAD_OMEN;l=4;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=3to4}
    - potion{t=BAD_OMEN;l=3;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=2}
    - potion{t=BAD_OMEN;l=2;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=1}
    - potion{t=BAD_OMEN;l=1;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=0}
    - potion{t=BAD_OMEN;l=0;d=120000}
    ]} @trigger ~onDeath ?~isPlayer ?wearing{m=WHITE_BANNER}
```
</details>


## 技能

### 聊天消息
<details><summary>我想在生物生成时警告所有玩家</summary>
[占位符 Wiki 页面](/Skills/Placeholders#examples)包含这样一个示例。
</details>


## 物品



## 掉落与掉落表

### 多份掉落
<details><summary>让参与战斗的每个玩家都获得掉落</summary>
<br>
可以通过启用生物的[仇恨表模块](/Mobs/ThreatTables)并在生物死亡时执行以下机制来实现：
&emsp;

```yaml
  Skills:
  - dropitem{i=droptable_name} @ThreatTablePlayers ~onDeath
```

这样，生物将对仇恨表中的每个玩家掉落名为 `droptable_name` 的掉落表，有效地向每个参与战斗的玩家分发掉落。
</details>

<details><summary>仅让造成伤害最多的 X 个玩家获得掉落</summary>
<br>
可以通过启用生物的[仇恨表模块](/Mobs/ThreatTables)并在生物死亡时执行以下机制来实现：
&emsp;

```yaml
  Skills:
  - dropitem{i=droptable_name} @ThreatTablePlayers{limit=X;sort=HIGHEST_THREAT} ~onDeath
```

其中 X 是你希望获得掉落的顶尖玩家数量。

虽然这种方法不一定精确（仇恨可以衰减等因素），但实现极其简单且精确度在可接受的范围内。
</details>

### 特定掉落
<details><summary>仅让造成伤害最多的玩家获得掉落</summary>
<br>
可以通过启用生物的[仇恨表模块](/Mobs/ThreatTables)并在生物死亡时执行以下机制来实现：
&emsp;

```yaml
  Skills:
  - dropitem{i=droptable_name} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT} ~onDeath
```

虽然这种方法不一定精确（仇恨可以衰减等因素），但实现极其简单且精确度在可接受的范围内。
</details>



<details><summary>让造成伤害最多的前 X 个玩家各自获得特定掉落</summary>
<br>
可以通过启用生物的[仇恨表模块](/Mobs/ThreatTables)并在生物死亡时执行以下机制来实现：

```yaml
  Skills:
  - skill{s=[
    - skill{s=[
      - dropitem{i=droptable_name_1}
      - threat{mode=reset}
      ]} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT}
    - skill{s=[
      - dropitem{i=droptable_name_2}
      - threat{mode=reset}
      ]} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT}
    - skill{s=[
      - dropitem{i=droptable_name_3}
      - threat{mode=reset}
      ]} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT}
    ]} ~onDeath
```

这样，掉落表 `droptable_name_1` 将给予造成伤害最多的玩家，`droptable_name_2` 给予第二多的玩家，以此类推。

这是因为每次调用内联技能
```yaml
    - skill{s=[
      - dropitem{i=droptable_name_1}
      - threat{mode=reset}
      ]} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT}
```
时，一个掉落表被给予仇恨最高的目标的，然后该目标的仇恨被清除，使"下一个"目标被视为最高仇恨者。
因此，要给第 10 名而不是前 3 名分发特定掉落，只需重复那段代码即可。

如果你有 MythicMobs Premium，还可以这样做
```yaml
  Skills:
  - skill{s=[
    - skill{s=[
      - dropitem{i=droptable_name_<skill.var.itr>}
      - threat{mode=reset}
      ]} @ThreatTablePlayers{limit=1;sort=HIGHEST_THREAT}
    ];repeat=X;repeatInterval=1} ~onDeath
```
也能实现，其中 X 是你要给予奖励的玩家数量减一（所以如果是前 10 名，X 就是 9），每个玩家将获得名为 `droptable_name_Y` 的掉落表，其中 Y 是他们在"排行榜"中的名次（第一名获得 droptable_name_1，第二名获得 droptable_name_2，以此类推）。

</details>



<details><summary>向最后击中生物的玩家掉落物品</summary>
<br>
这种情况下，你需要在生物每次受击时设置一个变量，条件是触发者是玩家。然后在生物死亡时，使用 UUID 目标选择器向变量记录的玩家掉落特定物品。这样，即使生物因其他原因死亡（火焰伤害、摔落伤害等），始终会有一个玩家被选中获得掉落，因此比在死亡时直接对触发者掉落物品更加稳定。
&emsp;

```yaml
  Skills:
  - setvariable{var=caster.lastplayer;type=STRING;val=<trigger.uuid>} @self ~onDamaged ?~isPlayer
  - dropitem{...} @UUID{u="<caster.var.lastplayer>"} ~onDeath ?variableisset{var=caster.lastplayer}
```
</details>


## 生成

### 随机生成
<details><summary>使用 ADD 生成操作的生物不生成</summary>
你必须在插件的配置文件中启用 `GenerateSpawnPoints`。
你不能处于创造模式或旁观模式。
</details>
