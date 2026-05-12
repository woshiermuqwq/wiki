#!/usr/bin/env python3
"""MythicMobs Wiki 文档汉化脚本 v3 - 最终优化版"""

import os, re, sys

# ============================================================
# 完整术语表
# ============================================================
TERMS = {
    # Core concepts
    "mob": "生物", "mobs": "生物",
    "skill": "技能", "skills": "技能",
    "mechanic": "机制", "mechanics": "机制",
    "condition": "条件", "conditions": "条件",
    "targeter": "目标选择器", "targeters": "目标选择器",
    "trigger": "触发器", "triggers": "触发器",
    "caster": "施法者", "origin": "原点", "parent": "父级",
    "child": "子级", "children": "子级",
    "spawn": "生成", "despawn": "消失",
    "faction": "阵营", "factions": "阵营",
    "threat table": "仇恨表", "threat tables": "仇恨表",
    "immunity table": "免疫表", "immunity tables": "免疫表",
    "template": "模板", "templates": "模板",
    "metaskill": "元技能", "metaskills": "元技能",
    "placeholder": "占位符", "placeholders": "占位符",
    "variable": "变量", "variables": "变量",
    "vanilla": "原版", "config": "配置",
    "permission": "权限", "permissions": "权限",
    "command": "指令", "commands": "指令",
    "damage": "伤害", "HP": "生命值", "health": "血量",
    "equipment": "装备", "drop": "掉落", "drops": "掉落",
    "projectile": "弹射物", "projectiles": "弹射物",
    "missile": "制导弹射物", "missiles": "制导弹射物",
    "particle": "粒子", "particles": "粒子",
    "aura": "光环", "auras": "光环",
    "cooldown": "冷却", "radius": "半径", "chance": "概率",
    "velocity": "速度向量",
    "AI goal": "AI 目标", "AI goals": "AI 目标",
    "AI target selector": "AI 目标选择器", "AI target selectors": "AI 目标选择器",
    "goal": "AI 目标", "goals": "AI 目标",
    "bossbar": "Boss血条", "boss bar": "Boss血条",
    "killmessage": "击杀信息",
    "inline": "内联", "disguise": "伪装", "disguises": "伪装",
    "level": "等级", "levels": "等级",
    "power scaling": "战力缩放",
    "biome": "生物群系", "biomes": "生物群系",
    "structure": "结构", "structures": "结构",
    "region": "区域", "regions": "区域",
    "block": "方块", "blocks": "方块",
    "enchantment": "附魔", "enchantments": "附魔",
    "potion": "药水", "potions": "药水",
    "attribute": "属性", "attributes": "属性",
    "lore": "物品描述", "banner": "旗帜",
    # General
    "entity": "实体", "entities": "实体",
    "player": "玩家", "players": "玩家",
    "server": "服务器", "world": "世界", "worlds": "世界",
    "plugin": "插件", "plugins": "插件",
    "event": "事件", "events": "事件",
    "value": "值", "values": "值",
    "type": "类型", "types": "类型",
    "name": "名称", "names": "名称",
    "file": "文件", "files": "文件",
    "pack": "包", "packs": "包",
    "item": "物品", "items": "物品",
    "bosses": "Boss", "boss": "Boss",
    "location": "位置", "locations": "位置",
    "owner": "主人", "passenger": "乘客", "passengers": "乘客",
    "mount": "坐骑", "mounted": "骑乘的",
    "vehicle": "载具", "spawner": "生成器", "spawners": "生成器",
    "signal": "信号", "signals": "信号",
    "timer": "计时器", "timers": "计时器",
    "charge": "充能", "channel": "引导",
    "effect": "效果", "effects": "效果",
    "option": "选项", "options": "选项",
    "example": "示例", "examples": "示例",
    "note": "注意", "notes": "注意",
    "tip": "提示", "tips": "提示",
    "alias": "别名", "aliases": "别名",
    "default": "默认", "range": "范围",
    "duration": "持续时间", "interval": "间隔",
    "stack": "堆叠", "stacks": "堆叠",
    "phase": "阶段", "phases": "阶段",
    "mode": "模式", "modes": "模式",
    "shape": "形状", "shapes": "形状",
    "display": "显示", "format": "格式",
    "parameter": "参数", "parameters": "参数",
    "flag": "标志", "flags": "标志",
    "property": "属性", "properties": "属性",
    "behavior": "行为", "behaviors": "行为",
    "combat": "战斗", "movement": "移动",
    "attack": "攻击", "attacks": "攻击",
    "defense": "防御", "speed": "速度",
    "height": "高度", "width": "宽度",
    "distance": "距离", "direction": "方向",
    "angle": "角度", "offset": "偏移",
    "rotation": "旋转", "vector": "向量",
    "amount": "数量", "percent": "百分比",
    "power": "战力", "tier": "层级", "tiers": "层级",
    "action": "动作", "actions": "动作",
    "category": "分类", "categories": "分类",
    "setting": "设置", "settings": "设置",
    "custom": "自定义", "unique": "唯一",
    "inherit": "继承", "inherits": "继承",
    "override": "覆盖", "overrides": "覆盖",
    "modify": "修改", "modifies": "修改",
    "remove": "移除", "removes": "移除",
    "add": "添加", "adds": "添加",
    "execute": "执行", "executes": "执行",
    "apply": "应用", "applies": "应用",
    "require": "需要", "requires": "需要", "required": "必需",
    "optional": "可选", "support": "支持", "supported": "支持",
    "include": "包含", "includes": "包含",
    "exclude": "排除", "excludes": "排除",
    "ignore": "忽略", "match": "匹配", "matches": "匹配",
    "filter": "过滤", "filters": "过滤",
    "return": "返回", "returns": "返回",
    "result": "结果", "results": "结果",
    "message": "消息", "messages": "消息",
    "error": "错误", "errors": "错误",
    "check": "检查", "checks": "检查",
    "fire": "触发", "fires": "触发",
    "target": "目标", "mode": "模式",
    "boolean": "布尔值", "integer": "整数",
    "string": "字符串", "array": "数组",
    "list": "列表", "table": "表",
    "tree": "树", "slot": "栏位", "slots": "栏位",
    "score": "分数", "token": "令牌",
    "currency": "货币", "fov": "视野",
    "lightning": "闪电", "lightning bolt": "闪电",
    "threat": "仇恨", "NONE": "无",
    "scope": "作用域", "scopes": "作用域",
    "enabled": "启用", "disabled": "禁用",
    "activation": "激活", "deactivation": "停用",
    "minecraft": "Minecraft", "minecraft's": "Minecraft 的",
}

