#!/usr/bin/env python3
"""MythicMobs Wiki 文档汉化脚本 v2 - 改进版"""

import os, re, sys

# ============================================================
# 术语表
# ============================================================
TERMS = {
    "mob": "生物", "mobs": "生物",
    "skill": "技能", "skills": "技能",
    "mechanic": "机制", "mechanics": "机制",
    "condition": "条件", "conditions": "条件",
    "targeter": "目标选择器", "targeters": "目标选择器",
    "trigger": "触发器", "triggers": "触发器",
    "caster": "施法者",
    "origin": "原点",
    "parent": "父级",
    "child": "子级", "children": "子级",
    "spawn": "生成", "despawn": "消失",
    "faction": "阵营", "factions": "阵营",
    "threat table": "仇恨表", "threat tables": "仇恨表",
    "immunity table": "免疫表", "immunity tables": "免疫表",
    "template": "模板", "templates": "模板",
    "metaskill": "元技能", "metaskills": "元技能",
    "placeholder": "占位符", "placeholders": "占位符",
    "variable": "变量", "variables": "变量",
    "vanilla": "原版",
    "config": "配置",
    "permission": "权限", "permissions": "权限",
    "command": "指令", "commands": "指令",
    "damage": "伤害",
    "HP": "生命值", "Health": "血量", "health": "血量",
    "equipment": "装备",
    "drop": "掉落", "drops": "掉落",
    "projectile": "弹射物", "projectiles": "弹射物",
    "missile": "制导弹射物", "missiles": "制导弹射物",
    "particle": "粒子", "particles": "粒子",
    "aura": "光环", "auras": "光环",
    "cooldown": "冷却",
    "radius": "半径",
    "chance": "概率",
    "velocity": "速度向量",
    "AI goal": "AI 目标", "AI goals": "AI 目标",
    "AI target selector": "AI 目标选择器", "AI target selectors": "AI 目标选择器",
    "goal": "AI 目标", "goals": "AI 目标",
    "bossbar": "Boss血条", "boss bar": "Boss血条",
    "killmessage": "击杀信息",
    "inline": "内联",
    "disguise": "伪装", "disguises": "伪装",
    "level": "等级", "levels": "等级",
    "power scaling": "战力缩放",
    "biome": "生物群系", "biomes": "生物群系",
    "structure": "结构", "structures": "结构",
    "region": "区域", "regions": "区域",
    "block": "方块", "blocks": "方块",
    "enchantment": "附魔", "enchantments": "附魔",
    "potion": "药水", "potions": "药水",
    "attribute": "属性", "attributes": "属性",
    "lore": "物品描述",
    "banner": "旗帜",
    "entity": "实体", "entities": "实体",
    "player": "玩家", "players": "玩家",
    "server": "服务器",
    "world": "世界", "worlds": "世界",
    "plugin": "插件", "plugins": "插件",
    "event": "事件", "events": "事件",
    "value": "值", "values": "值",
    "type": "类型", "types": "类型",
    "name": "名称", "names": "名称",
    "file": "文件", "files": "文件",
    "pack": "包", "packs": "包",
    "item": "物品", "items": "物品",
    "bosses": "Boss",
    "location": "位置", "locations": "位置",
    "owner": "主人",
    "passenger": "乘客", "passengers": "乘客",
    "mount": "坐骑",
    "mounted": "骑乘的",
    "vehicle": "载具",
    "spawner": "生成器", "spawners": "生成器",
    "signal": "信号", "signals": "信号",
    "timer": "计时器", "timers": "计时器",
    "charge": "充能",
    "channel": "引导",
    "channeling": "引导中",
    "effect": "效果", "effects": "效果",
    "option": "选项", "options": "选项",
    "example": "示例", "examples": "示例",
    "note": "注意", "notes": "注意",
    "tip": "提示", "tips": "提示",
    "alias": "别名", "aliases": "别名",
    "default": "默认",
    "range": "范围",
    "duration": "持续时间",
    "interval": "间隔",
    "stack": "堆叠", "stacks": "堆叠",
    "phase": "阶段", "phases": "阶段",
    "mode": "模式", "modes": "模式",
    "shape": "形状", "shapes": "形状",
    "display": "显示",
    "format": "格式",
    "parameter": "参数", "parameters": "参数",
    "flag": "标志", "flags": "标志",
    "property": "属性", "properties": "属性",
    "behavior": "行为", "behaviors": "行为",
    "combat": "战斗",
    "movement": "移动",
    "attack": "攻击", "attacks": "攻击",
    "defense": "防御",
    "speed": "速度",
    "height": "高度",
    "width": "宽度",
    "distance": "距离",
    "direction": "方向",
    "angle": "角度",
    "offset": "偏移",
    "rotation": "旋转",
    "vector": "向量",
    "amount": "数量",
    "percent": "百分比",
    "power": "战力",
    "tier": "层级", "tiers": "层级",
    "action": "动作", "actions": "动作",
    "category": "分类", "categories": "分类",
    "setting": "设置", "settings": "设置",
    "custom": "自定义",
    "unique": "唯一",
    "inherit": "继承",
    "inherits": "继承",
    "override": "覆盖", "overrides": "覆盖",
    "modify": "修改", "modifies": "修改",
    "remove": "移除", "removes": "移除",
    "add": "添加", "adds": "添加",
    "execute": "执行", "executes": "执行",
    "apply": "应用", "applies": "应用",
    "require": "需要", "requires": "需要", "required": "必需",
    "optional": "可选",
    "support": "支持", "supported": "支持",
    "include": "包含", "includes": "包含",
    "exclude": "排除", "excludes": "排除",
    "ignore": "忽略",
    "match": "匹配", "matches": "匹配",
    "filter": "过滤", "filters": "过滤",
    "return": "返回", "returns": "返回",
    "result": "结果", "results": "结果",
    "message": "消息", "messages": "消息",
    "error": "错误", "errors": "错误",
    "check": "检查", "checks": "检查",
    "fire": "触发",
    "fires": "触发",
    "target": "目标",
    "targets": "以...为目标",
    "mode": "模式",
    "boolean": "布尔值",
    "integer": "整数",
    "string": "字符串",
    "array": "数组",
    "list": "列表",
    "table": "表",
    "tree": "树",
    "slot": "栏位", "slots": "栏位",
    "score": "分数",
    "token": "令牌",
    "currency": "货币",
    "fov": "视野",
    "aidanger": "AI 危险度",
    "threat": "仇恨",
    "combat": "战斗",
    "lightning": "闪电",
    "lightning bolt": "闪电",
    "NONE": "无",
}

