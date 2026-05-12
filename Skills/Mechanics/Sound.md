## 描述
播放音效 from either the vanilla game or a resource pack 在targeted entity or location. An extensive list of sounds 可以 found [here](https://misode.github.io/sounds/). Using multiple sounds stacked together can give the impression of an entirely new sound.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| sound     | s         | 要播放的音效                             | entity.zombie.attack_iron_door<!--type:Sound-->|
| pitch     | p         | 音效的音高. Can be between 0.01 and 2.0                  | 1.0     |
| volume    | v         | 音效的音量.                                             | 1.0     |
| radius    | r         | The radius in which the sound 将会 heard                      | `volume`*16 |
| soundcategory | category, sc | The category at which the sound is played, useful for resourcepacks | MASTER<!--type:SoundCategory-->|
| audience  |           | The [audience] of the effect                                         | world<!--type:Audience--> |

### SoundCategory Attribute
A list of sound categories 可以 found [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/SoundCategory.html).

### Volume Attribute
The “volume” attribute, while above the value of "1", doesn't define the percentage of the loudness of the sound, but rather determines how far (measured in blocks) the sound 可以 heard at maximum volume.

The formula for this is v * 16 = maxvolume distance. For example if you use “1” 对于volume attribute, the sound 可以 heard at maximum volume in a radius of 16 blocks around the source. If you used “20” however, the sound 可以 heard at maximum volume in a 320 block radius! (20 * 16)

While the value is between 0 and 1, the sound is still played in a 16 blocks radius, but with diminished volume, with 0.1 being 10% of normal volume, 0.4 being 40% of normal volume and so on


## 示例
```yaml
EndermanAttack:
  Skills:
  - sound{s=entity.enderman.scream} @self
```
##
The below example plays a sound from your resource pack. A good guide on adding custom sounds 可以 found [here](https://mcmodels.net/guides/4-sounds).
```yaml
BossSoundEffect:
  Skills:
  - sound{s=yoursound:example.sound.name_1} @self
```


## 别名
- [x] effect:sound
- [x] s
- [x] e:sound
- [x] e:s


<!-- LINKS -->
[audience]: /Skills/Audience


<!--TAGS-->
<!--tag:Effect:Sound-->
