## 描述
Gives money to players.  
This 技能 needs the Vault plugin and an economy plugin installed to
work and Vault must be enabled in the Mythic生物 `config-general.yml` file
```yaml
    Vault:
      Enabled: true
```

## 属性
| 属性 | 缩写 | 描述          | 默认值 |
|-----------|---------|----------------------|---------|
| amount    | a       | The amount of money. | 0.0     |

  

## 示例
```yaml
  Skills:
  - currencygive{amount=20} @pir{r=20} ~onSpawn 0.2
```
If executed all players in 半径 of 20 blocks around the spawned 生物
will receive 20 money by a chance of 20%


## 别名
- [x] giveCurrency