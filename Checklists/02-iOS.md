# iOS specific requirements
| ID  | Priority | Feature | Description | Link |
| --  | -- | ---------------------- | ---------------------- | - |
| iOS.1 | Medium | Using NSURLSession | By default NSURLSession stores data, such as HTTP requests and responses in the Cache.db database. <br> It should be disabled in URLSession with setting .ephemeral type instead of default one | [Handbook](../Handbooks/02-iOS/iOS-Disable-caching-in-URLSession.md) |
| iOS.2 | Medium | Certificate Pinning implemetation using TrustKit | Set kTSKDisableDefaultReportUri to true <br> By default this flag is false, which means it will be sending error reports to tool owner | [Handbook](../Handbooks/TODO.md) |
| iOS.3 | High | Default | Verify if not needed files are not included in the bundle. <br> Exclude them if needed using EXCLUDED_SOURCE_FILE_NAMES | [Handbook](../Handbooks/TODO.md) |
| iOS.4 | Low | User enter sensitive data or password into inputs | Verify that the app prevents usage of custom third-party keyboards whenever sensitive data is entered | [Handbook](../Handbooks/02-iOS/iOS-Force-system-keyboard.md) |
| iOS.5 | Low | Using external libraries | External libraries should be linked staticly | [Handbook](../Handbooks/02-iOS/iOS-External-libraries-linking.md) |

