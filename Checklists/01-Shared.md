# Shared security requirements between platforms

## Default

| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| SD.1 | High | Login / Signup, keeping user session alive | All tokens / credentials must be stored in keychain/keystore if they are persisted | [Link](www.google.com) |
| SD.2 | High | Storing environment variables | Environment variables cannot be stored in github repository. All envs should be stored in secrets on CI (e. g. Bitrise) | [Link](www.google.com) |
| SD.3 | Medium | App is using logs. | No sensitive data is written to application logs. | [Link](www.google.com) |

## Extra

| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| SE.1 | Medium | Fintech app or very sensitive application | To increase security of the application it could be additionally protected with PIN screen. | [Link](www.google.com) |
