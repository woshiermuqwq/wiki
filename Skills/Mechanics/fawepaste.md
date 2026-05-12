## 描述
Pastes a Schematic using the FAWE Plugin found here: [FAWE](https://www.spigotmc.org/resources/fast-async-worldedit.13932/)

You must create a `Schematics` folder in your Mythic生物 directory and put the schematics you will use inside that folder.<br>
If the schematic defined in the 技能 is not found inside mm's `Schematics` folder, FAWE's and WE's will be then checked for its presence

> **This is a [Premium-Only] 技能!**


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| schematic | s         | Which schematic to load                                              |         |
| pasteID   | pid, id   | The paste's id. 可用于 undo the paste via the [undoPaste] 技能 |   |
| pasteAir  | air, a    | Should air be pasted?                                                | false   |
| xOffset   | x, xo     | The X offset of pasting the Schematic from the 目标                | 0       |
| yOffset   | y, yo     | The Y offset of pasting the Schematic from the 目标                | 0       |
| zOffset   | z, zo     | The Z offset of pasting the Schematic from the 目标                | 0       |
| rotation  | rot, r    | the rotation of the pasted schematic, in degrees                     | 0       |
| center    | c         | 是否 to center the schematic                               | true    |
| chestDropTable | chests,cdt | Which Mythic生物 掉落 Tables to supply the chests within the Schematic with |
| trapchestDropTable | trapchests, tcdt | Which Mythic生物 掉落 Tables to supply the Trapped Chests within the Schematic with                                                                      |         |
| blocksPerTick  | bpt  | The number of blocks that are placed every tick. If 0, all of the blocks will be pasted in a single tick | 0       |
| duration  | d         | If greater than 0, will undo the paste operation after that amount of ticks has elapsed | 0 |

## 示例
```yaml
  Skills:
  - fawePaste{schematic=deserttempleiron.schem;y=6;air=true;chestDropTable=IronDropTable} @origin
```


## 别名
- [x] pasteSchematic
- [x] schematicPaste
- [x] wePaste

<!-- LINKS -->
[Premium-Only]: Premium-Features
[undoPaste]: /Skills/mechanics/undopaste


<!--TAGS-->
<!--tag:World-->
<!--tag:Premium-Only-->
