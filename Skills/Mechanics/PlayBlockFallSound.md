## 描述
Plays the target block's falling sound.  

> **This is a [Paper-Only] 机制!**


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| pitch     | p         | 音效的音高. Can be between 0.01 and 2.0                  | 1.0     |
| volume    | v         | 音效的音量.                                             | 1.0     |

### Volume Attribute
The “volume” attribute doesn't define the percentage of the loudness of the sound, but rather determines how far (measured in blocks) the sound 可以 heard at maximum volume.  

The formula for this is `v * 16 = max volume distance`. For example if you use “1” 对于volume attribute, the sound 可以 heard at maximum volume in a radius of 16 blocks around the source. If you used “20” however, the sound 可以 heard at maximum volume in a 320 block radius! (20 * 16)


## 示例
```yaml
  Skills:
  - blockfallsound @targetlocation
```


## 别名
- [x] blockfallsound


<!-- LINKS -->
[Paper-Only]: https://papermc.io/downloads/all


<!--TAGS-->
<!--tag:Effect:Sound-->
<!--tag:Paper-Only-->
