MythicMobs 有[很多指令]。虽然所有指令都有各自的用途，但在深入之前你可能想先了解最有用的那些，本指南正是为此而生！

# 重载插件
`/mm reload`  
不重载的话，你的所有改动都不会生效！

# 基础指令
### 生成生物
`/mm mobs spawn [生物类型]`  
允许你生成指定的生物
### 移除生物
`/mm mobs kill [生物类型]` 击杀指定的生物类型
`/mm mobs killall` 击杀所有非持久性生物
`/mm mobs killall <半径>` 击杀半径范围内的所有非持久性生物
### 获取物品
`/mm items get [物品名]`  
获取指定的物品

# 实用指令
### 调试级别
`/mm debug [级别]`  
啊，独一无二的调试指令！它允许根据传递的级别参数在控制台打印出正在执行的技能和事件的更多信息（使用 `/mm debug 4` 将显示"最高 4 级"的调试消息，而 `/mm debug 0` 会禁用所有调试消息）
### 列出活跃生物
`/mm mobs listactive <生物类型>`  
允许你列出所有活跃生物，可选择按生物类型筛选，并获取条目的更多信息、传送到它们位置或击杀/移除它们
### 获取坐标
`/mm utilities getcoordinates`  
允许你获取当前位置、指针对准位置和目标的格式化坐标
### 获取物品信息
`/mm utilities getiteminfo`  
允许你查看手持物品上存在的所有 NBT 数据
### 获取路径
`/mm utilities getpathstring`  
使用此指令可以放置方块并获取坐标列表，可用于 patrol AI 目标或类似场景
### 列出所有实体
`mm utilities listallentities <半径/生物类型>`  
允许你列出所有实体，可按距离或类型进行筛选

**[>> 第五步](/Guides/(Step-5)-Extra-Notes)**
