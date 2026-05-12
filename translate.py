#!/usr/bin/env python3
"""MythicMobs Wiki 文档汉化脚本 - 批量翻译 .md 文件"""

import os, re, sys

# ============================================================
# 术语表 (term -> Chinese translation)
# ============================================================
TERMS = {
    # 核心概念
    "mob": "生物", "mobs": "生物",
    "skill": "技能", "skills": "技能",
    "mechanic": "机制", "mechanics": "机制",
    "condition": "条件", "conditions": "条件",
    "targeter": "目标选择器", "targeters": "目标选择器",
    "trigger": "触发器", "triggers": "触发器",
    # 角色
    "caster": "施法者", "target": "目标", "origin": "原点/起效点",
    "parent": "父级", "child": "子级", "children": "子级",
    # 行为
    "spawn": "生成", "despawn": "消失",
    "faction": "阵营", "factions": "阵营",
    "threat table": "仇恨表", "threat tables": "仇恨表",
    "immunity table": "免疫表", "immunity tables": "免疫表",
    # 模板变量
    "template": "模板", "templates": "模板",
    "metaskill": "元技能", "metaskills": "元技能",
    "placeholder": "占位符", "placeholders": "占位符",
    "variable": "变量", "variables": "变量",
    # 原版
    "vanilla": "原版", "vanilla mob": "原版生物",
    "config": "配置", "permission": "权限", "command": "指令", "commands": "指令",
    # 战斗
    "damage": "伤害", "HP": "生命值", "Health": "血量", "health": "血量",
    "equipment": "装备", "drop": "掉落", "drops": "掉落",
    # 弹射物/粒子
    "projectile": "弹射物", "projectiles": "弹射物",
    "missile": "制导弹射物", "missiles": "制导弹射物",
    "particle": "粒子", "particles": "粒子",
    "aura": "光环", "auras": "光环",
    # 技能参数
    "cooldown": "冷却", "radius": "半径", "chance": "概率",
    "velocity": "速度向量",
    # AI
    "AI goal": "AI 目标", "AI goals": "AI 目标",
    "AI target selector": "AI 目标选择器", "AI target selectors": "AI 目标选择器",
    "goal": "目标", "goals": "目标",
    # 显示
    "bossbar": "Boss血条", "boss bar": "Boss血条",
    "killmessage": "击杀信息", "kill message": "击杀信息",
    "inline": "内联",
    # 伪装/等级
    "disguise": "伪装", "disguises": "伪装",
    "level": "等级", "levels": "等级",
    "power scaling": "战力缩放",
    # 环境
    "biome": "生物群系", "biomes": "生物群系",
    "structure": "结构", "structures": "结构",
    "region": "区域", "regions": "区域",
    "block": "方块", "blocks": "方块",
    # 物品
    "enchantment": "附魔", "enchantments": "附魔",
    "potion": "药水", "potions": "药水",
    "attribute": "属性", "attributes": "属性",
    "lore": "物品描述", "banner": "旗帜",
    # 保留原名
    "MythicMobs": "MythicMobs",
    "ModelEngine": "ModelEngine",
    "Model Engine": "ModelEngine",
    "LibsDisguises": "LibsDisguises",
    "WorldEdit": "WorldEdit",
    "Paper": "Paper",
    "Spigot": "Spigot",
    "Bukkit": "Bukkit",
    # 添加更多
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
    "boss": "Boss", "bosses": "Boss",
    "location": "位置", "locations": "位置",
    "owner": "主人", "owners": "主人",
    "passenger": "乘客", "passengers": "乘客",
    "mount": "坐骑", "mounted": "骑乘状态",
    "vehicle": "载具",
    "spawner": "生成器", "spawners": "生成器",
    "signal": "信号", "signals": "信号",
    "timer": "计时器", "timers": "计时器",
    "charge": "充能",
    "channel": "引导", "channeling": "引导中",
    "effect": "效果", "effects": "效果",
    "option": "选项", "options": "选项",
    "example": "示例", "examples": "示例",
    "note": "注意", "notes": "注意",
    "warning": "警告",
    "tip": "提示", "tips": "提示",
    "alias": "别名", "aliases": "别名",
    "default": "默认值",
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
    "token": "令牌",
    "key": "键",
    "action": "动作", "actions": "动作",
    "category": "分类", "categories": "分类",
    "setting": "设置", "settings": "设置",
    "custom": "自定义",
    "unique": "唯一",
    "clone": "克隆",
    "copy": "复制",
    "paste": "粘贴",
    "inherit": "继承", "inherits": "继承",
    "override": "覆盖", "overrides": "覆盖",
    "modify": "修改", "modifies": "修改",
    "remove": "移除", "removes": "移除",
    "add": "添加", "adds": "添加",
    "create": "创建", "creates": "创建",
    "delete": "删除",
    "enable": "启用", "enabled": "已启用",
    "disable": "禁用", "disabled": "已禁用",
    "activate": "激活", "activated": "已激活",
    "trigger": "触发", "triggered": "已触发",
    "execute": "执行", "executes": "执行",
    "apply": "应用", "applies": "应用",
    "require": "需要", "requires": "需要", "required": "需要",
    "optional": "可选",
    "support": "支持", "supported": "支持",
    "include": "包含", "includes": "包含",
    "exclude": "排除", "excludes": "排除",
    "ignore": "忽略",
    "match": "匹配", "matches": "匹配",
    "filter": "过滤", "filters": "过滤",
    "return": "返回", "returns": "返回",
    "result": "结果", "results": "结果",
    "output": "输出",
    "input": "输入",
    "message": "消息", "messages": "消息",
    "error": "错误", "errors": "错误",
    "warning": "警告", "warnings": "警告",
    "debug": "调试",
    "log": "日志",
    "data": "数据",
    "cache": "缓存",
    "memory": "内存",
    "performance": "性能",
    "optimization": "优化",
    "compatibility": "兼容性",
    "version": "版本", "versions": "版本",
    "update": "更新", "updates": "更新",
    "install": "安装",
    "setup": "设置",
    "guide": "指南", "guides": "指南",
    "tutorial": "教程", "tutorials": "教程",
    "reference": "参考",
    "documentation": "文档",
    "resource": "资源", "resources": "资源",
    "wiki": "Wiki",
    "page": "页面", "pages": "页面",
    "section": "章节", "sections": "章节",
    "list": "列表",
    "table": "表格",
    "description": "描述",
    "usage": "用法",
    "syntax": "语法",
    "pattern": "模式",
    "expression": "表达式", "expressions": "表达式",
    "operation": "运算", "operations": "运算",
    "operator": "运算符", "operators": "运算符",
    "comparison": "比较",
    "equation": "方程式",
    "math": "数学",
    "number": "数字", "numbers": "数字",
    "string": "字符串", "strings": "字符串",
    "boolean": "布尔值",
    "integer": "整数",
    "float": "浮点数",
    "double": "双精度",
    "array": "数组", "arrays": "数组",
    "nested": "嵌套",
    "recursive": "递归",
    "loop": "循环",
    "conditional": "条件判断",
    "branch": "分支",
    "scope": "作用域", "scopes": "作用域",
    "context": "上下文",
    "priority": "优先级",
    "weight": "权重",
    "condition": "条件",
    "true": "true（真）",
    "false": "false（假）",
    "null": "null（空）",
    "enabled": "启用",
    "disabled": "禁用",
    # YAML
    "yaml": "YAML",
    "yml": "YML",
    "json": "JSON",
    "xml": "XML",
    # 分隔符
    "colon": "冒号 (:)",

    # AI goal specific
    "leap at target": "向目标跳跃",
    "melee attack": "近战攻击",
    "arrow attack": "弓箭攻击",
    "bow attack": "弓攻击",
    "crossbow attack": "弩攻击",
    "zombie attack": "僵尸攻击",
    "spider attack": "蜘蛛攻击",
    "creeper swell": "苦力怕膨胀",
    "move through village": "穿过村庄移动",
    "move to block": "移动到方块",
    "move to lava": "移动到熔岩",
    "move to water": "移动到水中",
    "move towards target": "向目标移动",
    "move towards restriction": "向限制区域移动",
    "look at target": "注视目标",
    "look at players": "注视玩家",
    "random stroll": "随机漫步",
    "random fly": "随机飞行",
    "random look around": "随机环顾",
    "random nod": "随机点头",
    "go to location": "前往位置",
    "go to owner": "前往主人",
    "go to parent": "前往父级",
    "go to spawn": "前往生成点",
    "do nothing": "什么都不做",
}

