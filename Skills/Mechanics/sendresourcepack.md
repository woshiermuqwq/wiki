## 描述
Sends a resource pack to 目标玩家.


## 属性
| 属性 | 缩写   | 描述                                                          | 默认值 |
|-----------|-----------|----------------------------------------------------------------------|---------|
| url       | u, link   | The link to the resourcepack to download                             | NONE    |
| hash      | h         | The hash for the resource pack                                    | mythic生物 |


## 示例
> The hash provided in this example is just a demonstration, do not
use it in your skill
```yaml
Skills:
  - sendresourcepack{url="https://yourresourcepackurlhere";hash="cf23df2207d99a74fbe169e3eba035e633b65d94"} @PIR{r=15} ~onSpawn
  - ...
```


## 别名
- [x] resourcepack