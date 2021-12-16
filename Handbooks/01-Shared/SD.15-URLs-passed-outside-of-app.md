# Requirement
## [CWE-601](https://cwe.mitre.org/data/definitions/601.html)
In case creating a URL object, it is suggested to check that host contains in allowed list of hosts.

## Risk
If an application gets URL strings from API, it has a risk during attack “man in the middle” that this link can be changed.
Attacker can substitute correct URL-strings to wrong one. In simplest case, the user will navigate to a fake page. A more significant threat can be brought by a case,  when using fake URL user download malware file to his phone.

## When you need it
- application gets URL from API to show internet page or download files
- application gets URL from iOS universal links, Android App Links

## Problem and desired effect
### Problem:
Application can open malicious URLs.

### Desired effect:
Application can open only trusted URLs included in allowed URLs list.

## Solution
We can create an extension to URL class with new initialiser that will validate the URL from API.
URL initialiser should check if:
- scheme is corresponded to app URL scheme
- the host is included in the list of allowed hosts
- host passes check with regular expression (for URLs that use subdomains)
- host has proper characters

### Swift:
```swift
let urlString = "https://www.google.com"
let url = URL.init(secureUrlString: urlString)
```

## Testing guide
### Description
Application should open only valid URLs and ignore URL that not contain in allowed list.

### Example scenario:
- In case URL host contains in allowed host list, proceed with this URL (open URL).
- In case URL host not contains in allowed host list, do nothing.

### Tools needed:
- [Proxy tool]: Charles or OWASP ZAP or any other proxy with possibility to modify request/response

### How to:
- Make request, catch response that contain URLs.
- Modify response with malicious URLs.
- Open “Received URL” (malicious URLs can’t be open if host not contains in allowed list).

## Additional resources
- Source code of URL extension: https://github.com/howtodance/SecureURL/blob/main/Shared/URL%2BSecure.swift
- Example of application with secure URL: https://github.com/howtodance/SecureURL

| Step 1 | Step 2 | Step 3 |
| --  | -- | -- |
| ![Step 1](/assets/SD15-1-example.png) | ![Step 2](/assets/SD15-2-example.png) | ![Step 3](/assets/SD15-3-example.png) |
