# Requirement
## [MSTG-NETWORK-4](https://mobile-security.gitbook.io/masvs/security-requirements/0x10-v5-network_communication_requirements)
The app either uses its own certificate store, or pins the endpoint certificate or public key, and subsequently does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA.

## Introduction

This handbook was created based on [the Certificate Pinning in iOS](https://www.netguru.com/blog/certificate-pinning-in-ios) and [3 Ways How To Implement Certificate Pinning on Android](https://www.netguru.com/blog/3-ways-how-to-implement-certificate-pinning-on-android) you can find much more detailed explanations there.

Our applications usually are using TLS protocol to communicate with the backend. TLS uses asymmetric cryptography to provide secure data transportation. Asymmetric cryptography uses two keys, a public key and a private key. The public key is used to encrypt data and the private key decrypts previously encrypted data. When you make a connection with a server you exchange public keys with it. You receive the public key to encrypt data before sending it. The server receives your public key so you can decrypt the data received from it with your private key. The keys are uniquely generated for each connection and are based on a shared secret negotiated at the beginning of the session, also known as a TLS handshake.

You can also check out this [video](https://www.youtube.com/watch?v=E5FEqGYLL0o) visualising asymmetric encryption.

## Risk
Imagine you are using a public Wi-Fi network on the train, conference or coffee shop. That network might be created by someone who wants to read the data sent by you. Since that person is providing your internet connection, they can create their own certificate and tell you to encrypt your data with it. Because this person created the certificate, they can read all the data inside it and then send it further to the right receiver. You may not see that you’re using the wrong certificate. This technique is called a man-in-the-middle attack. This illustration shows how it works.

![mitm-simulation](https://github.com/netguru/mobile-security-checklist/blob/handbook/SG.4/assets/mitm-simulation.png) 

## When you need it
Usually, the heavier your security implementation, the less flexible and harder to maintain it gets. You should always look for a solution that fits your app.

- If you really care about security and you can do it at the expense of flexibility, you should choose hardcoded certificate pinning. This solution should be used for example in banking applications — it is the safest of those presented here.

- If your certificates change very often and security isn't crucial in your project, you should probably use public key pinning. It will give you more flexibility and you will not block users with older versions of your application.

- If you want to support older versions of the app, but still implement certificate pinning, you can create a procedure to download the new certificate after expiration. It is not as safe as a hardcoded one, but it gives you more flexibility. After the certificate expires, you will download the new one. While you are downloading the new certificate, there is a chance that someone is listening to your communication.

- If your application does not need additional protection, e.g. it uses a public API to display the weather, you do not have to implement certificate pinning.

## Problem and desired effect
### Problem:
Communication with the backend may contain emails, passwords or sensitive data that for example could be used to log into email accounts.

### Desired effect:
The data encryption certificate sent from the backend has been checked if it is a valid Certificate. If the certificate is incorrect, the application will not communicate with this server

## Solution

Remember that you shouldn’t implement pinning by yourself, as implementation mistakes are extremely likely and usually lead to severe vulnerabilities.

### Warning

Usually if you would like to implement Certificate Pinning you will be pinning to domain fingerprint certificate (last in the chain of certificates). 

However there are two cases when it is not possible:
1. Using the Amazon domain (xxx.cloudfront.xxx), or other CDN.
2. Own domain Route53 and SSL Certificate from Amazon

In those cases you won’t be able to pin to the domain certificate, you should use Root certificate instead of it.

- [Official document about Certificate Pinning on AWS](https://aws.amazon.com/premiumsupport/knowledge-center/pin-application-acm-certificate/)

### iOS

- [The complete tutorial how to implement the Certificate Pinning using Alamofire or Firebase](https://www.netguru.com/codestories/certificate-pinning-in-ios)

- [Complete implementation of the Certificate Pinning using TrustKit](https://github.com/karolpiateknet/CertificatePinning/blob/master/CertificatePinning/Networking/TrustKit/TrustKitCertificatePinning.swift )

- [Unit Tests of TrustKit Certificate Pinning implementation for better understanding](https://github.com/karolpiateknet/CertificatePinning/blob/master/CertificatePinningTests/TrustKitCertificatePinningTests.swift )

### Android

[The complete tutorial how to implement the Certificate Pinning in Android](https://www.netguru.com/codestories/3-ways-how-to-implement-certificate-pinning-on-android)

## Testing guide
### Description
The app is using Certificate Pinning to validate the backend server.

### Example scenario:
Application performs different API calls.

### Tools needed:
- [Charles proxy](https://www.charlesproxy.com/)

### How to:
1. Install [Charles proxy](https://www.charlesproxy.com/)
2. Connect it to an application to receive communication in Charles. It can be used to simulate [Man in the middle attack](https://www.charlesproxy.com/documentation/proxying/ssl-proxying/).
3. If an application has working Certificate Pinning, it won’t allow connection to the server and you will receive an error message in the application.

## Additional resources
- https://www.netguru.com/blog/certificate-pinning-in-ios
- https://www.netguru.com/blog/3-ways-how-to-implement-certificate-pinning-on-android
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-3-and-mstg-network-4
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05g-Testing-Network-Communication.md#testing-custom-certificate-stores-and-certificate-pinning-mstg-network-4
