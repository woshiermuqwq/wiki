## 描述  
Plays the 目标 block's step sound (The sound played when an entity walks on it).  

> **This is a [Paper-Only] 技能!**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| 俯仰角(pitch)     | p         | 音效的音高. Can be between 0.01 and 2.0                  | 1.0     |
| volume    | v         | 音效的音量.                                             | 1.0     |

### Volume Attribute
The “volume” attribute doesn't define the percentage of the loudness of the sound, but rather determines how far (measured in blocks) the sound can be heard at maximum volume.  

The formula for this is `v * 16 = max volume distance`. For example if you use “1” for the volume attribute, the sound can be heard at maximum volume in a 半径 of 16 blocks around the source. If you used “20” however, the sound can be heard at maximum volume in a 320 block 半径! (20 * 16)


## Example
```yaml
  Skills:
  - blockstepsound @targetlocation
```

## 别名
- [x] blockstepsound


<!-- LINKS -->
[Paper-Only]: https://papermc.io/downloads/all


<!--TAGS-->
<!--tag:Effect:Sound-->
<!--tag:Paper-Only-->
