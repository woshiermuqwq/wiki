## 描述
选取由施法者召唤的所有子实体。  
对玩家施法者也有效，前提是使用了 [summon] 技能并将 `summonerIsOwner` 属性设为 `true`。


## 属性
>*此目标选择器没有属性*


## 示例
```yaml
  Skills:
  - heal{a=10} @Children
```


## 别名
- [x] child
- [x] summons


<!-- LINKS -->
[summon]: /skills/mechanics/summon