# ============================================================
# 复杂句子级翻译 - 按优先级排序
# ============================================================
SENTENCE_PATTERNS = [
    # --- "The X is used to Y" patterns ---
    (r'The (.+?) is used to (give|provide|show|display) (.+?)(?: a (.+?))?\.?$',
     r'\1用于\2\3\4。'),
    (r'The (.+?) feature is used to (.+?)\.$',
     r'\1功能用于\2。'),
    (r'The (.+?) is used (to|for|as) (.+?)\.?$',
     r'\1用于\2\3。'),

    # --- "X can be Y" patterns ---
    (r'(.+?) can be (used|found|configured|set|defined|created|made) (.*?)\.?$',
     r'\1可以\2\3。'),
    (r'(.+?) are generally (.+?)\.?$',
     r'\1通常\2。'),

    # --- "X will Y" patterns ---
    (r'(.+?) will be (.+?) when (.+?)\.?$',
     r'当\3时，\1将\2。'),
    (r'(.+?) will (try|attempt|do|perform|execute|show|display|return|use|apply) (.+?)\.?$',
     r'\1将\2\3。'),
    (r'(.+?) will not (.+?) unless (.+?)\.?$',
     r'除非\3，否则\1不会\2。'),
    (r'(.+?) will not (function|work|operate) until (.+?)\.?$',
     r'直到\3，\1才会\2。'),

    # --- Attribute description patterns ---
    (r'The (.+?) (modifier|value|amount|number|type|name|duration|interval|range|radius) (?:of|for|to use) (?:the )?(.+?)\.?$',
     r'\3的\1\2。'),
    (r'Whether (?:or not )?(.+?) should be (.+?)\.?$',
     r'是否应\2\1。'),
    (r'Whether (?:or not )?(.+?) is (.+?)\.?$',
     r'\1是否\2。'),
    (r'Determines (?:if|whether) (.+?)\.?$',
     r'决定是否\1。'),
    (r'Determines (.+?)\.?$',
     r'决定\1。'),
    (r'Sets (?:the )?(.+?) (?:to|as) (.+?)\.?$',
     r'将\1设\2。'),
    (r'Sets (?:the )?(.+?)\.?$',
     r'设\1。'),

    # --- "Available X for Y" ---
    (r'Available (.+?) for (.+?)(?: \(.*?\))?:?$',
     r'\2的可用\1：'),
    (r'Possible (.+?) (?:for|are|include):?$',
     r'可能的\1：'),

    # --- Table-like descriptions ---
    (r'A (.+?) with no (.+?)\.?$',
     r'一个没有\2的\1。'),
    (r'A (.+?) with (.+?)\.?$',
     r'一个具有\2的\1。'),
    (r'A (.+?) that can (?:be )?(.+?)\.?$',
     r'一个可以\2的\1。'),
    (r'A (.+?) that (.+?)s?\.?$',
     r'一个\2的\1。'),
    (r'A (.+?) where (.+?)\.?$',
     r'一个\2的\1。'),
    (r'A (.+?) (?:is|represents) (.+?)\.?$',
     r'\1是\2。'),
    (r'A (.+?) of (.+?)\.?$',
     r'\2的\1。'),

    # --- "If ..., ..." patterns ---
    (r'^If (.+?), (.+?) (will|can|is|are|must|should) (.+?)\.?$',
     r'若\1，\2将\3\4。'),
    (r'^If (.+?) is (.+?), it (will|can|is|are|must|should) (.+?)\.?$',
     r'若\1为\2，它将\3\4。'),

    # --- "Any" patterns ---
    (r'Any (.+?) you create with (.+?) could also be (.+?)\.?$',
     r'使用\2创建的任何\1也可以\3。'),
    (r'Any (.+?) can be (.+?)\.?$',
     r'任何\1都可以\2。'),

    # --- "Unlike" patterns ---
    (r'^Unlike (.+?), (.+?)\.?$',
     r'与\1不同，\2。'),

    # --- "X made with" patterns ---
    (r'(.+?) (made|created) with (?:this )?(.+?) (.+?)\.?$',
     r'使用\3\4的\1。'),

    # --- "X supports Y" ---
    (r'(.+?) supports? (.+?)\.?$',
     r'\1支持\2。'),

    # --- General sentence patterns ---
    (r'^(.+?) is based (?:on|around) (.+?)\.?$',
     r'\1基于\2。'),
    (r'^(.+?) are a system for (.+?)\.?$',
     r'\1是一个用于\2的系统。'),
    (r'^(.+?) does its best to (.+?)\.?$',
     r'\1会尽力\2。'),
    (r'^(.+?) (?:does|do) not (.+?) unless (.+?)\.?$',
     r'除非\3，否则\1不会\2。'),
    (r'^(.+?) (?:does|do) not come with (.+?)\.?$',
     r'\1不附带\2。'),
    (r'^(.+?) throw(?:s)? an (.+?) if (.+?)\.?$',
     r'若\3，\1会抛出\2。'),

    # --- Targets-related ---
    (r'^Targets (.+?) at (.+?)\.?$',
     r'以位于\2的\1为目标。'),
    (r'^Targets (.+?) from (.+?)\.?$',
     r'以来自\2的\1为目标。'),
    (r'^Targets (?:the )?(.+?) (?:using|based on|via) (.+?)\.?$',
     r'通过\2以\1为目标。'),
    (r'^Targets (?:the )?(.+?)\.?$',
     r'以\1为目标。'),
    (r'^targets (?:the )?(.+?)\.?$',
     r'以\1为目标。'),

    # --- Triggers ---
    (r'^(?:Fires?|Called|Executed|Triggered?|Activated?) when (.+?)\.?$',
     r'在以下情况触发：\1。'),
    (r'^(?:Fires?|Called|Executed|Triggered?|Activated?) on (.+?)\.?$',
     r'在以下情况触发：\1。'),

    # --- Conditions ---
    (r'^(?:Returns?|Gives?) (.+?) (?:if|when) (.+?)\.?$',
     r'若\2，返回\1。'),
    (r'^(?:Checks?|Tests?) (?:if|whether) (.+?)\.?$',
     r'检查是否\1。'),
    (r'^(?:Checks?|Tests?) (.+?)\.?$',
     r'检查\1。'),

    # --- Mobs ---
    (r'^Causes (?:the )?(.+?) to (.+?)\.?$',
     r'使\1\2。'),
    (r'^Makes (?:the )?(.+?) (.+?)\.?$',
     r'使\1\2。'),
]

