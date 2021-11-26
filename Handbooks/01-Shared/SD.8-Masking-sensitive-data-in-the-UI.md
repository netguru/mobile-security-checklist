# Requirement
## [MSTG-STORAGE-7](https://mobile-security.gitbook.io/masvs/security-requirements/0x07-v2-data_storage_and_privacy_requirements)
No sensitive data, such as passwords or pins, is exposed through the user interface. You have to use secure text entry for fields.

## Risk
Sensitive data can be leaked to user interface when inputs are not configured properly. It may lead to capturing for example password on a screenshot taken by spy apps. Inputs which may contain data like passwords, pins or other personal data should be masked with dots or asterisks for example.

## When you need it
When your app contains inputs that are meant to collect passwords, pins or other sensitive data.

## Problem and desired effect
### Problem:
Passwords, pins or other sensitive data is exposed to user interface.

### Desired effect:
Passwords, pins or other sensitive data should be masked.

## Solution
Review all input fields used in app to check if their input types are correct based on their purpose. In case of any doubts you can ask your QA as he probably has some knowledge to determine if specific input should be masked or not. What’s more please avoid using real names for layout preview purposes and replace them with John/Jane Doe for example. As last step make sure that no sensitive data is displayed in app as label or other content unless it’s really, really needed.

### Android
Set correct input type based on your requirements:
```kotlin
// for text from xml
android:inputType="textPassword"
// for number from xml
android:inputType="numberPassword"
// for text from code
editText.inputType = InputType.TYPE_TEXT_VARIATION_PASSWORD
// for number from code
editText.inputType = InputType.TYPE_NUMBER_VARIATION_PASSWORD
```
Example of basic password EditText with specified inputType:
```xml
<EditText
    android:id="@+id/passwordEt"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textPassword"
    android:maxLines="1" />
```

### iOS
To enable masking password you should add below line in code:
```swift
passwordTF.isSecureTextEntry = true
```

### React Native
Just add below line in the `<TextInput>` as follows:
```javascript
<TextInput
//...
secureTextEntry={true} />
```
For more information about safety related TextInput properties please check this great article [Sensitive & login/register forms in React Native](https://netguru.atlassian.net/wiki/spaces/RN/pages/915243053)

## Testing guide
### Description
App will mask input in correctly configured input fields.

### Example scenario:
Specify correct input type based on solution and notice that entered text is masked.

### Tools needed:
Platform based device with installed app.

### How to:
- Run the app.
- Enter some text in configured input field — it should be masked now.

## Additional resources
- https://developer.android.com/reference/android/text/InputType
- https://developer.android.com/training/keyboard-input/style
- https://developer.apple.com/documentation/uikit/uitextinputtraits/1624427-issecuretextentry
- [Sensitive & login/register forms in React Native](https://netguru.atlassian.net/wiki/spaces/RN/pages/915243053)
- https://mobile-security.gitbook.io/masvs/security-requirements/0x07-v2-data_storage_and_privacy_requirements
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#checking-for-sensitive-data-disclosed-through-the-user-interface-mstg-storage-7
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Testing-Data-Storage.md#checking-for-sensitive-data-disclosure-through-the-user-interface-mstg-storage-7