# ============================================================
# 句子级翻译规则 (regex pattern → replacement)
# ============================================================
SENTENCE_RULES = [
    # --- 目标选择器核心模式 ---
    (r'^Targets the (.+?) of the caster\.?$', r'以施法者的\1为目标。'),
    (r'^Targets the (.+?) of the target\.?$', r'以目标的\1为目标。'),
    (r'^Targets the caster(?: of the mechanic)?\.?$', r'以施法者为目标。'),
    (r'^Targets the mob itself\.?$', r'以生物自身为目标。'),
    (r'^Targets the (.+?)\.?$', r'以\1为目标。'),
    (r'^Targets a (.+?)\.?$', r'以一个\1为目标。'),
    (r'^Targets all (.+?) in a (.+?)\.?$', r'以\2范围内的所有\1为目标。'),
    (r'^Targets all (.+?) in the (.+?)\.?$', r'以\2范围内的所有\1为目标。'),
    (r'^Targets all (.+?) around the (.+?)\.?$', r'以\2周围的所有\1为目标。'),
    (r'^Targets all (.+?) near the (.+?)\.?$', r'以\2附近的所有\1为目标。'),
    (r'^Targets all (.+?) on the (.+?)\.?$', r'以\2上的所有\1为目标。'),
    (r'^Targets all (.+?)\.?$', r'以所有\1为目标。'),
    (r'^Targets no one\.?$', r'不选择任何目标。'),
    (r'^Targets the nearest (.+?)\.?$', r'以最近的\1为目标。'),
    (r'^Targets the origin\.?$', r'以原点为目标。'),
    (r'^Targets the location of (.+?)\.?$', r'以\1的位置为定位点。'),
    (r'^Targets locations? (.+?)\.?$', r'以\1的位置为目标。'),
    (r'^Targets a specific (.+?)\.?$', r'以指定\1为目标。'),

    # --- 条件核心模式 ---
    (r'^Checks if (.+?)\.?$', r'检查\1。'),
    (r'^Checks whether (.+?)\.?$', r'检查是否\1。'),
    (r'^Checks the (.+?) of the (.+?)\.?$', r'检查\2的\1。'),
    (r'^Returns true if (.+?)\.?$', r'若\1，返回 true。'),
    (r'^Returns false if (.+?)\.?$', r'若\1，返回 false。'),
    (r'^Returns the (.+?)\.?$', r'返回\1。'),
    (r'^Returns a (.+?)\.?$', r'返回一个\1。'),
    (r'^Tests if (.+?)\.?$', r'测试是否\1。'),
    (r'^Tests the (.+?)\.?$', r'测试\1。'),

    # --- 触发器核心模式 ---
    (r'^Fires when (.+?)\.?$', r'在以下情况触发：\1。'),
    (r'^Fires on (.+?)\.?$', r'在以下情况触发：\1。'),
    (r'^Triggers when (.+?)\.?$', r'在以下情况触发：\1。'),
    (r'^Triggered when (.+?)\.?$', r'在以下情况触发：\1。'),
    (r'^Executes the skill when (.+?)\.?$', r'在以下情况执行技能：\1。'),
    (r'^Executes a skill when (.+?)\.?$', r'在以下情况执行技能：\1。'),
    (r'^Activates on (.+?)\.?$', r'在以下情况激活：\1。'),
    (r'^Called when (.+?)\.?$', r'在以下情况调用：\1。'),

    # --- 属性描述 ---
    (r'^The (.+?) of the (.+?)(?: to target)?\.?$', r'目标的\2属性为\1。'),
    (r'^The range of the (.+?)\.?$', r'\1的范围。'),
    (r'^The amount of (.+?)\.?$', r'\1的数量。'),
    (r'^The duration of the (.+?)\.?$', r'\1的持续时间。'),
    (r'^The interval of the (.+?)\.?$', r'\1的间隔。'),
    (r'^This is the (.+?) of the (.+?)\.?$', r'这是\2的\1。'),

    # --- 一般陈述 ---
    (r'^This mechanic (.+?)s?\.?$', r'此机制\1。'),
    (r'^This condition (.+?)s?\.?$', r'此条件\1。'),
    (r'^This targeter (.+?)s?\.?$', r'此目标选择器\1。'),
    (r'^This trigger (.+?)s?\.?$', r'此触发器\1。'),
    (r'^This mob (.+?)s?\.?$', r'此生物\1。'),
    (r'^This item (.+?)s?\.?$', r'此物品\1。'),
    (r'^This (.+?) is used to (.+?)\.?$', r'此\1用于\2。'),
    (r'^Used to (.+?)\.?$', r'用于\1。'),
    (r'^Can be used to (.+?)\.?$', r'可用于\1。'),
    (r'^Allows you to (.+?)\.?$', r'允许\1。'),
    (r'^Determines (.+?)\.?$', r'决定\1。'),
    (r'^Defines (.+?)\.?$', r'定义\1。'),
    (r'^Sets (.+?)\.?$', r'设置\1。'),
    (r'^Default is (.+?)\.?$', r'默认值为\1。'),
    (r'^The default value is (.+?)\.?$', r'默认值为\1。'),
    (r'^The default is (.+?)\.?$', r'默认值为\1。'),
    (r'^If (?:set to )?true,? (.+?)\.?$', r'若设为 true，\1。'),
    (r'^If (?:set to )?false,? (.+?)\.?$', r'若设为 false，\1。'),
    (r'^When set to (.+?),? (.+?)\.?$', r'设为\1时，\2。'),

    # --- "no X" / "does not have" ---
    (r'^This (.+?) has no (.+?)\.?$', r'此\1没有\2。'),
    (r'^Has no (.+?)\.?$', r'没有\1。'),

    # --- 别名 ---
    (r'^Available aliases for this (.+?)\.?$', r'此\1的可用别名：'),

    # --- 注意行 ---
    (r'^> (.+?)\.?$', r'> \1。'),
]

