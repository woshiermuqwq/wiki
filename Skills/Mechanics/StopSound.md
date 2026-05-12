## 描述
Stops a sound from playing from either the vanilla game or a resource pack 对于targeted entity. A good list of sounds 可以 found [here](https://minecraft.wiki/w/Sounds.json#sound_events). Use the “sound event” column.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| sound     | s         | Sound to stop playing                         | entity.zombie.attack_iron_door<!--type:Sound--> |
| soundcategory | source, sc, category | The category at which the sound is played, useful for resourcepacks | MASTER<!--type:SoundCategory-->|

### SoundCategory Attribute
A list of sound categories 可以 found [here](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/SoundCategory.html).


## 示例
```yaml
SilenceEndermanSkill:
  Skills:
  - stopsound{s=entity.enderman.scream} @PIR{r=10}
```


## 别名
- [x] effect:stopsound
- [x] e:ss
- [x] ss


<!--TAGS-->
<!--tag:Effect:Sound-->