# 区分大小写的术语（需要精确匹配）
CASE_SENSITIVE = {
    # These only apply when the word appears in specific contexts
}

# ============================================================
# 短语翻译表 (longer phrases → translated text)
# ============================================================
PHRASES = {
    # 常见章节标题
    "Description": "描述",
    "Attributes": "属性",
    "Examples": "示例",
    "Example": "示例",
    "Usage": "用法",
    "Syntax": "语法",
    "Parameters": "参数",
    "Options": "选项",
    "Notes": "注意",
    "Tips": "提示",
    "Warning": "警告",
    "Configuration": "配置",
    "Requirements": "需求",
    "Dependencies": "依赖",
    "Installation": "安装",
    "Setup": "设置",
    "Getting Started": "入门",
    "Quick Start": "快速开始",
    "Overview": "概述",
    "Introduction": "介绍",
    "Summary": "总结",
    "Details": "详情",
    "Additional Information": "附加信息",
    "See Also": "另请参阅",
    "Related": "相关",
    "Troubleshooting": "故障排除",
    "Common Issues": "常见问题",
    "FAQ": "常见问题",
    "Changelog": "更新日志",
    "Advanced": "高级",
    "Basic": "基础",
    "General": "通用",

    # 表格头部
    "Attribute": "属性",
    "Aliases": "别名",
    "Type": "类型",
    "Default": "默认",
    "Default Value": "默认值",
    "Return Type": "返回类型",
    "Result Type": "结果类型",
    "Parameter": "参数",
    "Flag": "标志",

    # 扩展属性描述
    "Range": "范围",
    "Duration": "持续时间",
    "Interval": "间隔",
    "Chance": "概率",
    "Radius": "半径",
    "Speed": "速度",
    "Amount": "数量",
    "Percent": "百分比",
    "Repeat": "重复",
    "Repeat Interval": "重复间隔",
    "Cooldown": "冷却",
    "Power": "战力",
    "Level": "等级",
    "FOV": "视野",
    "Y Offset": "Y轴偏移",
    "Y-Offset": "Y轴偏移",
    "YOffset": "Y轴偏移",

    # 常见描述语句
    "Returns the": "返回",
    "Returns a": "返回一个",
    "Checks if": "检查",
    "Checks whether": "检查是否",
    "If true": "若为 true",
    "If false": "若为 false",
    "When true": "当为 true 时",
    "When false": "当为 false 时",
    "Default is": "默认值为",
    "The default value is": "默认值为",
    "The default is": "默认值为",
    "For example": "例如",
    "For instance": "例如",
    "such as": "例如",
    "In this case": "在此情况下",
    "In most cases": "大多数情况下",
    "Can be used to": "可用于",
    "Used to": "用于",
    "Allows you to": "允许",
    "This mechanic": "此机制",
    "This condition": "此条件",
    "This targeter": "此目标选择器",
    "This trigger": "此触发器",
    "This skill": "此技能",
    "This mob": "此生物",
    "This item": "此物品",

    # 触发器描述
    "Fires when": "在以下情况触发：",
    "Fires on": "在以下情况触发：",
    "Trigger when": "在以下情况触发：",
    "Triggered when": "在以下情况触发：",
    "Activates on": "在以下情况激活：",
    "Activated by": "由以下方式激活：",

    # Tab补全
    "Tab Completion": "Tab 补全",
    "Tab-Completion": "Tab 补全",
    "In-Line": "内联",

    # 目标选择器相关
    "Targets the": "以",
    "Targets all": "以所有",
    "Targets a": "以一个",
    "Targets any": "以任意",
    "Targets nearby": "以附近的",
    "Targets entities": "以实体",
    "Targets players": "以玩家",
    "Targets mobs": "以生物",
    "around the": "周围的",
    "within a": "范围内的",
    "at the": "位于",
    "in the": "在",
    "from the": "从",
    "of the": "的",

    # ===== 目标选择器专用短语 =====
    "targets the current caster": "以当前施法者为目标",
    "Targets the caster": "以施法者为目标",
    "Targets the mob itself": "以生物自身为目标",
    "Targets the caster of the mechanic": "以机制的施法者为目标",
    "targets a specific player by their name": "以指定名称的特定玩家为目标",
    "targets all blocks in a radius": "以半径范围内的所有方块为目标",
    "targets all entities in a radius": "以半径范围内的所有实体为目标",
    "targets all players in a radius": "以半径范围内的所有玩家为目标",
    "targets all mobs in a radius": "以半径范围内的所有生物为目标",
    "targets all items in a radius": "以半径范围内的所有物品为目标",
    "targets all entities in a cone": "以锥形范围内的所有实体为目标",
    "targets all entities in a line": "以直线上的所有实体为目标",
    "targets all entities in a ring": "以环形范围内的所有实体为目标",
    "targets all entities in a rectangle": "以矩形范围内的所有实体为目标",
    "targets all entities in a sphere": "以球形范围内的所有实体为目标",
    "targets all entities in a cuboid": "以长方体范围内的所有实体为目标",
    "targets entities near the origin": "以原点附近的实体为目标",
    "targets mobs near the origin": "以原点附近的生物为目标",
    "targets players near the origin": "以原点附近的玩家为目标",
    "targets items near the origin": "以原点附近的物品为目标",
    "targets blocks near the origin": "以原点附近的方块为目标",
    "targets the location of the target": "以目标的位置为定位点",
    "targets the location of the caster": "以施法者的位置为定位点",
    "targets a specific location": "以指定位置为目标",
    "targets the parent of the caster": "以施法者的父级为目标",
    "targets the children of the caster": "以施法者的子级为目标",
    "targets the owner of the caster": "以施法者的主人为目标",
    "targets the mount of the caster": "以施法者的坐骑为目标",
    "targets the vehicle of the caster": "以施法者的载具为目标",
    "Targets the parent": "以父级为目标",
    "Targets the children": "以子级为目标",
    "Targets the owner": "以主人为目标",
    "targets the passenger": "以乘客为目标",
    "Targets the spawn location": "以生成位置为目标",
    "Targets the caster's spawn location": "以施法者的生成位置为目标",
    "targets the threat table": "以仇恨表为目标",
    "targets the trigger": "以触发器为目标",
    "targets the origin": "以原点为目标",
    "Targets no one": "不选择任何目标",
    "targets all players on the server": "以服务器上的所有玩家为目标",
    "targets all players in the world": "以世界中的所有玩家为目标",
    "targets all living entities in the world": "以世界中的所有活体实体为目标",
    "targets all entities in the world": "以世界中的所有实体为目标",
    "targets the target of the target": "以目标的目标为目标",
    "targets a point on a ring": "以环形上的一个点为目标",
    "targets a ring of locations": "以环形位置为目标",
    "Targets the nearest player": "以最近的玩家为目标",
    "targets the nearest structure": "以最近的结构为目标",
    "targets a specific block": "以指定方块为目标",
    "targets all spawners": "以所有生成器为目标",
    "targets the siblings": "以同级为目标",
    "targets the forward location": "以前方位置为目标",
    "targets entities in the forward direction": "以前方方向上的实体为目标",

    # Items
    "Item Builder": "物品构建器",
    "Item Options": "物品选项",

    # Mobs
    "Mob Options": "生物选项",
    "Mob Types": "生物类型",
    "Faction Options": "阵营选项",
    "AI Options": "AI 选项",
    "Threat Table": "仇恨表",
    "Immunity Table": "免疫表",
    "Kill Messages": "击杀信息",
    "Disguise Options": "伪装选项",
    "Display Options": "显示选项",
    "Equipment Options": "装备选项",
    "Damage Modifiers": "伤害修正",
    "Damage Modifier": "伤害修正",
    "Boss Bar": "Boss血条",
    "Power Scaling": "战力缩放",
    "Level Modifiers": "等级修正",

    # Targets
    "Last Target": "上一个目标",
    "Current Target": "当前目标",
    "Nearest Target": "最近目标",
    "Specific Target": "指定目标",

    # 技能元
    "Skill List": "技能列表",
    "Skill Tree": "技能树",
    "Inline Condition": "内联条件",
    "Inline Skill": "内联技能",
    "Inline Mechanic": "内联机制",
    "Dynamic Skill": "动态技能",
    "Dynamic Metaskill": "动态元技能",
    "Placeholder API": "PlaceholderAPI",
    "Intratick Scheduling": "同Tick调度",

    # AI
    "AI Goals": "AI 目标",
    "AI Goal": "AI 目标",
    "AI Targeting": "AI 目标选择",
    "AI Target Selectors": "AI 目标选择器",
    "AI Target Selector": "AI 目标选择器",
    "Custom AI": "自定义 AI",

    # 环境
    "WorldGuard Region": "WorldGuard 区域",
    "WorldGuard regions": "WorldGuard 区域",
    "Block Type": "方块类型",
    "Block Vein": "方块矿脉",
    "Line of Sight": "视线",
    "Field of View": "视野",
    "Bounding Box": "包围盒",

    # 中文标题补充
    "Targeters": "目标选择器",
    "Triggers": "触发器",
    "Conditions": "条件",
    "Mechanics": "机制",
    "Skills": "技能",
    "Mobs": "生物",
    "Items": "物品",
    "Drops": "掉落",
    "Guides": "指南",
    "Changelogs": "更新日志",
    "Config": "配置",
    "API": "API",

    # 更多
    "Mob Name": "生物名称",
    "Mob Type": "生物类型",
    "Health": "血量",
    "Damage": "伤害",
    "Movement Speed": "移动速度",

    # Shape enum
    "Sphere": "球形",
    "Circle": "圆形",
    "Cube": "立方体",
    "Cuboid": "长方体",
    "Cylinder": "圆柱体",
    "Cone": "锥形",
    "Line": "直线",
    "Ring": "环形",
    "Rectangle": "矩形",
    "Wall": "墙体",
    "Cross": "十字形",
    "Dome": "圆顶",
    "Pyramid": "金字塔",
    "Point": "点",
    "Grid": "网格",
    "Custom": "自定义",
}

