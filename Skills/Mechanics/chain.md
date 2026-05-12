## 描述
Chain allows you to make skills that bounce between 目标, like a
"chain lightning" type skill.

Bounce条件 are evaluated after each "bounce" of the skill. With
the example, if someone were on the other side of a wall from the 生物
but you were standing in the doorway, it could bounce from you to them
since it bounced around the wall

It will only bounce to the same entity per 施放 once. Also every time
the skill bounces, the entity it is bouncing from will be the "原点"
in the skill and the inherited 目标 of onBounce will be the next
entity it is bouncing to, so fromOrigin is your friend for making
effects!


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onBounce  | ob, m, meta, onbounceskill, ontick, ontickskill, ot, s, skill | The skill that bounces between 目标                                                                                |<!--type:Metaskill-->|
| bounces   | b         | How many times the chain should bounce                               | 2       |
| delay     | d, bd, bouncedelay, i, interval | The delay between bounces                      | 1       |
| 半径    | r, bounceradius, bouncerange, range | How far the skill will bounce to a new 目标 | 5    |
| hitSelf   | hs        | 是否 the chain should affect the 施法者                           | false   |
| hitTarget | ht        | 是否 the chain should do the initial from the 施法者 to the first 目标 | true    |
| hitPlayers | hp       | 是否 the chain should bounce to players                           | true    |
| hitNonPlayers | hnp   | 是否 the chain should bounce to non-players                       | false   |
| bounce条件 | 条件, cond, c | 条件 applied to the bounce 目标             |<!--type:条件-->|


## 示例
```yaml
Skills:
- chain{
    bounces=5;
    bounceRadius=10;
    bounceDelay=1;
    hitSelf=false;
    hitPlayers=true; 
    hitNonPlayers=true;
    hitTarget=true;
    onBounce=[
      - effect:particleline{p=flame;fromOrigin=true}
    ];
    bounceConditions=[
      - inlineofsight
      - hasaura{aura=damageResist} false
    ];
  } @target ~onTimer:20
```


<!--TAGS-->
<!--tag:Meta-Mechanic-->