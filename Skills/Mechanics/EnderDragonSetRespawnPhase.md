## 描述
Sets the EnderDragon respawn phase if an EnderDragon battle is going on in the target location's dimension


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| phase     | p         | The phase to set                                                     | NONE<!--type:DragonBattleRespawnPhase--> |

### Phase Attribute
The possible values of the phase attribute (at the time of writing) are listed below.  
The most up to date list 可以 found in the [javadoc](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/boss/DragonBattle.RespawnPhase.html).  

| Phase                 | Description                                                                    |
|-----------------------|--------------------------------------------------------------------------------|
| END                   | The end of the respawn sequence                                                |
| NONE                  | No respawn is in progress                                                      |
| PREPARING_TO_SUMMON_PILLARS | The crystal beams remain directed upwards                                |
| START                 | The crystal beams are directed upwards into the sky                            |
| SUMMONING_DRAGON      | All crystals (including those from the pillars) are aimed towards the sky      |
| SUMMONING_PILLARS     | The crystal beams are directed from pillar to pillar, regenerating their crystals if necessary   |


## 示例
```yaml
  Skills:
  - enderDragonSetRespawnPhase{p=SUMMONING_DRAGON} @selflocation
```


## 别名
- [x] setEnderDragonRespawnPhase
