# Requirement
Libraries are linked statically to increase the difficulty level of reverse engineering.

## Risk
If application contains sensitive libraries like security checks (Jailbreak detection), networking, payments, etc.
It will be much easier to change their code while they are linked dynamicly.

### Example of dynamically linked library
Application is using external library to check multiple anti-tampering defenses.

Library is dynamically linked to the project and stores it as separate directory and binary file:

<img width="239" alt="SecurityChecksLibrary" src="https://user-images.githubusercontent.com/57398986/145821852-4285d6f0-7b2a-442d-aba4-3191411e59c6.png">

Framework content:

<img width="187" alt="SecurityChecksLibrary-Directory" src="https://user-images.githubusercontent.com/57398986/145822028-fc718b19-43f8-4d20-9bad-6f0f9587ad97.png">

Attackers can easily prepare a version of SecurityChecksLibrary which will always return false in case of detecting strange behaviour for Jailbreak detection.

After replacing the library with the compromised version, the application will no longer have protections checked by this library, because the attacker hardcoded all checks.

## When you need it
When you would like to protect your application against reverse engineering. 
It can be easily implemented by just changing one line of code for Cocoapods so it would be a nice improvement for any application.

## Problem and desired effect
### Problem:
Easy replacement of dynamically linked sensitive library.

### Desired effect:
Attacker is not able to easily replace implementation of used library.

## Solution
Link libraries in a static way, they will be compiled into a single binary file. In the result application should have a single binary file instead of separate files for every library.

### Cocoapods

Add linkage static option in Podfile to your main target, for test target you can use dynamic linkage. 

`use_frameworks! :linkage => :static`

If you have warnings about “Multiple targets match implicit dependency for linker flags” check if you have only one reference to every library. If target is not specified for example for cocoapods-keys it will generate a static library for the main target and a dynamic one for test target.

### Swift Package Manager

Swift Package Manager uses static linking by default, so there’s no need for any changes while using it.

#### Carthage

Adding libraries with static linkage is quite hard, there is no support by default. However there are some workarounds that may or may not work, so this section is being skipped.

## Testing guide
### Description
External libraries are linkedin staticly and build inside the app file.

### Example scenario:
Application is using external libraries using for example Cocoapods.

### How to:
1. Download project ipa file
2. Unzip it using command `unzip projectName.ipa`
3. Open directory with unzipped project
4. Open project package contents

   <img width="451" alt="project-package-contents" src="https://user-images.githubusercontent.com/57398986/145824822-9cf61476-0edd-44ea-87a8-1a9fdd6c6972.png">
6. Verify if the “Framework” directory contains third party libraries. It should not, it should only contain linked Apple libraries.

## Additional resources
- https://blog.krzyzanowskim.com/2018/12/05/rpath-what/
- https://www.swift.org/package-manager/
- https://cocoapods.org/
- https://docs.gradle.org/current/javadoc/org/gradle/nativeplatform/Linkage.html
