# Requirement
## [MSTG-STORAGE-3](https://mobile-security.gitbook.io/masvs/security-requirements/0x07-v2-data_storage_and_privacy_requirements)
No sensitive data is written to application logs.

## Risk
Sensitive data can be unintentionally exposed through the console logs. Logging information into the console is a common way to debug applications, but should only be done in debug mode, not leaving any trace of information in production application.

Logs can contain different information like descriptions of interaction flows, details of API requests or current user data. This could allow access to sensitive data or allow an easier reverse engineering process.

This risk also applies to events logged via analytics service platforms.

## When you need it
You are creating logs in your application that can contain sensitive information.

## Problem and desired effect
### Problem:
Application logs that can contain sensitive data are visible in production application.

### Desired effect:
No logs with sensitive data are visible while running a live application.

## Solution
Before implementing a solution for each platform on how to use logs without exposing any of the sensitive data take a moment and decide if logs outside debug mode are even needed in your application. If not you could use compiler directives to disable logging code in production builds.

If you really need to have logs enabled on non-debug builds, remember that no solution grants full security to logged information and we can only make the process of compromising such data harder.

### iOS
#### **Disable production logs with preprocessor macro**
Wrap your logging code with preprocessor flag (DEBUG flag is automatically configured for new Xcode projects):
```swift
#if DEBUG
<your logging code>
#endif
```

#### **Mask sensitive data in your logs**
Make sure that logging system that you are using allows to mask data in the logs if the device is not running in debug mode. For example native iOS solution, OSLog, allows us to mark values put into logs as private:
```swift
os_log(.default, log: log, "Current user phone: %{private}@", user.phoneNumber)
```

### Android
Currently the most common logging library for Android is Timber, making sure that no sensitive information is logged in production is as simple as planting a debug tree only in debug mode as described.

In your Application class onCreate method check if BuildConfig is debug and plant the tree, that’s all.
```kotlin
class App : Application() {

    override fun onCreate() {
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        }
    }
}
```

### React Native
Properly configured ESLint should disallow any unwanted logs to be made in our application. Ensure that your configuration include this rule:
```javascript
'no-console': 'error'
```
Additionally to have logs enabled in debug mode you can use following helper that create logs with ESLint rule disabled:
```javascript
global.devLog = (...messages) => __DEV__ && console.log(...messages) // eslint-disable-line no-console, max-len
global.devTron = (...messages) => __DEV__ && console.tron.log(...messages) // eslint-disable-line no-console, max-len
```

### Analytics Services
While logging events to analytics services make sure that only minimal amount of information is saved, eg. id of current user, performed action and application state name. You must not send any sensitive user information to any third-party analytics service.

## Testing guide
### Description
Logs from the production app are not showing any sensitive data.

### Example scenario:
Application performs different API calls.

### Tools needed:
- **iOS**: iPhone, Macbook
- **Android**: Android device, Logcat
- **Analytics**: proper access rights in dashboard panel (depends on analytics service provider)

### How to:
#### **iOS**
- Connect the device with the launched application to your Macbook.
- Launch Console application.
- Filter visible logs with application bundle id.
- Check if any sensitive data is printed into logs while using the application.

#### **Android**
- Connect an Android device to your computer.
- Start using the application.
- Check the application's data directory for any log files (`/data/data/<package-name>`).
- Use Logcat to filter system messages looking for any `println` or `printStackTrace` output.
    ```bash
    adb logcat | grep "$(adb shell ps | grep <package-name> | awk '{print $2}')"
    ```
- Check if any sensitive data is visible in found logs.

#### **React Native**
Follow guides above depending on what device you want to test on.

#### **Analytics Services**
- Log into your analytics dashboard panel.
- Filter collected logs to only show those from production application.
- Validate that no sensitive information is stored.

## Additional resources
- https://www.netguru.com/codestories/ios-logging-practices
- https://reactnative.dev/docs/debugging#debugging-on-a-device-with-chrome-developer-tools
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#checking-logs-for-sensitive-data-mstg-storage-3
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#testing-logs-for-sensitive-data-mstg-storage-3