# ============================================================
# 内联短语替换 (长→短顺序)
# ============================================================
INLINE_PHRASES = [
    # Complex phrases
    ("is a way to", "是一种"),
    ("must be a unique name and", "必须为一个唯一名称且"),
    ("must be a unique name", "必须为一个唯一名称"),
    ("It is advised that", "建议"),
    ("is based all around", "完全围绕"),
    ("based on what is specified", "基于指定的内容"),
    ("in the same style used by", "以与...相同的风格"),
    ("Can represent much larger numbers than", "可表示比...大得多的数字"),
    ("making the items using the", "使用"),
    ("complete list of", "完整列表"),
    ("as long as the", "只要"),
    ("there are plenty of", "有大量"),
    ("that you can utilize", "可供使用"),
    ("Below you find a", "以下是"),
    ("that can be added to your", "可添加到您的"),
    ("Most of the", "大部分"),
    ("meaning you", "意味着您"),
    ("have to configure the entire", "必须配置完整的"),
    ("each time you are creating", "每次创建"),
    ("All that really", "真正"),
    ("How your", "您的"),
    ("will be referenced internally", "在内部引用"),
    ("can be any name you like", "可以是您喜欢的任何名称"),
    ("clash with other", "与其他...冲突"),
    ("how your mob will be", "您的生物将如何"),
    ("will not change or update on its own", "不会自行更改或更新"),
    ("you have to use", "您必须使用"),
    ("to change or update it", "来更改或更新它"),
    ("could also be created by", "也可以通过...创建"),
    ("named anything you like", "随意命名"),
    ("can be either permanent or temporary", "可以是永久的或临时的"),
    ("will vanish when the current queue of", "将在当前...队列结束时消失"),
    ("are all applicable for all", "并非所有情况都适用所有"),
    ("it will throw an error if", "若...则会抛出错误"),
    ("for something that makes no", "用于无意义的"),
    ("on what you specify", "取决于您指定的内容"),
    ("will do its xp to", "将尽力"),
    ("even if it is hidden from view", "即使它不可见"),
    ("is the speed modifier for the mob while this action is being taken", "是生物执行此动作时的速度修正值"),

    # Medium phrases
    ("is used to", "用于"),
    ("are used to", "用于"),
    ("can be used to", "可用于"),
    ("allows you to", "允许"),
    ("This field determines", "此字段决定"),
    ("A complete list of available", "可用...的完整列表"),
    ("can be found on", "可在...找到"),
    ("while here you can find", "而在此可找到"),
    ("that are explicitly", "明确"),
    ("hard-to-discover quirks", "难以发现的怪异行为"),
    ("for new entity types that", "对于...的新实体类型"),
    ("will not function until", "在...之前不会生效"),
    ("adds to the base game", "添加到原版游戏"),
    ("It is advised that you refer to", "建议参考"),
    ("in order to form a better opinion", "以更好地了解"),
    ("on what entity you should be using", "应使用哪种实体"),
    ("for your current endeavor", "用于当前的需求"),
    ("This option supports", "此选项支持"),
    ("You can make any number of", "您可以创建任意数量的"),
    ("in the items folder", "在物品文件夹中"),
    ("and they can be named anything you like", "并可随意命名"),
    ("is much more comfortable", "更舒适"),
    ("unlike mobs and skills however", "但与生物和技能不同"),
    ("any items you create", "您创建的任何物品"),
    ("though making the items", "尽管创建物品"),
    ("used to specify the", "用于指定"),
    ("references an items", "引用物品的"),
    ("does not need specified", "无需指定"),
    ("can also be left blank", "也可留空"),
    ("will just not be applied", "将不会被应用"),
    ("the default value for", "的默认值"),
    ("any slot that", "任何"),
    ("not included to", "不包含"),
    ("is left empty", "留空为"),
    ("if left empty", "如果留空"),
    ("defaults to", "默认为"),
    ("in most cases", "大多数情况下"),
    ("in this case", "在此情况下"),
    ("in either case", "无论如何"),
    ("by default", "默认情况下"),
    ("the default value is", "默认值为"),
    ("set to true", "设为 true"),
    ("set to false", "设为 false"),
    ("for example", "例如"),
    ("for instance", "例如"),
    ("such as", "例如"),
    ("as well as", "以及"),
    ("based on", "基于"),
    ("depending on", "取决于"),
    ("instead of", "而不是"),
    ("rather than", "而不是"),
    ("in order to", "为了"),
    ("at least", "至少"),
    ("at most", "最多"),
    ("capable of", "能够"),
    ("associated with", "关联"),
    ("related to", "相关"),
    ("regardless of", "无论"),
    ("due to", "由于"),
    ("as long as", "只要"),
    ("as soon as", "一旦"),
    ("more than", "多于"),
    ("less than", "小于"),
    ("equal to", "等于"),
    ("greater than", "大于"),
    ("no longer", "不再"),
    ("the same as", "与...相同"),
    ("identical to", "与...相同"),
    ("similar to", "类似"),
    ("different from", "不同于"),
    ("compatible with", "兼容"),
    ("compared to", "相较于"),
    ("referred to as", "被称为"),
    ("also known as", "也称为"),
    ("a lot more", "更多的"),
    ("even more", "甚至更多"),
    ("quite easy", "相当简单"),
    ("do not come with", "不附带"),
    ("come with", "附带"),
    ("take effect until", "才会生效"),
    ("not all", "并非所有"),
    ("no longer", "不再"),
    ("each other", "彼此"),
    ("one another", "彼此"),
    ("the same time", "同时"),
    ("over time", "随时间"),
    ("at that same time", "在同一时间"),
    ("is not", "不是"),
    ("does not", "不"),
    ("do not", "不要"),
    ("cannot", "不能"),
    ("should be", "应为"),
    ("must be", "必须为"),
    ("needs to", "需要"),
    ("has to", "必须"),
    ("can be set", "可设为"),
    ("at the moment", "此刻"),
    ("right now", "现在"),
    ("for now", "目前"),
    ("up until", "直到"),
    ("up to", "最多"),
    ("a number with", "带"),
    ("decimal places", "小数位"),
    ("can either be", "可以是"),
    ("true or false", "true 或 false"),
    ("a set of", "一组"),
    ("an ordered list of", "一个有序的"),
    ("a list of", "一系列"),
    ("a series of", "一系列"),
    ("key-value pairs", "键值对"),
    ("a location in the server", "服务器中的位置"),
    ("a moment in time", "时间中的一个时刻"),
    ("represented by the number of milliseconds", "以毫秒数表示"),
    ("since the epoch", "自纪元以来的"),
    ("parsed at the moment", "在...时解析"),
    ("that can be used to", "可用于"),
    ("where that", "该"),
    ("where the", "该"),
    ("when you", "当您"),
    ("you will", "您将"),

    # Table headers
    ("Tab Completion", "Tab 补全"),
    ("Return Type", "返回类型"),
    ("Result Type", "结果类型"),
    ("Default Value", "默认值"),

    # Short phrases
    ("without the", "不"),
    ("with the", "与"),
    ("for the", "对于"),
    ("from the", "从"),
    ("into the", "到"),
    ("onto the", "到"),
    ("out of", "从"),
    ("out the", "移除"),
    ("over the", "在"),
    ("under the", "在...下"),
    ("behind the", "在...后"),
    ("inside the", "在...内"),
    ("outside the", "在...外"),
    ("around the", "在...周围"),
    ("through the", "通过"),
    ("across the", "跨过"),
    ("between the", "在...之间"),
    ("along the", "沿着"),
    ("towards the", "朝向"),
    ("away from", "远离"),
    ("next to", "紧挨"),
    ("close to", "靠近"),
    ("far from", "远离"),
    ("above the", "在...上方"),
    ("below the", "在...下方"),
    ("in front of", "在...前方"),
    ("on top of", "在...顶部"),

    # "有" patterns (avoid over-conversion)
    ("there is no", "没有"),
    ("there are no", "没有"),
    ("there is a", "有"),
    ("there are a", "有"),
    ("it is possible to", "可以"),
    ("it allows", "它允许"),
    ("it has", "它有"),
    ("it will", "它将"),
    ("it is", "它是"),
    ("it can", "它可以"),
    ("it does", "它会"),
    ("they are", "它们是"),
    ("they have", "它们有"),
    ("they will", "它们将"),
    ("they can", "它们可以"),
    ("they do", "它们会"),
    ("this is", "这是"),
    ("this means", "这意味着"),
    ("this includes", "这包括"),
    ("that is", "即"),
    ("that are", "即"),
    ("which is", "即"),
    ("which are", "即"),
    ("who is", "即"),
    ("who are", "即"),
    ("has been", "已被"),
    ("have been", "已被"),
    ("will be", "将"),
    ("will not", "不会"),
    ("will have", "将有"),
    ("will also", "还将"),
    ("will only", "只会"),
    ("will never", "永远不会"),
    ("will always", "总会"),
    ("will still", "仍会"),
    ("will instead", "将改为"),
    ("will automatically", "将自动"),
    ("will immediately", "将立即"),
    ("may not", "可能不"),
    ("might not", "可能不"),
    ("could not", "无法"),
    ("should not", "不应"),
    ("did not", "未"),
    ("does not", "不"),
    ("do not", "不要"),
    ("doesn't", "不"),
    ("don't", "不要"),
    ("won't", "不会"),
    ("can't", "不能"),
    ("isn't", "不是"),
    ("aren't", "不是"),
    ("wasn't", "不是"),
    ("weren't", "不是"),
    ("hasn't", "尚未"),
    ("haven't", "尚未"),
    ("wouldn't", "不会"),
    ("couldn't", "无法"),
    ("shouldn't", "不应"),
    ("it's", "它是"),
    ("that's", "那是"),
    ("here's", "这是"),
    ("there's", "有"),
    ("let's", "让我们"),
    ("we're", "我们是"),
    ("they're", "它们是"),
    ("you're", "您是"),
    ("I'm", "我"),

    # common small words
    ("means", "意味着"),
    ("allows", "允许"),
    ("causes", "导致"),
    ("prevents", "阻止"),
    ("creates", "创建"),
    ("contains", "包含"),
    ("provides", "提供"),
    ("defines", "定义"),
    ("determines", "决定"),
    ("specifies", "指定"),
    ("represents", "表示"),
    ("commonly", "通常"),
    ("typically", "通常"),
    ("generally", "通常"),
    ("usually", "通常"),
    ("exactly", "精确地"),
    ("currently", "当前"),
    ("previously", "之前"),
    ("recently", "最近"),
    ("immediately", "立即"),
    ("completely", "完全"),
    ("entirely", "完全"),
    ("partially", "部分"),
    ("automatically", "自动"),
    ("explicitly", "明确"),
    ("implicitly", "隐式"),
    ("essentially", "本质上"),
    ("basically", "基本上"),
    ("functionally", "功能上"),
    ("technically", "技术上"),
    ("specifically", "具体"),
    ("potentially", "可能"),
    ("certainly", "肯定"),
    ("probably", "可能"),
    ("perhaps", "也许"),
    ("maybe", "也许"),
    ("slightly", "略微"),
    ("significantly", "显著"),
    ("extremely", "极其"),
    ("especially", "尤其"),
    ("particularly", "特别"),
    ("additionally", "此外"),
    ("alternatively", "或者"),
    ("consequently", "因此"),
    ("unfortunately", "不幸"),
    ("fortunately", "幸运"),
    ("surprisingly", "出人意料"),
    ("accordingly", "相应地"),
    ("respectively", "分别"),
    ("individually", "单独"),
    ("separately", "分开"),
    ("together", "一起"),
    ("independently", "独立"),
    ("simultaneously", "同时"),
    ("temporarily", "暂时"),
    ("permanently", "永久"),
    ("eventually", "最终"),
    ("occasionally", "偶尔"),
    ("frequently", "频繁"),
    ("rarely", "很少"),
    ("always", "总是"),
    ("never", "永不"),
    ("sometimes", "有时"),
    ("often", "经常"),
    ("once", "一旦"),
    ("twice", "两次"),
    ("however", "但是"),
    ("therefore", "因此"),
    ("otherwise", "否则"),
    ("meanwhile", "同时"),
    ("nonetheless", "尽管如此"),
    ("furthermore", "此外"),
    ("moreover", "而且"),
    ("besides", "除此之外"),
    ("indeed", "确实"),
    ("actually", "实际上"),
    ("really", "真的"),
    ("simply", "仅仅"),
    ("merely", "仅仅"),
    ("only", "仅"),
    ("just", "仅"),
    ("still", "仍然"),
    ("already", "已经"),
    ("yet", "还"),
    ("again", "再次"),
    ("also", "也"),
    ("too", "也"),
    ("either", "也"),
    ("neither", "都不"),
    ("both", "两者都"),
    ("none", "没有"),
    ("nothing", "没有"),
    ("everything", "一切"),
    ("something", "某事"),
    ("anything", "任何事物"),
    ("nothing", "无"),
    ("nobody", "没有人"),
    ("anybody", "任何人"),
    ("everybody", "每个人"),
    ("somebody", "某人"),
    ("someone", "某人"),
    ("anyone", "任何人"),
    ("everyone", "每个人"),
    ("no one", "没有人"),
    ("somewhere", "某处"),
    ("anywhere", "任何地方"),
    ("everywhere", "到处"),
    ("nowhere", "无处"),
    ("otherwise", "否则"),
    ("within", "在...内"),
    ("without", "没有"),
    ("throughout", "遍及"),
    ("through", "通过"),
    ("except", "除了"),
    ("including", "包括"),
    ("excluding", "排除"),
    ("during", "期间"),
    ("after", "之后"),
    ("before", "之前"),
    ("until", "直到"),
    ("while", "当"),
    ("since", "自从"),
    ("unless", "除非"),
    ("although", "尽管"),
    ("though", "尽管"),
    ("because", "因为"),
    ("whether", "是否"),
    ("either", "任一"),
    ("another", "另一个"),
    ("other", "其他"),
    ("others", "其他"),
    ("itself", "自身"),
    ("themselves", "自身"),
    ("yourself", "您自己"),
    ("ourselves", "我们自己"),
    ("myself", "我自己"),
    ("himself", "他自己"),
    ("herself", "她自己"),

    # extra specific patterns from observed output
    ("it is possible to", "可以"),
    ("to know if", "以判断是否"),
    ("you are wanting to", "您想要"),
    ("You can also", "您还可以"),
    ("you can", "您可以"),
    ("you have to", "您必须"),
    ("you do not", "您不要"),
    ("you use", "您使用"),
    ("you want", "您想要"),
    ("you need", "您需要"),
    ("you like", "您喜欢"),
    ("you refer", "您参考"),
    ("you create", "您创建"),
    ("you can make", "您可以创建"),
    ("have to", "必须"),
    ("on spigot javadocs", "在 Spigot Javadocs 上"),
    ("will strike a", "将击出"),
    ("fake lightning", "假闪电"),
    ("into the", "到"),
    ("above it", "上方"),
    ("given to", "给予"),
    ("color codes", "颜色代码"),
    ("adds support for", "添加...支持"),
    ("will not function", "不会生效"),
    ("page in order", "页面以"),
    ("should be using", "应使用"),
    ("when the server", "当服务器"),
    ("the health that the", "生物在"),
    ("will vanish", "将消失"),
    ("queue of skills", "技能队列"),
    ("sends a message", "发送消息"),
    ("the following example", "以下示例"),
    ("would return the same", "将返回相同"),
    ("since their", "因为它们的"),
    ("functionally the same", "功能相同"),
    ("and there are", "有"),
    ("this field", "此字段"),
    ("which entity type", "哪个实体类型"),
    ("your creation will be based upon", "您的创建将以...为基础"),
    ("does not need specified", "无需指定"),
    ("an internal", "内部"),
    ("left empty", "留空"),
    ("will just not be applied", "将不会被应用"),
    ("the base material", "基础材料"),
    ("for your item", "用于您的物品"),
    ("it can be any valid material that", "它可以是任何有效的材料，"),
    ("for your custom", "用于您的自定义"),
    ("found here", "在此找到"),
    ("is listed", "已列出"),
    ("base game", "原版游戏"),
    ("is quite easy", "相当简单"),
    ("a healthbar", "一个生命条"),
    ("in the same", "以相同的"),
    ("but with", "但具有"),
    ("for customization", "用于自定义"),
    ("the mob will be", "该生物将被"),
    ("has after this", "在此之后"),
    ("on what is specified in", "取决于...中指定的内容"),
    ("it is", "它是"),
    ("can be set", "可以设置"),
    ("be followed", "被跟踪"),
    ("hidden from", "从...隐藏"),
    ("even if", "即使"),
    ("while in the", "在...中时"),
    ("defined for the", "定义的"),
    ("when the wither", "当凋灵"),
    ("is spawned", "生成时"),
]

