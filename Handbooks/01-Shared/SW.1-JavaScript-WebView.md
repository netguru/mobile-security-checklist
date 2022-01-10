# Requirement
## [MSTG-PLATFORM-5](https://mobile-security.gitbook.io/masvs/security-requirements/0x11-v6-interaction_with_the_environment)
JavaScript is disabled in WebViews unless explicitly required.

## Risk
Using WebViews exposes application for displaying malicious web content and/or allow the attacker to access the user's files.

## When you need it
When app is using WebView.

## Problem and desired effect
### Problem:
WebViews support JavaScript execution so script injection and Cross-Site Scripting attacks can affect them.

### Desired effect:
Disable JavaScript in WebViews unless explicitly required.

## Solution

### iOS
`UIWebView` → Deprecated starting on iOS 12 and should not be used. Make sure that either `WKWebView` or `SFSafariViewController` are used to embed web content.

`WKWebView` → Disable JavaScript using `WKPreferences` & `WKWebViewConfiguration` or use `SFSafariViewController`.

```
let preferences = WKPreferences()
preferences.javaScriptEnabled = false
preferences.javaScriptCanOpenWindowsAutomatically = false
        
let configuration = WKWebViewConfiguration()
configuration.preferences = preferences
        
let webView = WKWebView(frame: view.bounds, configuration: configuration)
```

`SFSafariViewController` → Safari application with separate `Sandbox` so there is no interaction between App <-> WebView. You don't have to worry about JavaScript which anyway cannot be disabled by developer.

### Android

JavaScript is disabled by default for WebViews.

## Testing guide
### Description
WebViews should be used with disabled JavaScript.

### Example scenario:
- App opens WebView.
- No JavaScript code is executed.

### Tools needed:
- Xcode for iOS
- Android Studio for android

### How to:

#### iOS
- Search for `UIWebView` / `WKWebView` in Xcode by Find navigator.
- Verify that there is no `UIWebView` and JavaScript is properly disabled for usages of `WKPreferences` and ensure that the `javaScriptEnabled` property is set to `false`.

#### Android
Look for the method `setJavaScriptEnabled` to check for JavaScript activation.

`webview.getSettings().setJavaScriptEnabled(true);`

## Additional resources
- https://mobile-security.gitbook.io/masvs/security-requirements/0x11-v6-interaction_with_the_environment
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06h-Testing-Platform-Interaction.md#testing-ios-webviews-mstg-platform-5
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05h-Testing-Platform-Interaction.md#testing-javascript-execution-in-webviews-mstg-platform-5 
