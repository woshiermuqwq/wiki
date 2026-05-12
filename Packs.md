MythicMobs 拥有非常强大的包（Pack）系统，可以更好地组织你的所有文件，并且能够轻松安装来自 MCModels 等渠道供应商提供的包。

只需在 MythicMobs/Packs 文件夹中创建一个文件夹（根据你的包随便取名字），然后在其内部可以创建 Items、Mobs、Skills、RandomSpawns 等文件夹，就像在基础 MythicMobs 目录中一样。这些文件夹内你也可以像基础文件夹那样放置对应类型的任意数量的文件。打包成 zip 就可以轻松分发了！

## 包信息
制作包时，你可能想要嵌入更多信息，比如作者、包名等。这可以通过在包的主目录中创建 `packinfo.yml` 文件来实现。

```yaml
Name: 包的名称
Version: 0.1.0
Author: 作者名称
Icon:
  Material: 要使用的物品的 Bukkit 名称
  Model: 物品的 CustomModelData
URL: 指向你网站的链接（如有）
Description:
- 这是一个列表
- 将作为包描述
- 出现的内容
- &a你也可以使用颜色代码！&r
```

这些信息将在用户使用 `/mm menu` 指令进入 MythicMobs 菜单浏览任意可用分类时，悬停在包图标上显示。如果包中包含与所选分类相关的物品，就会展示。