# ============================================================
# YAML 表格头翻译
# ============================================================
HEADER_TABLE = {
    "description": "描述",
    "attribute": "属性", "attributes": "属性",
    "example": "示例", "examples": "示例",
    "usage": "用法",
    "syntax": "语法",
    "parameter": "参数", "parameters": "参数",
    "option": "选项", "options": "选项",
    "note": "注意", "notes": "注意",
    "tip": "提示", "tips": "提示",
    "warning": "警告",
    "alias": "别名", "aliases": "别名",
    "configuration": "配置",
    "requirement": "需求", "requirements": "需求",
    "installation": "安装",
    "setup": "设置",
    "overview": "概述",
    "introduction": "介绍",
    "summary": "总结",
    "details": "详情",
    "see also": "另请参阅",
    "related": "相关",
    "troubleshooting": "故障排除",
    "faq": "常见问题",
    "changelog": "更新日志",
    "advanced": "高级",
    "basic": "基础",
    "general": "通用",
    "implementation": "实现", "implementations": "实现",
    "property": "属性", "properties": "属性",
    "field": "字段", "fields": "字段",
    "format": "格式",
    "flag": "标志", "flags": "标志",
    "return": "返回值", "return value": "返回值",
    "return type": "返回类型",
    "type": "类型",
    "name": "名称",
    "value": "值", "values": "可选值",
    "modifier": "修正值", "modifiers": "修正值",
    "color": "颜色", "colors": "颜色",
    "style": "样式", "styles": "样式",
    "behavior": "行为", "behaviors": "行为",
    "restriction": "限制", "restrictions": "限制",
    "loot table": "战利品表",
    "default": "默认",
    "tab completion": "Tab 补全",
    "weight": "权重",
    "priority": "优先级",
    "duration": "持续时间",
    "interval": "间隔",
    "radius": "半径",
    "range": "范围",
    "speed": "速度",
    "chance": "概率",
    "power": "战力",
}

