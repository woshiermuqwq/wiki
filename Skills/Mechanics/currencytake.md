## 描述
Takes money from players.  
This 技能 needs the Vault plugin and an economy plugin installed to
work.  
It also requires Vault being enabled in the [config.yml](/configuration/)
```yaml
        Vault:
          Enabled: true
```

## 属性
| 属性 | 缩写 | 描述 | 默认值 |
|-----------|---------|----------------------------------------|---------|
| amount    | a       | The amount of money taken from player. | 0.0     |

  

## 示例
This skill will take away 20 money from all players in radius of 20 blocks.
```yaml
  Skills:
  - currencytake{amount=20} @pir{r=20} ~onSpawn
```


## 别名
- [x] takeCurrency
