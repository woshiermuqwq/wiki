## 描述
A switch allows a 条件 to be tested against a list of (cases) values.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| uniqueresult | unique, first | 是否 to stop execution of other skills if a 条件 was met | true |
| 条件 |           | A 条件 to test for                                              |         |
| cases     |           | A list of cases to evaluate                                          |         |


## 示例
```yml
MyCoolMob:
  Type: ZOMBIE
  Skills:
    - switch{condition=entitytype{t=<case>};cases=
        case SKELETON=[
          - message{m="A SKELETON JUST HIT ME"} @Server
          ]
        case HUSK=[
          - message{m="A HUSK JUST HIT ME!"} @Server
          ]
        case PIG=[
          - message{m="NOOO A PIG"} @Server
          ]
        case DEFAULT=[
          - message{m="SOMEONE or SOMETHING HIT ME OUT OF NOWHEREE!!"} @Server
          ]
      } @trigger ~onDamaged
```


<!--TAGS-->
<!--tag:Meta-->
<!--tag:Meta-Mechanic-->

