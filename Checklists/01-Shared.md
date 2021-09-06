# Shared security requirements between platforms

## Default

| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| SD.1 | High | Login / Signup, keeping user session alive | All tokens / credentials must be stored in keychain/keystore if they are persisted | [Link](www.google.com) |
| SD.2 | High | Storing environment variables | Environment variables cannot be stored in github repository. All envs should be stored in secrets on CI (e. g. Bitrise) | [Link](www.google.com) |
| SD.3 | Medium | App is using logs. | No sensitive data is written to application logs. | [Link](www.google.com) |
| SD.4 | Critical | Sensitive aplication logic | "Validate every update of a sensitive value with the server. <br> Do not validate sensitive features locally <br> For example: <br> - Admin mode <br> - Coins for premium features" | [Link](www.google.com) |
| SD.5 | Critical | Hardcoded keys | App doesn't store sensitive hardcoded keys inside app and conforms to best practices of storing hardcoded keys. | [Link](www.google.com) |
| SD.6 | Critical | Login / signup | Do not store user password in local data storage. | [Link](www.google.com) |
| SD.7 | High | Third party service with API keys. | Keys generated in Third Party service like Google Cloud should have minimum set of permissions. <br> It should have assigned bundleID / AppID to key, It will accept data only from those apps. | [Link](www.google.com) |

## Extra

| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| SE.1 | Medium | Fintech app or very sensitive application | To increase security of the application it could be additionally protected with PIN screen. | [Link](www.google.com) |
