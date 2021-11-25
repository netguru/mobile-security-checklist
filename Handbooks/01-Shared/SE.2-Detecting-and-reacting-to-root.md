# Requirement
## [MSTG-RESILIENCE-1](https://mobile-security.gitbook.io/masvs/security-requirements/0x15-v8-resiliency_against_reverse_engineering_requirements)
The app detects and reacts to the presence of a rooted or jailbroken device either by alerting the user or terminating the app.

## Risk
Running your application on a rooted or jailbroken device may cause some serious issues like for example leaking sensitive data or even reverse engineer of the code. Based on requirements and project specification app should at least be aware of that and act in proper way like limiting functionalities or terminating itself if needed.

## When you need it
When you want your app to behave in a specific way when running on rooted device. For example to increase protection against revers engineering or when it stores some sensitive data, like:

- credit card details
- health information
- any personal data which has to be protected

## Problem and desired effect
### Problem:
Application runs on rooted or jailbroken device.

### Desired effect:
Application should inform user about limited functionalities or terminate itself.

## Solution

### Android
Unfortunately there’s no way of determining with 100% sure that application is running on rooted device as there’s a lot of ways to hide or cloak that, due to “unlimited power”. There are tools on the market that can trick root checks and allow user to run apps without disabling root, like for example RootCloak.

Fortunately on the other side of the fence there are tools that are doing everything they can to correctly detect if the device is rooted or not, one of them is RootBeer.

Because of that let me explain two options for detecting root, a basic one and a 3rd party library one.

**Option 1: Basic root detection**

Check for test keys in build properties:
```kotlin
private fun isRooted(): Boolean = Build.TAGS.contains("test-keys")

class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        if (isRooted()) {
            // root detected, proceed accordingly
            Toast.makeText(this, "This device IS rooted", Toast.LENGTH_SHORT).show()
        }
    }
}
```

**Option 2: Using [RootBeer](https://github.com/scottyab/rootbeer) library**

Add required dependency to *app/build.gradle*:
```kotlin
implementation 'com.scottyab:rootbeer-lib:0.0.8'
```
Check for root status for example in SplashActivity:
```kotlin
class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val rootBeer = RootBeer(this)
        if (rootBeer.isRooted()) {
            // root detected, proceed accordingly
            Toast.makeText(this, "This device IS rooted", Toast.LENGTH_SHORT).show()
        }
    }
}
```

### iOS
Please keep in mind that situation is similar here as on Android, there’s pretty much no way to be absolutely sure that device is jailbroken. Every project team should discuss requirements with client and decide if they need a basic solution or a more complex one. It has to be said that it’s **recommended to use paid solutions** when jailbreak detection is really needed, otherwise below basic check can be enough but please keep in mind that it can be easily bypassed.

One of the recommended free OpenSource solutions can be found at [IOSSecuritySuite](https://github.com/securing/IOSSecuritySuite/blob/master/IOSSecuritySuite/JailbreakChecker.swift), when it comes to paid ones [Guardsquare](https://www.guardsquare.com/en) should be taken into consideration.

Helper used to detect jailbroken device which implements three basic checks:
- files check
- url check
- outside sandbox write check
```swift
enum JailbreakChecker {

    // Check if files created during jailbreaking process are present on the device.
    static var hasJailbrokenFiles: Bool {
        ![
            "/Applications/Cydia.app",
            "/Library/MobileSubstrate/MobileSubstrate.dylib",
            "/bin/bash",
            "/usr/sbin/sshd",
            "/etc/apt",
            "/usr/bin/ssh",
            "/private/var/lib/apt/",
        ]
        .map { fileManager.fileExists(atPath: $0) }
        .filter { $0 }
        .isEmpty
    }

    // Check if URL scheme for Cydia manager is configured on the device.
    static var canOpenJailbrokenURL: Bool {
        guard let url = URL(string: "cydia://package/com.example.package") else { return false }
        return UIApplication.shared.canOpenURL(url)
    }

    // Check if you can write to files outside of application sandbox.
    static var canWriteOutsideSandbox: Bool {
        try? "jailbreak_test".write(toFile: "/private/jailbreak.txt", atomically: true, encoding: .utf8) != nil
    }

}
```
Example usage to show dialog when device is jailbroken:
```swift
guard !JailbreakChecker.hasJailbrokenFiles && !JailbreakChecker.canOpenJailbrokenURL && !JailbreakChecker.canWriteOutsideSandbox else {
    let alertController = UIAlertController(title: "Jailbreak detected", message: "This device IS jailbroken.", preferredStyle: .alert)
    present(alertController, animated: true, completion: nil)
    return
    // Stop loading of the application.
}
```

### React Native
Same story as above so project team should discuss requirements and decide how crucial root detection is for their use case. When it’s really needed then some paid solutions should be taken into consideration, when basic check is enough one of popular ways is to use [jail-monkey](https://github.com/GantMan/jail-monkey). Another possible way is to use a native solutions described above, for example if you already have it implemented that’s a nice option.

First of all you need to install jail-monkey using below commands:
```
npm i jail-monkey --save
react-native link
```

Usage is pretty simple, just import it and use as below:
```javascript
import JailMonkey from 'jail-monkey'
import {
    ToastAndroid,
    Platform,
    AlertIOS,
} from 'react-native';


if (JailMonkey.isJailBroken()) {
    if (Platform.OS === 'android') {
        ToastAndroid.show("This device IS rooted!", ToastAndroid.SHORT)
    } else {
        AlertIOS.alert("This device is rooted!");
    }
}
```

## Testing guide
### Description
App will show a message based on rooted state.

### Example scenario:
Open app on a rooted/jailbroken device and a normal one to notice different messages.

### Tools needed:
Rooted/Jailbroken and normal device with installed application.

### How to:
- Install and open app on a normal device — notice no message being displayed.
- Install and open app on a rooted/jailbroken device — notice message saying “This device IS rooted/jailbroken”.

## Additional resources
- https://medium.com/@deekshithmoolyakavoor/root-detection-in-android-device-9144b7c2ae07
- https://medium.com/secarmalabs/comparison-of-different-android-root-detection-bypass-tools-8fd477251640
- https://www.xda-developers.com/root/ — root directory with guides how to root specific device
- https://www.digitaltrends.com/mobile/how-to-jailbreak-your-iphone/
- https://medium.com/better-programming/how-to-make-ios-app-secure-from-jailbroken-device-1efccc736d9b
- https://github.com/ProteGO-Safe/ios/blob/e84c068209abd6390c4ac5b2ff06a24135b92cb4/safesafe/Services/JailbreakService.swift — example jailbreak detection implementation
- https://github.com/GantMan/jail-monkey
- https://mobile-security.gitbook.io/masvs/security-requirements/0x15-v8-resiliency_against_reverse_engineering_requirements
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md#jailbreak-detection-mstg-resilience-1
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md#testing-root-detection-mstg-resilience-1