# ============================================================
# 翻译函数
# ============================================================

def translate_content(content):
    """Translate markdown content from English to Chinese"""

    # Split into lines for processing
    lines = content.split('\n')
    result = []
    in_yaml = False
    in_code_block = False
    yaml_indent = 0

    for line in lines:
        # Detect code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            # Inside code block, don't translate
            result.append(line)
            continue

        # Skip pure blank lines
        if not line.strip():
            result.append(line)
            continue

        # Translate the line
        translated = translate_line(line.strip())
        # Preserve leading whitespace
        if line.startswith(' ') or line.startswith('\t'):
            indent = line[:len(line) - len(line.lstrip())]
            result.append(indent + translated)
        else:
            result.append(translated)

    return '\n'.join(result)


def translate_line(line):
    """Translate a single line of markdown"""

    # ============ Handle Markdown Headers ============
    m = re.match(r'^(#{1,6})\s+(.+)$', line)
    if m:
        hashes, text = m.groups()
        # Translate the header text
        trans = translate_text(text)
        return f"{hashes} {trans}"

    # ============ Handle Markdown Links (don't change URL) ============
    # [text](url) - translate text, keep url
    def replace_link(m):
        text = m.group(1)
        url = m.group(2)
        return f"[{translate_text(text)}]({url})"

    line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, line)

    # ============ Handle Inline Code (don't translate) ============
    # `code` - preserve
    inline_codes = re.findall(r'`([^`]+)`', line)
    # Temporarily replace inline code with placeholders
    code_map = {}
    for i, code in enumerate(inline_codes):
        placeholder = f"__CODE_{i}__"
        code_map[placeholder] = code
        line = line.replace(f'`{code}`', f'`{placeholder}`', 1)

    # ============ Handle YAML keys (don't translate key names) ============
    # Detect potential YAML lines: key: value or key:
    m_yaml = re.match(r'^(\s*)([\w-]+)(\s*:\s*)(.*)$', line)
    is_yaml_line = False
    if m_yaml:
        indent, key, colon, value = m_yaml.groups()
        # Check if this looks like a YAML key (not a regular sentence with colon)
        # YAML keys are typically at start of line (optional indent) with no other punctuation before colon
        if not any(c in key for c in [' ', '.', ',', '?', '!', '(', ')', '[', ']', '<', '>', "'", '"']):
            is_yaml_line = True

    if is_yaml_line:
        # Only translate the value part
        indent, key, colon, value = m_yaml.groups()
        if value.strip():
            trans_value = translate_text(value.strip())
            line = f"{indent}{key}{colon}{trans_value}"
        else:
            # No value, just key
            line = f"{indent}{key}{colon}"
    else:
        # Translate full text line
        line = translate_text(line)

    # Restore inline codes
    for placeholder, code in code_map.items():
        line = line.replace(f'`{placeholder}`', f'`{code}`')

    return line