# ============================================================
# 内联翻译: 在句子内替换常见英文短语
# ============================================================
INLINE_REPLACE = [
    # 通用
    ("is not", "不是"),
    ("does not have", "没有"),
    ("does not", "不"),
    ("do not", "不要"),
    ("cannot", "不能"),
    ("must be", "必须为"),
    ("should be", "应"),
    ("needs to be", "需要"),
    ("has to be", "必须"),
    ("greater than", "大于"),
    ("less than", "小于"),
    ("equal to", "等于"),
    ("greater than or equal to", "大于或等于"),
    ("less than or equal to", "小于或等于"),
    ("not equal to", "不等于"),
    ("based on", "基于"),
    ("depending on", "取决于"),
    ("instead of", "而非"),
    ("in order to", "为了"),
    ("as well as", "以及"),
    ("such as", "例如"),
    ("for example", "例如"),
    ("for instance", "例如"),
    ("and/or", "和/或"),
    ("at least", "至少"),
    ("at most", "最多"),
    ("more than", "多于"),
    ("whether or not", "是否"),
    ("once per", "每个"),
    ("per tick", "每 tick"),
    ("per second", "每秒"),
    ("per minute", "每分钟"),
    ("the number of", "的数量"),
    ("the amount of", "的数量"),
    ("the result of", "的结果"),
    ("the value of", "的值"),
    ("the size of", "的大小"),
    ("the type of", "的类型"),
    ("the name of", "的名称"),
    ("the location of", "的位置"),
    ("the distance from", "与...的距离"),
    ("the distance to", "到...的距离"),
    ("the distance between", "之间的距离"),
    ("the center of", "的中心"),
    ("the origin of", "的原点"),
    ("the target of", "的目标"),
    ("in front of", "在...前方"),
    ("behind the", "在...后方"),
    ("next to", "紧挨"),
    ("close to", "靠近"),
    ("far from", "远离"),
    ("above the", "在...上方"),
    ("below the", "在...下方"),
    ("inside the", "在...内部"),
    ("outside the", "在...外部"),
    ("around the", "在...周围"),
    ("within the", "在...范围内"),
    ("in the same", "在同一个"),
    ("on the ground", "在地面上"),
    ("in the air", "在空中"),
    ("in the water", "在水中"),
    ("in the world", "在世界中"),
    ("on the server", "在服务器上"),
    ("allow you to", "允许"),
    ("allows you to", "允许"),
    ("is used to", "用于"),
    ("are used to", "用于"),
    ("can be used to", "可用于"),
    ("can be used as", "可作为"),
    ("is able to", "能够"),
    ("will be", "将"),
    ("will not be", "将不会"),
    ("has been", "已被"),
    ("have been", "已被"),
    ("needs to", "需要"),
    ("has to", "必须"),
    ("makes the", "使"),
    ("causes the", "导致"),
    ("prevents the", "阻止"),
    ("is a way to", "是一种"),
    ("There is no", "没有"),
    ("There are no", "没有"),
    ("there is no", "没有"),
    ("there are no", "没有"),
    ("each time", "每次"),
    ("every time", "每次"),
    ("the first time", "首次"),
    ("the second time", "第二次"),
    ("the last time", "最后一次"),
    ("at the same time", "同时"),
    ("at any time", "随时"),
    ("at that time", "当时"),
    ("over time", "随时间"),
    ("from time to time", "偶尔"),
    ("most of the time", "大多数时候"),
    ("after a short time", "短暂之后"),
    ("right after", "紧接"),
    ("as long as", "只要"),
    ("only if", "仅当"),
    ("if and only if", "当且仅当"),
    ("provided that", "前提是"),
    ("unless the", "除非"),
    ("with the exception of", "除了"),
    ("with respect to", "关于"),
    ("with regard to", "关于"),
    ("in addition to", "除了...之外"),
    ("in case of", "如果"),
    ("in terms of", "在...方面"),
    ("a variety of", "多种"),
    ("a range of", "一系列"),
    ("a list of", "一系列"),
    ("a set of", "一组"),
    ("a group of", "一组"),
    ("a couple of", "几个"),
    ("a few", "几个"),
    ("due to", "由于"),
    ("because of", "因为"),
    ("in contrast to", "与...相对"),
    ("similar to", "与...类似"),
    ("identical to", "与...相同"),
    ("different from", "与...不同"),
    ("the same as", "与...相同"),
    ("the opposite of", "与...相反"),
    ("capable of", "能够"),
    ("incapable of", "不能"),
    ("associated with", "关联的"),
    ("related to", "相关的"),
    ("responsible for", "负责"),
    ("compatible with", "兼容"),
    ("compared to", "与...相比"),
    ("considered as", "被视为"),
    ("referred to as", "被称为"),
    ("known as", "被称为"),
    ("also known as", "也称为"),
    ("divided by", "除以"),
    ("multiplied by", "乘以"),
    ("added to", "加上"),
    ("subtracted from", "减去"),
    ("powered by", "由...驱动"),
    ("made of", "由...制成"),
    ("consists of", "由...组成"),
    ("consisting of", "组成"),
    ("composed of", "组成"),
    ("regardless of", "无论"),
    ("no matter what", "无论如何"),
    ("in any case", "无论如何"),
    ("in all cases", "在所有情况下"),
    ("in most cases", "在大多数情况下"),
    ("in some cases", "在某些情况下"),
    ("in this case", "在此情况下"),
    ("in that case", "在那种情况下"),
    ("in either case", "无论哪种情况"),
    ("on the other hand", "另一方面"),
    ("in the meantime", "同时"),
    ("in the future", "未来"),
    ("in the past", "过去"),
    ("in the present", "当前"),
    ("by default", "默认情况下"),
    ("by means of", "通过"),
    ("in response to", "响应"),
    ("with each", "每"),
    ("per each", "每"),
    ("for each", "每个"),
    ("at a time", "一次"),
    ("in a row", "连续"),
    ("in total", "总共"),
    ("to begin with", "首先"),
    ("to start with", "首先"),
    ("to sum up", "总结"),
    ("as follows", "如下"),
    ("as shown below", "如下所示"),
    ("as shown above", "如上所示"),
    ("as mentioned", "如前所述"),
    ("as expected", "如预期"),
    ("as usual", "照常"),
    ("as always", "一如既往"),
    ("as soon as", "一旦"),
    ("as much as", "尽可能多"),
    ("as little as", "尽可能少"),
    ("as many as", "多达"),
    ("as far as", "就...而言"),
    # possessive / links
    ("on the left", "在左侧"),
    ("on the right", "在右侧"),
    ("on the top", "在顶部"),
    ("on the bottom", "在底部"),
    ("able to be", "可以"),
    ("intended to be", "旨在"),
    ("designed to be", "设计用于"),
    ("meant to be", "意为"),
    ("meant for", "专为"),
    ("built for", "专为"),
    ("suitable for", "适用于"),
    ("available for", "可用于"),
    ("account for", "占"),
    ("takes into account", "考虑"),
    ("taking into account", "考虑到"),
    ("without taking into account", "不考虑"),
    ("without the need for", "无需"),
    ("no longer", "不再"),
    ("at no point", "从未"),
    ("at any point", "任何时候"),
    ("at that point", "此时"),
    ("at this point", "此时"),
    ("at the moment", "此刻"),
    ("at present", "目前"),
    ("currently", "目前"),
    ("from now on", "从现在开始"),
    ("until then", "在此之前"),
    ("so far", "到目前为止"),
    ("up to now", "到目前为止"),
    ("up until now", "目前为止"),
    ("up to this point", "到此为止"),
    ("as well", "也"),
    ("as well", "也"),
    ("either way", "无论如何"),
    ("one way or another", "无论如何"),
    ("all the time", "一直"),
    ("some of the time", "有时"),
    ("none of the time", "从不"),
    ("most of which", "其中大多数"),
    ("some of which", "其中一些"),
    ("each of which", "每个"),
    ("any of which", "任意一个"),
    ("none of which", "没有一个"),
    ("instead of", "而不是"),
    ("rather than", "而不是"),
    # these specific patterns
    ("at the location", "在该位置"),
    ("near the location", "在该位置附近"),
    ("from the location", "从该位置"),
    ("to the location", "到该位置"),
    ("towards the location", "朝向该位置"),
    ("away from the location", "远离该位置"),
    ("has the tag", "带有标签"),
    ("has the aura", "带有光环"),
    ("has the effect", "带有效果"),
    ("has the permission", "拥有权限"),
    ("has the item", "拥有物品"),
    ("on the ground", "在地面上"),
    ("on the server", "在服务器上"),
    ("by the player", "由玩家"),
    ("by the caster", "由施法者"),
    ("by the mob", "由生物"),
    ("for the player", "为玩家"),
    ("for the mob", "为生物"),
    ("for the caster", "为施法者"),
    ("to the player", "给玩家"),
    ("to the mob", "给生物"),
    ("to the target", "给目标"),
    ("from the player", "来自玩家"),
    ("from the mob", "来自生物"),
    ("with the player", "与玩家"),
    ("with the mob", "与生物"),
    # specific mob patterns
    ("will strike", "将击出"),
    ("will spawn", "将生成"),
    ("will teleport", "将传送"),
    ("will damage", "将伤害"),
    ("will heal", "将治疗"),
    ("will activate", "将激活"),
    ("will trigger", "将触发"),
    ("will fire", "将触发"),
    ("will execute", "将执行"),
    ("will remove", "将移除"),
    ("will add", "将添加"),
    ("will set", "将设置"),
    ("will only", "只会"),
    ("will not", "不会"),
    ("will never", "永远不会"),
    ("will always", "总会"),
    ("will sometimes", "有时会"),
    ("will occasionally", "偶尔会"),
    ("will automatically", "将自动"),
    ("will immediately", "将立即"),
    ("will eventually", "最终会"),
    ("will no longer", "将不再"),
    ("will still", "仍会"),
    ("will instead", "将改为"),
    ("will target", "将选择"),
    # negation patterns
    ("may not", "可能不会"),
    ("might not", "可能不会"),
    ("could not", "无法"),
    ("should not", "不应"),
    ("would not", "不会"),
    ("did not", "未"),
    ("doesn't", "不"),
    ("don't", "不要"),
    ("won't", "不会"),
    ("can't", "不能"),
    ("couldn't", "无法"),
    ("shouldn't", "不应"),
    ("wouldn't", "不会"),
    ("isn't", "不是"),
    ("aren't", "不是"),
    ("wasn't", "不是"),
    ("weren't", "不是"),
    ("hasn't", "尚未"),
    ("haven't", "尚未"),
    ("hadn't", "尚未"),
]

