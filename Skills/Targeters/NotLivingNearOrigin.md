## 描述
选取原点附近半径内的所有非活体实体


## 属性
| 属性 | 别名   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| radius    | r         | 选取半径                                           | 5       |


## 示例
此技能结束时将在全局聊天中输出其周围 10 格半径内所有非活体实体的 UUID
```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - command{c="say <target.uuid>"} @NotLivingNearOrigin{r=10}
    ]}
```

## 别名
- [x] nonLivingNearOrigin
- [x] NLNO