# ============================================================
# 翻译引擎
# ============================================================

def translate_content(content):
    lines = content.split('\n')
    result = []
    in_code_block = False

    for line in lines:
        stripped = line.strip()

        if stripped.startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        if not stripped:
            result.append(line)
            continue

        translated = translate_line(stripped)
        indent = line[:len(line) - len(stripped)]
        result.append(indent + translated)

    return '\n'.join(result)


def translate_line(line):
    # HTML comments - leave as is
    if line.startswith('<!--') or line.startswith('-->'):
        return line

    # Markdown headers
    m = re.match(r'^(#{1,6})\s+(.+)$', line)
    if m:
        hashes, text = m.groups()
        lower = text.strip().lower()
        if lower in HEADER_TABLE:
            return f"{hashes} {HEADER_TABLE[lower]}"
        return f"{hashes} {translate_text(text)}"

    # Markdown table separators
    if re.match(r'^[\-\| :]+$', line):
        return line

    # Markdown links
    line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  lambda m: f"[{translate_text(m.group(1))}]({m.group(2)})",
                  line)

    # Save inline code
    codes = re.findall(r'`([^`]+)`', line)
    code_map = {}
    for i, code in enumerate(codes):
        placeholder = f"__ICODE{i:04d}__"
        code_map[placeholder] = code
        line = line.replace(f'`{code}`', f'`{placeholder}`', 1)

    # Check if this is a YAML key: value line
    m_yaml = re.match(r'^([\s]*)([\w-]+)(\s*:\s*)(.*)$', line)
    if m_yaml:
        indent, key, colon, value = m_yaml.groups()
        key_clean = key.strip()
        # Is it a YAML key? (no spaces, no special chars in key)
        if key_clean and re.match(r'^[\w-]+$', key_clean):
            if value.strip():
                new_val = translate_text(value.strip())
                text = f"{indent}{key}{colon}{new_val}"
            else:
                text = f"{indent}{key}{colon}"
        else:
            text = translate_text(line)
    else:
        text = translate_text(line)

    # Restore inline code
    for placeholder, code in code_map.items():
        text = text.replace(f'`{placeholder}`', f'`{code}`')

    return text


