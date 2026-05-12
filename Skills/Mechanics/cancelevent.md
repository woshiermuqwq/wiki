## 描述

Cancel the Event that triggered the skill. This 技能 has several
important requirements in order to 执行 properly:

-   **The 技能 or initial skill must be run with sync=true.**
> Example: -
    skill{s=CancelEventSkill;sync=true} ~onDamaged
-   No delays allowed.
-   Not all 触发 are associated with events that can be cancelled. 
-   Other 技能 that listens to the same 触发 仍将 be triggered even if the event is ultimately cancelled.

### Compatible 触发
-   ~onAttack
-   ~onBucket
-   ~onDamaged
-   ~onDeath
-   ~onExplode
-   ~onInteract
-   ~onCombat
-   ~onTeleport
-   ~onShoot (Requires Crucible for a bow / crossbow if the 施法者 is a player)
-   ~onUse (Requires Crucible)
-   ~onConsume (Requires Crucible)

> This is not a complete list, and other 触发 may work too, the ones listed here are just the confirmed ones

## 属性
> *This 技能 has no attributes*


## 示例

Skill.yml:
```yaml
CancelDamageEvent:
  Skills:
  - CancelEvent
  - message{m="&cYou cannot hurt this mob!"} @trigger
```
生物.yml:
```yaml
NoDamageMob:
  Type: villager
  Skills:
  - skill{s=CancelDamageEvent;sync=true} ~onDamaged
```
You can use it in-line too! 此示例将 prevent the 生物 from shooting its bow, and from taking any damage.
```yaml
customskeleton:
  Type: skeleton
  Skills:
  - cancelevent{sync=true} @self ~onShoot
  - cancelevent{sync=true} @self ~onDamaged
```


<!--TAGS-->
<!--tag:Meta:Flow-->
