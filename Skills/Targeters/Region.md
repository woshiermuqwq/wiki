## 描述
Special 目标选择器 to 目标 a 区域. Only works with specific 机制


## 属性
| 属性 | 别名 | Description | 默认 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| min | | The 位置 of the first point | 0,0,0 |
| max | | The 位置 of the second point | 0,0,0 |
| 世界 | | The 世界 the 区域 is in | `<caster.l.w>` |

### Min and Max 属性
The returned 区域 将 the one contained between those two points


## 示例
```yaml
  Skills:
  - worldEditReplace{from=STONE;to=AIR} @Region{min=0,0,0;max=100,100,100;world=resources}
```