## 描述
Draws a guardian beam between the 原点 and the 目标.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| duration  | d, maxduration, md | The time (in ticks) for which the effect will be active     | 400     |
| interval  | int, i    | How often the effect will tick                                       | 1       |
| startYOffset | syo    | The starting y offset of the beam                                    | 1       |
| targetYOffset | tyo    | The 目标 y offset of the beam                                    | 0       |
| fromOrigin | fo       | Whether to make the effect start from the @原点 instead of from @self| false |
| onstartskill | onstart, os | Metaskill to execute when the effect starts                     |<!--type:Metaskill-->|
| ontickskill | ontick, ot | Metaskill to execute each interval tick                           |<!--type:Metaskill-->|
| onendskill | onend, oe | Metaskill to execute when the effect ends                           |<!--type:Metaskill-->|


## 示例
```yaml
Guardian_Beam:
   Skills:
   - guardianbeam{d=200;i=1;syo=1;fromOrigin=false;oS=AStartingSkill;oT=ATickingSkill;oE=AEndingSkill} @Target
```


## 别名
- [x] effect:guardianbeam
- [x] effect:beam
- [x] e:guardianbeam
- [x] e:beam



<!--TAGS-->
<!--tag:Effect-->