# Requirement
## [CWE-798](https://cwe.mitre.org/data/definitions/798.html)
App doesn't store sensitive hardcoded keys inside app and conforms to best practices of storing hardcoded keys.

## Introduction

Mobile applications are often viewed as safe storage by some developers.

When you look at an application’s compiled code, it seems that it's not readable and no hard-coded values can be found. However, an experienced and motivated pentester will find it really easy to extract such keys and even automate the process of extracting hard-coded values. That's why you should never store or hard-code sensitive keys inside your app.

The problem of considering compiled mobile applications as safe storage is real. [This article claims](https://bevigil.com/blog/mobile-apps-exposing-aws-keys-affect-100m-users-data/) that 0.5% of mobile applications contain AWS API keys which has resulted in the exposure of 100M+ users. That number is for sure bigger than 0.5%, as in this article they only consider AWS API keys. There are much more sensitive keys that should not be stored directly in code and you can find a lot of articles describing such cases. There are also [CWE issues](https://cwe.mitre.org/data/definitions/798.html) describing the subject.

## Risk

Hard-coded, sensitive data in application binary can always leak and could be used to harm your business. API keys may provide access to third-party services like AWS storage, SMS gateway, payments API, or analytics. While analytics keys don't lead to much risk, leaking any of the other mentioned keys may lead to serious consequences.
Let’s see some examples.

1. **Keys providing read access for public data from a free API** 
   In such cases, there is no real risk, as API requests are free and the stored data is public. An attacker can also generate such a key for themselves, so there is no reason for them to use your key. 
   
2. **Keys providing read access to confidential data**
   One of the best examples here is the AWS API key. It may contain read access permissions, which allows an attacker to download the whole database stored there. As a result, you will leak confidential data and may get a fine for breaking GDPR or other data protection laws. 

3. **Keys providing access to SMS gateways**
   Let’s imagine a service in which an attacker could send an SMS using your hard-coded key and subscribe to a spam service that will make them money at your expense. It could result in losing large amounts of money in a short time from your account connected to the SMS gateway key.

4. **Keys providing access to payment services**
   Let’s consider an application that has a key that allows sending money to or from a Bitcoin wallet.An attacker could find this key and send all the money out of your account, or even use it as a chain for money laundering.

5. **Firebase cloud functions server key**
   From the official documentation: “Important: Do not include the server key anywhere in your client code. Also, make sure to use only server keys to authorize your app server. Android, iOS, and browser keys are rejected by FCM.”

   Using the Firebase cloud functions server key, an attacker could send notifications to every app user. Such notifications could contain malicious links and install malware applications, just as one example.

## When you need it
When you need to use static keys in your application.

## Problem and desired effect
### Problem:
Storage of static keys.

### Desired effect:
Storing not harmful keys in not easy to extract form.

## Solution

Do not store these keys in the code.

If you need to communicate with a sensitive, external API, ask the backend to create an endpoint to do that. This endpoint should be authenticated with a user token and implement proper security requirements. In this way, attackers should never get those API keys, and only you will be able to communicate with your backend.

## Testing guide
### Android 
For Android, you can check out [my tutorials](https://github.com/karolpiateknet/Android-Security-UnCrackable-Level-1), where I explain everything from reconnaissance of Android apps to an automated Frida script that finds hidden secrets in Uncrackable Level 1.

You can also check out other tutorials in [the OWASP repository](https://github.com/OWASP/owasp-mstg/tree/master/Crackmes).

### iOS
This section contains a tutorial on how to find a hard-coded secret key inside an iOS app.

#### Secret stored as variable

A common solution used by many developers is to store a secret key as a property.

`private let topSecretKey = "top_secret_key_value"`

It is the simplest solution to store a secret key in iOS, but it can be easily extracted using a proper tool, e.g. [Hopper Disassembler](https://www.hopperapp.com/).

Load your ipa project file to Hopper and select the Str button in the left menu, then search for the value of the provided secret.

<img width="341" alt="Hopper" src="https://user-images.githubusercontent.com/57398986/145383067-0089c620-6f37-4e6e-a2b6-604915b40aa3.png">

You can find that it can easily be found, especially when a stored secret has a specific pattern and you can search for strings containing that pattern.

#### Secret stored in array of Ints

A common solution for storing hard-coded strings is to encrypt and encode them to an array of Ints. In this way, we won’t see them in the str section in Hopper. However, we can execute code of the class that contains it to get its properties using a dynamic analysis tool like Frida.

For ObjC class, the Frida code would look like this:

```
var instance = ObjC.classes["ClassWithKeys"].alloc().init();
console.log("Class properties: " + instance["- _ivarDescription"]());
```

It would return us all class properties and methods parsed to String.

```
{
  "topSecretKey" = "top_secret_key_value";
}
```

Storing these secrets in encrypted form and using another class for decryption would make it a little bit harder to get the secrets, but in the end the app would still need a place where this secret is in the memory in decrypted form.

## Additional resources
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06c-Reverse-Engineering-and-Tampering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05c-Reverse-Engineering-and-Tampering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md 
