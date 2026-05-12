## 描述
Allows to either equip or remove a saddle on the target entity.


## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| take      | t, remove, r | Whether the saddle 应当 taken away instead                   | false   |


## 示例
```yaml
ExampleSkill:
  Skills:
  - saddle{r=true} @self
```

The following example is a bit more nuanced: it shows how a horse that can equip itself with a temporary saddle 可以 made
```yaml
ExampleMob:
  Type: HORSE
  Options:
    Tamed: true
  Skills:
  - aura{d=1200;auraName=TemporarySaddle;cd=600;sync=true;i=1;
    onStart=[
    - saddle @self
    ];
    onTick=[
    - particle{p=crit;hs=0.3;vs=0.2;y=1;a=2} @self
    - closeinventory @Passenger
    ];
    onEnd=[
    - saddle{r=true} @self
    ]
    } @self ~onInteract
```


## 别名
- [x] setsaddle
- [x] givesaddle


<!--TAGS-->
<!--tag:Inventory-->