# ============================================================
# 章节标题映射
# ============================================================
HEADER_TRANSLATIONS = {
    "description": "描述",
    "attributes": "属性",
    "attribute": "属性",
    "examples": "示例",
    "example": "示例",
    "usage": "用法",
    "syntax": "语法",
    "parameters": "参数",
    "options": "选项",
    "option": "选项",
    "notes": "注意",
    "note": "注意",
    "tips": "提示",
    "tip": "提示",
    "warning": "警告",
    "warnings": "警告",
    "configuration": "配置",
    "requirements": "需求",
    "installation": "安装",
    "setup": "设置",
    "overview": "概述",
    "introduction": "介绍",
    "summary": "总结",
    "details": "详情",
    "see also": "另请参阅",
    "related": "相关",
    "troubleshooting": "故障排除",
    "common issues": "常见问题",
    "faq": "常见问题",
    "changelog": "更新日志",
    "advanced": "高级",
    "basic": "基础",
    "general": "通用",
    "aliases": "别名",
    "alias": "别名",
    "implementations": "实现",
    "implementation": "实现",
    "properties": "属性",
    "property": "属性",
    "fields": "字段",
    "field": "字段",
    "format": "格式",
    "flags": "标志",
    "flag": "标志",
    "return": "返回值",
    "return value": "返回值",
    "return type": "返回类型",
    "type": "类型",
    "name": "名称",
    "values": "可选值",
    "value": "值",
    "modifiers": "修正值",
    "modifier": "修正值",
    "colors": "颜色",
    "color": "颜色",
    "styles": "样式",
    "style": "样式",
    "customization": "自定义",
    "behavior": "行为",
    "behaviors": "行为",
    "restrictions": "限制",
    "restriction": "限制",
    "loot table": "战利品表",
    "loot tables": "战利品表",
}