def translate_text(text):
    """Translate English text to Chinese"""

    result = text

    # Apply phrase translations (longer phrases first)
    # Sort phrases by length descending to match longer phrases first
    sorted_phrases = sorted(PHRASES.items(), key=lambda x: len(x[0]), reverse=True)
    for eng, chn in sorted_phrases:
        if eng in result:
            result = result.replace(eng, chn)

    # Apply term translations (word-level)
    # Use word boundary matching for terms
    for eng, chn in TERMS.items():
        # Match whole word with boundaries
        pattern = r'\b' + re.escape(eng) + r'\b'
        repl_func = lambda m, c=chn: c
        result = re.sub(pattern, repl_func, result, flags=re.IGNORECASE)

    # Fix punctuation: replace English punctuation with Chinese where appropriate
    # (but not within code-related contexts)
    # result = result.replace('. ', '。').replace('! ', '！').replace('? ', '？')

    # Clean up double spaces
    result = re.sub(r'  +', ' ', result)

    # Clean up orphaned possessive patterns like "的的"
    if '的的' in result:
        result = result.replace('的的', '的')

    # Fix specific patterns that appear from term substitution
    replacements = [
        # Clean duplicate "的"
        ("的的", "的"),
        # "在以下情况触发：: the" → "在以下情况触发：the"
        ("触发：: ", "触发："),
        # "的 the" → "的"
        # Fix "of the" patterns
        ("的 的", "的"),
        # Common post-translation fixes
        ("的 the ", "的 "),
        ("的 in ", "在"),
        ("的 at ", "在"),
        ("的 by ", "由"),
        ("的 from ", "从"),
        # Fix "target the" → "以...为目标"
        ("以目标 the", "以"),
    ]
    for old, new in replacements:
        if old in result:
            result = result.replace(old, new)

    return result