def translate_text(text):
    """Core translation function"""
    result = text

    # 1. Try sentence-level patterns
    for pattern, replacement in SENTENCE_PATTERNS:
        try:
            m = re.match(pattern, result, re.IGNORECASE)
            if m:
                groups = list(m.groups())
                # Apply term translation to each group
                groups = [translate_single_group(g) for g in groups]
                # Build replacement
                try:
                    new = replacement
                    for i, g in enumerate(groups):
                        new = new.replace(f'\\{i+1}', g)
                    return new
                except:
                    pass
        except:
            pass

    # 2. Apply inline phrase replacements (longest first)
    for english, chinese in INLINE_PHRASES:
        result = result.replace(english, chinese)

    # 3. Apply term translations
    result = apply_terms(result)

    # 4. Cleanup
    result = cleanup_translation(result)

    return result


def translate_single_group(text):
    """Translate a single regex capture group"""
    if not text or text.strip() == '':
        return text
    result = text
    for english, chinese in INLINE_PHRASES:
        result = result.replace(english, chinese)
    result = apply_terms(result)
    result = cleanup_translation(result)
    return result


def apply_terms(text):
    """Apply term translations, longest first"""
    result = text
    sorted_terms = sorted(TERMS.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, chn in sorted_terms:
        result = re.sub(r'\b' + re.escape(eng) + r'\b', chn, result, flags=re.IGNORECASE)
    return result


def cleanup_translation(text):
    """Clean up translation artifacts"""
    # Remove possessive 's
    text = re.sub(r"'s\b", '', text)
    text = re.sub(r"s'\b", '', text)
    # Fix repeated words
    text = re.sub(r'\b(\S+)\s+\1\b', r'\1', text)
    # Fix 的的
    text = text.replace('的的', '的')
    # Fix double spaces
    text = re.sub(r' {2,}', ' ', text)
    # Fix spacing before Chinese punctuation
    text = re.sub(r'\s+([，。！？、：；])', r'\1', text)
    return text.strip()


def process_file(src, dst):
    try:
        try:
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(src, 'r', encoding='latin-1') as f:
                content = f.read()
            content = content.replace('\x93', '"').replace('\x94', '"').replace('\x91', "'").replace('\x92', "'")

        translated = translate_content(content)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(translated)
        return True
    except Exception as e:
        print(f"ERROR: {src}: {e}", file=sys.stderr)
        return False


def process_directory(src_dir, dst_dir):
    count = 0
    errors = 0
    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        dst_root = os.path.join(dst_dir, rel_path) if rel_path != '.' else dst_dir
        for fname in files:
            if fname.endswith('.md'):
                src = os.path.join(root, fname)
                dst = os.path.join(dst_root, fname)
                if process_file(src, dst):
                    count += 1
                else:
                    errors += 1
                if count % 10 == 0:
                    print(f"  进度: {count} 个文件已翻译...", flush=True)
    return count, errors


def main():
    base_src = "/root/.openclaw/workspace/mythicmobs/MythicMobsWiki-master"
    base_dst = "/root/.openclaw/workspace/mythicmobs-zh"

    tasks = [
        ("Skills/Targeters", "Skills/Targeters"),
        ("Skills/Triggers", "Skills/Triggers"),
        ("Skills/Tags", "Skills/Tags"),
        ("Mobs", "Mobs"),
        ("Items", "Items"),
        ("Troubleshooting", "Troubleshooting"),
        ("Wiki-Editors-Resources", "Wiki-Editors-Resources"),
    ]

    total = 0
    total_errors = 0

    for rel_src, rel_dst in tasks:
        src_dir = os.path.join(base_src, rel_src)
        dst_dir = os.path.join(base_dst, rel_dst)
        print(f"\n📁 翻译目录: {rel_src}")
        count, errors = process_directory(src_dir, dst_dir)
        total += count
        total_errors += errors
        print(f"  完成: {count} 个文件，{errors} 个错误")

    # Skills root files
    skills_root_files = [
        "Skills.md", "Variables.md", "Placeholders.md", "Metaskills.md",
        "Math.md", "Inline-Conditions.md", "Audience.md", "EquipSlot.md",
        "SkillTrees.md", "Effects.md", "Dynamic-Metaskills.md",
        "Intratick-Scheduling.md", "Placeholder-Parsing.md",
        "Advanced-User-Guides-and-Techniques.md"
    ]
    print(f"\n📁 翻译目录: Skills/ (根目录文件)")
    skills_count = 0
    skills_src_dir = os.path.join(base_src, "Skills")
    skills_dst_dir = os.path.join(base_dst, "Skills")
    for fname in skills_root_files:
        src = os.path.join(skills_src_dir, fname)
        dst = os.path.join(skills_dst_dir, fname)
        if os.path.exists(src):
            if process_file(src, dst):
                skills_count += 1
                total += 1
            else:
                total_errors += 1
        else:
            print(f"  ⚠️ 未找到文件: {fname}")
    print(f"  完成: {skills_count} 个文件")

    # Enum/Shape.md
    print(f"\n📁 翻译文件: Enum/Shape.md")
    shape_src = os.path.join(base_src, "Enum", "Shape.md")
    shape_dst = os.path.join(base_dst, "Enum", "Shape.md")
    if os.path.exists(shape_src):
        if process_file(shape_src, shape_dst):
            total += 1
            print(f"  完成")
        else:
            total_errors += 1

    print(f"\n{'='*50}")
    print(f"✅ 翻译完成！总计: {total} 个文件，{total_errors} 个错误")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