# ============================================================
# 翻译函数
# ============================================================

def translate_content(content):
    """Translate markdown content"""
    lines = content.split('\n')
    result = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        if not line.strip():
            result.append(line)
            continue

        translated = translate_line(line.strip())
        if line.startswith(' ') or line.startswith('\t'):
            indent = line[:len(line) - len(line.lstrip())]
            result.append(indent + translated)
        else:
            result.append(translated)

    return '\n'.join(result)


def translate_line(line):
    """Translate a single line"""

    # Markdown headers
    m = re.match(r'^(#{1,6})\s+(.+)$', line)
    if m:
        hashes, text = m.groups()
        # Try header translation first
        lower = text.strip().lower()
        if lower in HEADER_TRANSLATIONS:
            return f"{hashes} {HEADER_TRANSLATIONS[lower]}"
        trans = translate_full_text(text)
        return f"{hashes} {trans}"

    # Horizontal rule / table separator
    if re.match(r'^[\-\| :]+$', line):
        return line

    # Markdown links - translate text, keep URL
    line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  lambda m: f"[{translate_full_text(m.group(1))}]({m.group(2)})",
                  line)

    # Save inline code
    code_map = {}
    for i, code in enumerate(re.findall(r'`([^`]+)`', line)):
        placeholder = f"__CODE_{i}__"
        code_map[placeholder] = code
        line = line.replace(f'`{code}`', f'`{placeholder}`', 1)

    text = line

    # Check YAML-like line
    m_yaml = re.match(r'^(\s*)([\w-]+)(\s*:\s*)(.*?)$', text)
    if m_yaml:
        indent, key, colon, value = m_yaml.groups()
        # Skip if key contains spaces or special chars (not a YAML key)
        key_clean = key.strip()
        if key_clean and not any(c in key_clean for c in [' ', '.', ',', '!', '(', ')', '[', ']', '<', '>', "'", '"', '*', '|']):
            if value.strip():
                new_value = translate_full_text(value.strip())
                text = f"{indent}{key}{colon}{new_value}"
            else:
                text = f"{indent}{key}{colon}"
        else:
            text = translate_full_text(text)
    else:
        text = translate_full_text(text)

    # Restore inline codes
    for placeholder, code in code_map.items():
        text = text.replace(f'`{placeholder}`', f'`{code}`')

    return text


