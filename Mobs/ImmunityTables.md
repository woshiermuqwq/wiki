免疫表 allow a 生物 to track each 玩家 伤害 and assigns NoDamageTicks 单独, so that the 生物 can 仅 take 伤害 every half second PER 玩家 而不是 TOTAL. Essentially, they allow for multiple 玩家 to hit a 生物 and 仍然 have all their 伤害 register.

**Enabling 免疫表**

Turning on 免疫表 for a 生物 is easy. Just 添加 Modules.ImmunityTable: true to your 生物, like so:

```yaml
BigHealthBoss:
  Type: pig_zombie
  Display: '&6Hungry Hungry Piggy Zombie'
  Health: 20000
  Modules:
    ImmunityTable: true
  Options:
    NoDamageTicks: 10
```

That it!

免疫表 will take the NoDamageTicks 选项 into account if you decide to change it, 但是 it 不是 necessary and将useMinecraft 的 默认 of 10 if one 不是 specified。