def process_file(src, dst):
    """Read source file, translate, write to destination"""
    try:
        with open(src, 'r', encoding='utf-8') as f:
            content = f.read()

        translated = translate_content(content)

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(translated)

        return True
    except Exception as e:
        print(f"ERROR: {src}: {e}", file=sys.stderr)
        return False


def process_directory(src_dir, dst_dir, pattern='*.md'):
    """Process all .md files in a directory tree"""
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


# ============================================================
# 主入口
# ============================================================

def main():
    base_src = "/root/.openclaw/workspace/mythicmobs/MythicMobsWiki-master"
    base_dst = "/root/.openclaw/workspace/mythicmobs-zh"

    # 定义翻译任务
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

    # 翻译 Skills 根目录下的特定文件
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

    # 翻译 Enum/Shape.md
    print(f"\n📁 翻译文件: Enum/Shape.md")
    shape_src = os.path.join(base_src, "Enum", "Shape.md")
    shape_dst = os.path.join(base_dst, "Enum", "Shape.md")
    if os.path.exists(shape_src):
        if process_file(shape_src, shape_dst):
            total += 1
            print(f"  完成")
        else:
            total_errors += 1
    else:
        print(f"  ⚠️ 未找到文件")

    print(f"\n{'='*50}")
    print(f"✅ 翻译完成！总计: {total} 个文件，{total_errors} 个错误")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
