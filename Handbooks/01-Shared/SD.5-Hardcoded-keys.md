# Requirement
## [CWE-798](https://cwe.mitre.org/data/definitions/798.html)
App doesn't store sensitive hardcoded keys inside app and conforms to best practices of storing hardcoded keys.

## Introduction

Mobile applications are often viewed as safe storage by some developers.

When you look at an application’s compiled code, it seems that it's not readable and no hard-coded values can be found. However, an experienced and motivated pentester will find it really easy to extract such keys and even automate the process of extracting hard-coded values. That's why you should never store or hard-code sensitive keys inside your app.

The problem of considering compiled mobile applications as safe storage is real. [This article claims](https://bevigil.com/blog/mobile-apps-exposing-aws-keys-affect-100m-users-data/) that 0.5% of mobile applications contain AWS API keys which has resulted in the exposure of 100M+ users. That number is for sure bigger than 0.5%, as in this article they only consider AWS API keys. There are much more sensitive keys that should not be stored directly in code and you can find a lot of articles describing such cases. There are also [CWE issues](https://cwe.mitre.org/data/definitions/798.html) describing the subject.

## Risk
TODO

## When you need it
When you need to use static keys in your application.

## Problem and desired effect
### Problem:
Storage of static keys.

### Desired effect:
Storing not harmful keys in not easy to extract form.

## Solution

TODO

### iOS

TODO

### Android

TODO

## Testing guide
### Description
TODO

### Example scenario:
TODO

### Tools needed:
TODO

### How to:
TODO

## Additional resources
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06j-Testing-Resiliency-Against-Reverse-Engineering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06c-Reverse-Engineering-and-Tampering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05c-Reverse-Engineering-and-Tampering.md 
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05j-Testing-Resiliency-Against-Reverse-Engineering.md 