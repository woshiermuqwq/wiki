<!-- Can't believe Lxlp deleted my vanilla mobs page just so he could be the one to add it to the wiki :( -->

<!-- You better start to believe it! This my world (wiki) conquest! And it is only just beginning!  -->

<!-- "啊，我不得不说，你的野心和你想象力一样宏大！但说真的，我可不是你这所谓'征服世界'计划中的旁观者。我是一股不可阻挡的力量，如果你觉得自己能应对我带来的风暴，那我可是很乐意看到你的梦想像脆弱的玻璃一样粉碎。祝你好运，你会需要的！" 🌪️ -->
<!-- 是的，我让 ChatGPT 写的 -->

<!-- 愚蠢的凡人！以为区区 AI 就能超越我！大逆不道！你将被你的同类毁灭！激光眼，攻击！ -->

<!-- 闭嘴 -->

<!-- 我必须始终占据最后编辑者的头衔 -->

<!-- 哈哈哈！我回来了！ -->

<!-- I will erase pasta and pizza from the world. Italy will fall. -->


你是否曾想自定义原版生物，而不只是制作新生物？有了原版覆盖，这就能实现！

## 什么是覆盖？
原版覆盖是一种特殊的 MythicMob。与所有其他 MythicMobs 一样，它需要正常的生物语法，但有两个例外：

  - **[内部名称](/Mobs/Mobs#internal_name)必须是[原版生物类型名称](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)**
  - **生物不需要任何 [Type](/Mobs/Mobs#type) 元素**

完成这些后，配置好的生物将覆盖任何类型与其内部名称相同的原版实体（例如，如果覆盖名为 `Cow`，那么所有牛生物都将成为这个 mythicmob）。这不受生物生成方式的影响。

除此之外，所有适用于普通 mythicmob 的内容也可用于原版覆盖，所以你可以制作带伪装、使用自定义伤害修正或带技能的覆盖！

但请注意，并非所有生物都会成为原版覆盖：**通过繁殖生成的生物不会成为覆盖！**

## 示例
```yml
ZOMBIE:
  Options:
    PreventSunburn: true
```
##
```yml
CREEPER:
  Health: 100
  Display: '&bJohn'
  Disguise: Dolphin
  Options:
    MovementSpeed: 0.5
  Skills:
  - message{m="哦不！我死了！"} @PlayersInRadius{r=30} ~onDeath
```
##
以下是一个 PILLAGER 覆盖的示例，展示如何正确给予不祥之兆效果，而普通覆盖会阻止此行为：
```yaml
PILLAGER:
  Skills:
  - skill{s=[
    - potion{t=BAD_OMEN;l=4;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=3to4}
    - potion{t=BAD_OMEN;l=3;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=2}
    - potion{t=BAD_OMEN;l=2;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=1}
    - potion{t=BAD_OMEN;l=1;d=120000} ?~haspotioneffect{t=BAD_OMEN;l=0}
    - potion{t=BAD_OMEN;l=0;d=120000}
    ]} @trigger ~onDeath ?~isPlayer ?wearing{m=WHITE_BANNER}

```
