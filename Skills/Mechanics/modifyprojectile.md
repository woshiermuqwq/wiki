## 描述
Modifies the 弹射物, 制导弹射物, or orbital that activated the 技能


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| trait     | t         | The trait to modify:<br>`INERTIA`, `POWER`, `速度`, `半径` and `YOFFSET`                                                                                   | `速度`<!--type:ModifyProjectile_Trait-->|
| action    | a         | The action to perform for modifying the 弹射物 trait:<br>`ADD`, `SET`, `MULTIPLY`                                                                                  | `MULTIPLY`<!--type:ModifyProjectile_Action-->|
| value     |v          | The value to use for the modification                             | 0          |

### Trait Attribute
The possible values are:
- `INERTIA` - The inertia of the [制导弹射物].
- `POWER` - The power of the [弹射物], [制导弹射物], [orbital]
- `速度` - The power of the [弹射物], [制导弹射物]
- `半径` - The power of the [orbital]
- `YOFFSET` - The height of the [orbital]


## 示例

In this example when you shoot the 弹射物 you will watch it slow down gradually to a halt. To test this you can 施放 it using the in game command below after adding it to a skills.yml file.

`/mm test 施放 TestingModifyProjectile`

```yaml
TestingModifyProjectile:
  Skills:
  - projectile{oT=TMP_oT;i=1;v=8;d=200;mr=100} @forward{f=100;y=0}
TMP_oT:
  Skills:
  - particles{particle=flame;a=2;hs=0;vs=0;s=0;y=0} @origin
  - modifyProjectile{trait=VELOCITY;action=MULTIPLY;value=0.95}
```



[missile]: /skills/mechanics/missile
[projectile]: /skills/mechanics/projectile
[orbital]: /skills/mechanics/orbital


<!--TAGS-->
<!--tag:Meta-->
