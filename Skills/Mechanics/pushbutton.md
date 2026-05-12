## 描述
Pushes a button 在supplied coordinates.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| x         |           | The X coordinate of the button                                       | 0       |
| y         |           | The Y coordinate of the button                                       | 0       |
| z         |           | The Z coordinate of the button                                       | 0       |
| location  | loc, l    | Location of the action, in a `x,y,z` syntax. If set, other attributes are ignored     |           |


## 示例
```yaml
HitSecretButton:
  Skills:
  - pushbutton{x=15;y=67;z=-213}
```


## 别名
- [x] buttonpush


<!--TAGS-->
<!--tag:World-->
