# iOS specific requirements
| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| iOS.1 | Low | Using UITextField with sensitive data | Set autocorrectionType to .none in Sensitive UITextFields. | [Handbook](../Handbooks/TODO.md) |
| iOS.2 | Medium | Using NSURLSession | By default NSURLSession stores data, such as HTTP requests and responses in the Cache.db database. <br> It should be disabled in URLSession with setting .ephemeral type instead of default one. | [Handbook](../Handbooks/TODO.md) |
| iOS.3 | Medium | Certificate Pinning implemetation using TrustKit | Set kTSKDisableDefaultReportUri to true <br> By default this flag is false, which means it will be sending error reports to tool owner. | [Handbook](../Handbooks/TODO.md) |
| iOS.4 | High | Default | Verify if not needed files are not included in the bundle. <br> Exclude them if needed using EXCLUDED_SOURCE_FILE_NAMES | [Handbook](../Handbooks/TODO.md) |

