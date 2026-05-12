# [THIS PAGE HAS BEEN MOVED!](/技能/机制)

效果 机制 are now part of the 机制 wiki page!

<!--
技能 效果 (or 效果 机制) are a special 类型 of 机制
具体 designed to create special 效果. These are called 仅
like any 其他 [技能 机制][] in your 生物 技能 列表, or 您可以
添加 them to your own 技能 and even combine them.

Most 效果 are able to 目标 两者都 实体 and 位置. You control
what your 效果 targets using a [目标选择器][].


# THIS PAGE IS CURRENTLY BEING MOVED OVER TO THE 机制 ONE, SOME LINKS MAY BECOME TEMPORARILY BROKEN DURING THIS PROCESS


## 语法
效果 不要 have any 选项. To call them, you 仅 call the的lot。
技能 **效果:名称**, 例如:

```yaml
    Skills:
    - effect:flames @target
    - effect:lightning @self
    - effect:ender @PlayersInRadius{r=20}
    - effect:ender @PlayersInRadius{r=20}
    - effect:particles{particle=reddust;color=#EE22CC;amount=10;speed=1;hS=0.15;vS=.15;audience=Target} @target
```


#### Audience
Audience arguments可以usedto 显示 the 效果 仅 to a specific group of 玩家, 而不是 the entire 服务器, by using the `audience=<audience type>` 属性 in an 效果 机制 and specifying an audience 类型 to use. This can be useful in preventing 也 many 粒子 from being displayed to 每个人 unnecessarily, and can reduce client-side lag to some extent。

The audience 类型 are:
- `self`/`caster`: the 施法者 of the 机制
- `nonSelfWorld`/`nonSelf`: every 玩家 in the 世界 其他 than the 施法者 of the 机制
- `target`: the 目标 of the 机制
- `world`: every 玩家 in the 世界
- `nearby`: every nearby 玩家
- `tracked`: every 玩家 who clients can render the 施法者
- `@Targeter`: every 玩家 that the 目标选择器 targets

> The 默认 值 is `nearby`

Of particular relevance is the `audience=@Targeter` 属性, that 允许 any 实体 目标选择器 to be used as the audience of the 效果
```yaml
    Skills:
    - effect:particles{particle=reddust;y=2;audience=@Owner} @self
```

## 效果
| 效果 机制 | Description |
|----------------------|-----------------------------------------------------------------------|
| [Atom][] | Creates electron-esque orbitals. |
| [BlackScreen][] | Blacks 移除 目标 screen 对于 持续时间 |
| [BlockMask][] | Temporarily masks a 方块 as a different 方块 |
| [BlockUnmask][] | Unmasks 方块 that 已被 masked |
| [BlockWave][] | Creates a wave of 方块 at the 目标 位置 |
| [BloodyScreen][] | Makes the 目标 screen glow red |
| [Ender][] | Causes the "Ender" 效果 |
| [EnderBeam][] | Creates the enderbeam 效果 at the 目标 (类似 End Crystals) |
| [Explosion][] | Causes an explosion 效果 |
| [Firework][] | Causes a firework explosion (当前 not working in most builds) |
| [Flames][] | Causes the 生物 生成器 flame 效果 |
| [Geyser][] | Creates a "geyser" of water or lava |
| [Glow][] | Gives the 目标 the glow 效果 with different colors (req. GlowAPI) |
| [GuardianBeam][] | Draw a guardian beam 在...之间 原点 and the 目标 |
| [ItemSpray][] | Sprays temporary 物品 在...周围 目标 |
| [闪电][] | Causes a 假闪电 strike |
| [粒子][] | Creates 粒子 效果 在...周围 目标 |
| [ParticleBox][] | Draws a box of 粒子 在...周围 目标 |
| [ParticleEquation][] | Generates 粒子 基于 equations |
| [ParticleLine][] | Draws a line of 粒子 效果 to the 目标 |
| [ParticleLine Helix][] | Draws a line based helix 效果 |
| [ParticleLine Ring][] | Draws a 粒子 ring connected by lines |
| [ParticleOrbital][] | Draws orbiting 粒子 效果 在...周围 目标 |
| [ParticleRing][] | Draws a ring of 粒子 在...周围 目标 |
| [ParticleSphere][] | Draws a sphere of 粒子 在...周围 目标 |
| [ParticleTornado][] | Draws a persistent "tornado" of 粒子 at the 目标 |
| [PlayAnimation][] | Forces the 实体 to play an animation |
| [Recoil][] | Kicks the 目标 screen |
| [Skybox][] | Alters the 目标 skybox |
| [Smoke][] | Creates a puff of smoke |
| [Smoke Swirl][] | Creates a persistent "swirl" of smoke |
| [Sound][]    | [Sound][] | Plays a sound 效果 from 两者都 原版 Minecraft and resource 包 |
| [Spin][] | Causes the 生物 to spin |
| [StopSound][] | Stops a sound 效果 from playing |
| [ThunderLevel][] | Creates a rainless storm for 玩家 client side (per 玩家) |
| [TotemOfUndying][] | Plays the 效果 of a 玩家 resurrecting |


  [技能 机制]: /技能/机制/
  [目标选择器]: /技能/目标选择器/
  [Atom]: /技能/机制/atom
  [BlackScreen]: /技能/机制/blackscreen
  [BlockMask]: /技能/机制/blockmask
  [BlockUnmask]: /技能/机制/blockunmask
  [BlockWave]: /技能/机制/blockwave
  [BloodyScreen]: /技能/机制/bloodyscreen
  [Ender]: /技能/机制/ender
  [EnderBeam]: /技能/机制/enderbeam
  [Explosion]: /技能/机制/FakeExplosion
  [Firework]: /技能/效果/firework
  [Flames]: /技能/效果/flames
  [Geyser]: /技能/效果/geyser
  [Glow]: /技能/机制/glow
  [GuardianBeam]: /效果/guardianbeam
  [ItemSpray]: /技能/效果/itemspray
  [闪电]: /技能/机制/FakeLightning
  [粒子]: /技能/机制/粒子
  [ParticleBox]: /技能/效果/particlebox
  [ParticleEquation]: /技能/效果/particleequation
  [ParticleLine]: /技能/效果/particleline
  [ParticleLine Helix]: /技能/效果/particlelinehelix
  [ParticleLine Ring]: /技能/效果/particlelinering
  [ParticleOrbital]: /技能/效果/particleorbital
  [ParticleRing]: /技能/效果/particlering
  [ParticleSphere]: /技能/效果/particlesphere
  [ParticleTornado]: /技能/效果/particletornado
  [Recoil]: /技能/效果/recoil
  [Skybox]: /技能/效果/skybox
  [Smoke]: /技能/效果/smoke
  [Smoke Swirl]: /技能/效果/smokeswirl
  [Sound]: /技能/效果/sound
  [Spin]: /技能/效果/spin
  [StopSound]: /技能/效果/stopsound
  [ThunderLevel]: /技能/效果/thunderlevel
  [TotemOfUndying]: /技能/效果/totemOfUndying
  [Atom]: /技能/机制/atom
  [ParticleVortex]: /技能/效果/particlevortex
  [DNA]: /技能/效果/dna
  [PlayAnimation]: /技能/效果/playanimation
-->