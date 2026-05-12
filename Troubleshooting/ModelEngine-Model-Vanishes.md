如果你的 ModelEngine 模型在服务器重启后消失，或者当你离开生物所在区域后消失，你需要确保模型的 `save` 属性设为 true。

你当前的生物文件中可能有一行类似这样：
```yaml
Skills:
- model{m=Duck;n=name} @self ~onSpawn
```

你可以通过添加以下内容来解决此问题：
```yaml
Skills:
- model{m=Duck;n=name;save=true} @self ~onSpawn
```
