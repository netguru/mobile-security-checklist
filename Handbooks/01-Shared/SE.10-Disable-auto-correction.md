# Requirement
## [Application Security Verification Standard 3.0.1 (Paragraph 9.1)](https://owasp.org/www-pdf-archive/OWASP_Application_Security_Verification_Standard_3.0.1.pdf)
Disable auto-correction in sensitive inputs

## Risk
All sensitive information can be cached or added to a dictionary if not secured properly. Currently auto-correction is a very common feature used by most of available keyboards across platforms. It’s very useful but it can also cause data leaks as they’re often stored in cache which can be accessed without any additional permissions.

## When you need it
When your app contains inputs that are meant to collect passwords, pins or other sensitive data.

## Problem and desired effect
### Problem:
Passwords, pins or other sensitive data can be stored in cache and accessed without any permissions.

### Desired effect:
Any sensitive data should not be cached for auto-correction purposes.

## Solution
Review input fields and disable auto-correct feature for all sensitive data, not only passwords but also pins, medical data etc. If aiming for maximum protection, like in banking app for example, please consider implementing your own password/pin input, or even a custom keyboard depending on requirements.

### Android
Android has open approach when it comes keyboards so please keep in mind that some settings can be ignored by some implementations or manufacturers. Default way to disable auto-correction is to use `textNoSuggestions` input type like below:
```xml
<EditText
    android:id="@+id/sensitiveEt"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textNoSuggestions" />
```
Stronger way is to use `textVisiblePassword` input type, but that can have some unexpected behavior in some cases, so it should be used with care as a last resort.
```xml
<EditText
    android:id="@+id/sensitiveEt"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textVisiblePassword" />
```
Recommended way is to use a proper input type based on field requirements, or like mentioned above, implement an own input if really needed.

### iOS
To disable auto-correction you should set `autocorrectionType` as follows:
```cpp
sensitiveTF.autocorrectionType = UITextAutocorrectionTypeNo;
```
Swift solution below:
```swift
sensitiveTF.autocorrectionType = .no
```

### React Native
Just add below line in the `<TextInput>` as follows:
```javascript
<TextInput
//...
autoCorrect={false} />
```

## Testing guide
### Description
App will not suggest or correct previously entered sensitive data.

### Example scenario:
Enter some sensitive word into properly configured input field, switch fields and notice that keyboard won’t suggest to use it or correct any similar one to match it.

### Tools needed:
Platform based device with installed app.

### How to:
- Run the app.
- Enter some text in configured input field.
- Switch fields or apps.
- Start entering the same or similar text - notice that keyboard will not suggest or autocomplete it.

## Additional resources
- https://books.nowsecure.com/secure-mobile-development/en/caching-logging/be-aware-of-the-keyboard-cache.html
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#finding-sensitive-data-in-the-keyboard-cache-mstg-storage-5
- https://mobile-security.gitbook.io/masvs/security-requirements/0x07-v2-data_storage_and_privacy_requirements
