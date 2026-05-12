## 描述

Cancel the Event that triggered the skill. This 技能 has several
important requirements in order to execute properly:

-   **The 技能 or initial skill 必须 run with sync=true.**
> Example: -
    skill{s=CancelEventSkill;sync=true} ~onDamaged
-   No delays allowed.
-   Not all triggers are associated with events that 可以 cancelled. 
-   Other 技能s that listens to the same trigger will still be triggered even if the event is ultimately cancelled.

### Compatible Triggers
-   ~onAttack
-   ~onBucket
-   ~onDamaged
-   ~onDeath
-   ~onExplode
-   ~onInteract
-   ~onCombat
-   ~onTeleport
-   ~onShoot (Requires Crucible for a bow / crossbow if the caster is a player)
-   ~onUse (Requires Crucible)
-   ~onConsume (Requires Crucible)

> This is not a complete list, and other triggers may work too, the ones listed here are just the confirmed ones

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
Mob.yml:
```yaml
NoDamageMob:
  Type: villager
  Skills:
  - skill{s=CancelDamageEvent;sync=true} ~onDamaged
```
You can use it in-line too! This example will prevent the mob from shooting its bow, and from taking any damage.
```yaml
customskeleton:
  Type: skeleton
  Skills:
  - cancelevent{sync=true} @self ~onShoot
  - cancelevent{sync=true} @self ~onDamaged
```


<!--TAGS-->
<!--tag:Meta:Flow-->
