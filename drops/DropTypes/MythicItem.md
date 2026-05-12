## 描述
掉落一个 [Mythic 物品](/Items/Items)


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| level     | lvl, l    | 物品的等级                                                |         |
| lootsplosion | lootsplosionenabled, ls | 是否启用战利品爆炸效果              |         |
| itemvfx   | itemvfxenabled, iv | 是否启用物品视觉特效                          |         |
| itemvfxmaterial | itemvfxmaterial, ivm | 物品视觉特效的材质                        |         |
| vfxdata   | vfxd      | 视觉特效材质的自定义模型数据               |         |
| vfxcolor  | vfxc, color | 物品视觉特效的颜色                                          |         |
| hologramname | hologramnameenabled, hn | 是否启用掉落的全息名称  |         |
| clientsidedrops | clientsidedropsenabled, csd | 是否启用客户端掉落  |         |
| itemglowcolor | glowcolor, gc | 掉落物的发光颜色                                   |         |
| itembeamcolor | beamColor, bc | 掉落物的光束颜色                                   |         |
| billboarding | billboard, bill | 掉落物的朝向                                   |         |
| brightness | bright, b | 掉落物的亮度                                              |         |


## 示例
```yaml
  Drops:
  - SuperCoolItem{lootsplosion=true} 2 0.5
```
