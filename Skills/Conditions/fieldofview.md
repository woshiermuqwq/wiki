## 描述
检测目标是否在施法者视角的给定角度范围内。

## 属性
| 属性       | 别名   | 描述                     | 默认值 |
| ---------- | ------ | ------------------------ | ------ |
| angle      | a      | 要检测的视野角度          | 90     |
| rotation   | r      | 旋转检测的视野            | 0      |


## 示例
```yaml
  TargetConditions:
  - fieldofview{angle=90} false
```
此条件会过滤掉所有在施法者 90 度视野范围内的目标。

```yaml
  TargetConditions:
  - fieldofview{angle=90} true
```
此条件只允许在施法者 90 度视野范围内的生物被锁定。

## 别名
- [x] infieldofview
- [x] fov
