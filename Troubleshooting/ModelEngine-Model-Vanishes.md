If若your ModelEngine model vanishes on a 服务器 restart，or 当您 leave the area the 生物将isin, 您需要 to make sure the Model has the `save` 属性 设为 true。

Your current 生物 文件 may have a line like the following:
```yaml
Skills:
- model{m=Duck;n=name} @self ~onSpawn
```

WWhile 您可以 solve the issue by adding the following:
```yaml
Skills:
- model{m=Duck;n=name;save=true} @self ~onSpawn
```