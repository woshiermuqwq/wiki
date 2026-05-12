Java文档
--------

Mythic API 的 JavaDoc 可在此处找到：

1.  <https://www.mythiccraft.io/javadocs/mythic/>

-------------------------
## 仓库

#### Maven
```xml
<repository>
    <id>nexus</id>
    <name>Lumine Releases</name>
    <url>https://mvn.lumine.io/repository/maven-public/</url>
</repository>
```
#### Gradle (Groovy)
```groovy
repositories {
    // ...
    mavenCentral()
    maven { url 'https://mvn.lumine.io/repository/maven-public/' }
}
```
#### Gradle (Kotlin)
```kotlin
repositories {
    // ...
    mavenCentral()
    maven(url = "https://mvn.lumine.io/repository/maven-public/")
}
```

## 依赖
#### Maven
```xml
<dependency>
    <groupId>io.lumine</groupId>
    <artifactId>Mythic-Dist</artifactId>
    <version>5.6.1</version>  
    <scope>provided</scope>
</dependency>
```
#### Gradle (Groovy)
```groovy
dependencies {
    //...
    compileOnly 'io.lumine:Mythic-Dist:5.6.1'
}
```
#### Gradle (Kotlin)
```kotlin
dependencies {
    // ...
    compileOnly("io.lumine:Mythic-Dist:5.6.1")
}
```
--------------------------

示例
--------
MythicMobs API 包含众多事件和辅助类，帮助你利用我们的生物、物品和技能系统。

以下是一些入门示例：

1.  [MythicMobs API 示例仓库](https://github.com/xikage/MythicMobs-API-Examples)

### 生成一个 MythicMob

```java
MythicMob mob = MythicBukkit.inst().getMobManager().getMythicMob("SkeletalKnight").orElse(null);
Location spawnLocation = player.getLocation();
if(mob != null){
    // 生成生物            
    ActiveMob knight = mob.spawn(BukkitAdapter.adapt(spawnLocation),1);
    
    // 将生物作为 Bukkit 实体获取
    Entity entity = knight.getEntity().getBukkitEntity();
}
```

### 检查 Bukkit 实体是否为 MythicMob
```java
Entity bukkitEntity = ...;
boolean isMythicMob = MythicBukkit.inst().getMobManager().isMythicMob(bukkitEntity);
if(isMythicMob){
    // ...             
}
```

### 从 Bukkit 实体获取 ActiveMob 实例
```java
Entity bukkitEntity = ...;
Optional<ActiveMob> optActiveMob = MythicBukkit.inst().getMobManager().getActiveMob(bukkitEntity.getUniqueId());
optActiveMob.ifPresent(activeMob -> {
    //...
}).orElse(() -> /* ... */);
```

### 使用谓词获取 ActiveMob 集合
```java
Collection<ActiveMob> activeMobs = MythicBukkit.inst().getMobManager().getActiveMobs(am -> am.getMobType().equals("SkeletalKnight"));
```
