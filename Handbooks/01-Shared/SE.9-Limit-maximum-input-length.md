# Requirement
## [CWE-20: Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html)
## [CWE-1287: Improper Validation of Specified Type of Input](https://cwe.mitre.org/data/definitions/1287.html)
The app should limit maximum input length.

## Risk
Some of the common attack patterns are based on incorrectly configured input types in your application. One of them is SQL Injection which is often an example of motivation to check your inputs. Depending on type and how bad the protection is it can even lead to destroying the whole database or altering system behavior by injecting malicious code.

## When you need it
When your app contains inputs that should have limited characters count, for example name, password, notes etc. Pretty much all the time you need to keep focus on proper configuration of your input fields as currently most apps are using some sort of input.

## Problem and desired effect
### Problem:
Long input can be entered in insecure input fields allowing, for example, Injection attacks.

### Desired effect:
All input fields should be configured properly and have at least basic max length validation.

## Solution
Review all input fields to make sure that their maximum length is correct for specific use cases. For example there’s no need to have more than 100 characters for a name or address input. Consider consulting with the backend as most of the time they should have some default characters limit like 255 or other for different cases. Try to follow their requirements and your experience when it comes to inputs that are sent to the backend.

If backend is missing such protection then strongly suggest that it should be added.

### Android
Add default max length to integers
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <integer name="maxLength">255</integer>
    <integer name="maxNameLength">50</integer>
</resources>
```
preferably set it in your app theme which is used in Manifest.xml to limit all inputs
```xml
<style name="Theme" parent="Theme.MaterialComponents.DayNight">
    <!-- Primary colors and other customization -->
    <item name="android:maxLength">@integer/maxLength</item>
</style>
```
and if needed override it in specific style or simply by widget attribute, like:
```xml
<!-- Style declaration -->
<style name="NameInputStyle">
    <item name="android:maxLength">@integer/maxNameLength</item>
</style>
<!-- Style usage -->
<EditText
    android:id="@+id/nameEt"
    style="@style/NameInputStyle"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textPersonName|textCapWords" />
<!-- Simple attribute usage -->
<EditText
    android:id="@+id/nameEt"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:inputType="textPersonName|textCapWords"
    android:maxLength="@integer/maxNameLength" />
```

### iOS
One of the solutions is to subclass `UITextField` by adding a trim logic with some default max length which can be changed based on specific use case, an example:
```swift
/// `UITextField` with added `Maximum Input Length` property that constraints input length.
class LengthLimitedTextField: UITextField {

    /// Value indicating maximum length of the input. Minimum value is 1.
    @IBInspectable var maximumInputLength: Int = 255 {
        didSet { maximumInputLength = max(maximumInputLength, 1) }
    }

    // - SeeAlso: UITextField.init(frame:)
    override init(frame: CGRect) {
        super.init(frame: frame)
        addTarget(self, action: #selector(trimInputToLimit), for: .editingChanged)
    }

    // - SeeAlso: UITextField.init(coder:)
    required init?(coder: NSCoder) {
        super.init(coder: coder)
        addTarget(self, action: #selector(trimInputToLimit), for: .editingChanged)
    }

    @objc private func trimInputToLimit() {
        guard let text = self.text, text.count > maximumInputLength else { return }
        self.text = String(text.prefix(maximumInputLength))
    }
}
```
Of course it’s possible to override the maximumInputLength when needed for shorter input, like:
```swift
let textField = LengthLimitedTextField()
textField.maximumInputLength = 30
```
This subclass can also be used in Interface Builder with custom length limit.

Below example is for SwiftUI, custom TextField:
```swift
import Combine
import SwiftUI

/// Wrapper for `TextField` with added `Maximum Input Length` property that constraints input length.
struct LimitedTextField: View {

    /// Value indicating maximum length of the input. Minimum length is restricted to 1.
    var maximumInputLength: Int = 255

    /// `Binding` for the text to display and edit.
    @Binding var textBinding: String

    // - SeeAlso: View.body
    var body: some View {
        TextField(String(), text: $textBinding)
            .onReceive(Just(textBinding).filter { !$0.isEmpty }) { input in
                let lengthLimit = max(maximumInputLength, 1)
                guard input.count > lengthLimit else { return }
                textBinding = String(input.prefix(lengthLimit))
            }
    }
}
```
with usage as follows:
```swift
LimitedTextField(maximumInputLength: 30, textBinding: $text)
```

### React Native
Just add below line in the `<TextInput>` as follows:
```javascript
<TextInput
//...
maxLength={255} />
```

## Testing guide
### Description
App will block input when the threshold is reached.

### Example scenario:
Specify the correct max input length type based on use case and notice that you are not allowed to enter more than that.

### Tools needed:
Platform based device with installed app.

### How to:
- Run the app.
- Enter some long text in the configured input field — it should not allow you to input more than specified.

## Additional resources
- [TextInput · React Native](https://reactnative.dev/docs/textinput)
- [CWE - CWE-20: Improper Input Validation (4.6)](https://cwe.mitre.org/data/definitions/20.html)
- [CWE - CWE-1287: Improper Validation of Specified Type of Input (4.6)](https://cwe.mitre.org/data/definitions/1287.html)
- https://owasp.org/www-pdf-archive/OWASP_Application_Security_Verification_Standard_4.0-en.pdf