def translate_full_text(text):
    """Translate full English text to Chinese"""
    result = text

    # Try sentence-level patterns first (full line match for short lines)
    for pattern, replacement in SENTENCE_RULES:
        m = re.match(pattern, result, re.IGNORECASE)
        if m:
            try:
                # Apply term translation to captured groups
                groups = [translate_simple_terms(g) if '{' not in replacement.split('\\')[0] else g
                          for g in m.groups()]
                return replacement.format(*groups) if '{' in replacement else re.sub(pattern, replacement, result, flags=re.IGNORECASE)
            except:
                pass

    # Apply inline phrase replacements
    for eng, chn in INLINE_REPLACE:
        pattern = re.escape(eng)
        result = re.sub(pattern, chn, result, flags=re.IGNORECASE)

    # Apply term translations (word-level)
    result = translate_simple_terms(result)

    # Cleanup
    result = cleanup(result)

    return result


def translate_simple_terms(text):
    """Apply word-level term translations"""
    result = text
    # Sort by length descending
    sorted_terms = sorted(TERMS.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, chn in sorted_terms:
        pattern = r'\b' + re.escape(eng) + r'\b'
        result = re.sub(pattern, chn, result, flags=re.IGNORECASE)
    return result


def cleanup(text):
    """Clean up translation artifacts"""
    # Remove duplicate words
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)
    # Fix possessive 's patterns
    text = re.sub(r"'s\b", '', text)
    text = re.sub(r"s'\b", '', text)
    # Remove trailing English possessives mixed with Chinese
    text = re.sub(r"的\s+的", "的", text)
    # Clean redundant spaces
    text = re.sub(r' {2,}', ' ', text)
    # Clean leading/trailing spaces
    text = text.strip()
    return text


def process_file(src, dst):
    """Read, translate, write"""
    try:
        # Try UTF-8 first, fall back to latin-1
        try:
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(src, 'r', encoding='latin-1') as f:
                content = f.read()
            # Replace smart quotes
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
    """Process all .md files in directory tree"""
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
