# Requirement
## [M2: Insecure data storage](https://owasp.org/www-project-mobile-top-10/2014-risks/m2-insecure-data-storage)
Store data securely or not at all.

## Risk
By default URLSession stores data, such as HTTP requests and responses in the Cache.db database.

It is recommended to disable Caching requests in Cache.db file, as it may contain sensitive information in the request or response. This database file can contain unencrypted sensitive data, if tokens, usernames or any other sensitive information has been cached. 

## When you need it
When you use NSURLSession for communication with backend.

## Problem and desired effect
### Problem:
All requests and responses are being saved unencrypted to Cache.db file by default.

### Desired effect:
Requests and responses are not being stored in unencrypted Cache.db file.

## Solution
1. It is recommended to remove Cached responses after logout. This can be done with the provided method by Apple called `removeAllCachedResponses` You can call this method as follows:

   `URLCache.shared.removeAllCachedResponses()`

   This method will remove all cached requests and responses from Cache.db file.

2. If you don't need to use the advantage of cookies it would be recommended to just use the [.ephemeral](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral) configuration property of URLSession, which will disable saving cookies and Caches.

   [Apple documentation](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/1410529-ephemeral):

   `
   An ephemeral session configuration object is similar to a default session configuration (see default), except that the corresponding session object doesn’t store caches, credential stores, or any session-related data to disk. Instead, session-related data is stored in RAM. The only time an ephemeral session writes data to disk is when you tell it to write the contents of a URL to a file.
   `

3. Cache can be also disabled by setting the Cache Policy to [.notAllowed](https://developer.apple.com/documentation/foundation/urlcache/storagepolicy/notallowed). It will disable storing Cache in any fashion, either in memory or on disk.

## Testing guide
### Description
Application should not store unencrypted sensitive data.

### Example scenario:
Application performs different API calls.

### Tools needed:
- Jailbroken iPhone
- Objection

### How to:
To find the cached information open the data directory of the app (`/var/mobile/Containers/Data/Application/<UUID>`) and go to `/Library/Caches/<Bundle Identifier>`. The WebKit cache is also being stored in the Cache.db file. 

Objection can open and interact with the database with the command `sqlite connect Cache.db`, as it is a normal SQLite database.

## Additional resources
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x06d-Testing-Data-Storage.md#searching-for-cache-databases
- https://cwe.mitre.org/data/definitions/312.html 
- https://cwe.mitre.org/data/definitions/922.html
