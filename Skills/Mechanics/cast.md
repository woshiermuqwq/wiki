## 描述
施放 is an [光环] 技能 similar to
[Skill](/skills/技能/skill) in that it 执行 a skill, however
施放 instead "施放" the skill similar to how you'd expect an RPG hero
or monster to do so. 施放 will 执行 the given skill if the 施放
completes successfully (例如 if the 光环 finishes normally), but can be
interrupted.

Only one spell can be 施放 at a time, and which runs as an 光环 on the
施法者 named **#casting**. Removing the 光环 from the entity will
interrupt the 施放. Any 光环 settings that cause the 施放 to stop early
will also interrupt casting, such as cancelling on move or teleport.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| onCastSkill | oncast, oc | Skill to 执行 if the 施放 finishes successfully                   |<!--type:Metaskill-->|
| onInterruptedSkill | oninterrupted, oninterrupt, oi | Skill to 执行 if the 施放 is interrupted |<!--type:Metaskill-->|
| onnotargetsskill | onnotargets, onnotarget, ont | Skill to 执行 if no 目标 is found     |<!--type:Metaskill-->|
| skillname | spellname, sn | Display name of the spell in the 施放 bar                        |         |
| showCastBar | castbar, cb | 是否 to show the 施放 bar                                     | true    |
| cancelOnMove | com    | 是否 to cancel the 光环 if the 施法者 moves                       | false   |
> This 技能 继承 [光环] 技能
>> - The `auraName` attribute is **set** at `#casting` and **cannot be changed**
>> - The `charges` attribute is **set** at `1` and **cannot be changed**
>> - The `maxStacks` attribute is **set** at `1` and **cannot be changed**
>> - The `mergeAll` attribute is **set** at `true` and **cannot be changed**


## 示例
```yml
myCoolMob:
  Type: ZOMBIE
  Skills:
    - cast{
          skillName="&aFrost Blast";
          duration=40;
          onCast=FrostBlast-Cast;
          onTick=FrostBlast-Tick;
          onInterrupted=FrostBlast-Interrupted;
          onNoTargets=FrostBlast-NoTargets;
          showCastBar=true
        } @target ~onTimer:100
```
```yaml
# This will be cast once the duration has elapsed
FrostBlast-Cast:
  Skills:
  - damage{a=20}
  - message{m="MUHAHA, TAKE THAT!"}

# This will be cast while the main casting is still in progress
FrostBlast-Tick:
  Skills:
  - particle{p=end_rod;a=4;hs=1;vs=1} @selflocation{y=1}

# This will be cast if the aura is somehow removed
FrostBlast-Interrupted:
  Skills:
  - message{m="Tsk, you got me!"}

# This will be cast if the original target for the aura no longer exist
FrostBlast-NoTargets:
  Skills:
  - message{m="...Where has everyone gone to?"} @World
```

<!-- LINKS -->
[aura]: /skills/mechanics/aura


<!--TAGS-->
<!--tag:Meta-Mechanic:Aura-->