# Requirement
## [MSTG-PLATFORM-11](https://mobile-security.gitbook.io/masvs/security-requirements/0x11-v6-interaction_with_the_environment)
Verify that the app prevents usage of custom third-party keyboards whenever sensitive data is entered.

## Risk
Third-party keyboards often contain some way of learning to improve predictions and autocorrects. This behaviour is achieved by monitoring all input user is providing with use of such keyboard. Data stored in learning databases could be leaked, leading to compromise of sensitive data such as password or security pins.

## When you need it
If your application takes input of sensitive data from user, such as:
- password, 
- credit card security code,
- security PIN.

## Problem and desired effect
### Problem:
User’s sensitive data is logged by third party software.

### Desired effect:
User’s sensitive data is kept enclosed within application’s sandbox.

## Solution
To ensure usage of system keyboard for sensitive inputs in our applications we need to setup our Text Fields to use secure entry:

### Swift:
```swift
passwordTextField.secureTextEntry = true
```

### React Native:
```javascript
<TextInput secureTextEntry = {true} />
```

## Testing guide
### Description
The application forces system keyboard for sensitive inputs.

### Example scenario:
- Application requires user to provide his password.
- When focused on password input only system keyboard is allowed.

### Tools needed:
- iPhone with third-party keyboard installed.

### How to:
- Open application on device with third-party keyboard set as default.
- Navigate to text input that should be secure.
- System keyboard should be presented without any hints for autocompletion/-correction (only iOS keychain prompt is allowed).

## Additional resources
- https://developer.apple.com/documentation/uikit/uitextinputtraits/1624427-securetextentry
- https://mobile-security.gitbook.io/mobile-security-testing-guide/ios-testing-guide/0x06d-testing-data-storage#finding-sensitive-data-in-the-keyboard-cache-mstg-storage-5