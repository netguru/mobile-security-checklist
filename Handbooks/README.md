# Mobile Security Handbook

## Why did we decide to create a Mobile Security Handbook?
In the security team when we talk about security, we want every project to be as secure as it should be or even more. This is our mission and it is heavily time consuming, that’s why we are creating tools that help us with monitoring and consulting security in all mobile projects. Monitoring is taken care of by the Security Checklist, it tells us how secure your project is and should be, it will also tell you which security features you need to implement in your project. We try to provide a link to some reference in the form of a blogpost or article, but they often describe a given security issue in detail without providing a quick way to fix it. That’s the consulting part of our work — answering questions, suggesting solutions and helping with implementations, and as mentioned above this is time consuming due to the fact that usually there’s a need to discuss more than one platform, which means engaging more than one person from the security team.

This is where the Security Handbook comes from. We want a source of easily accessible knowledge, a collection of solutions for your questions presented in a unified way for all the platforms. This way we can have one tool for both people looking for answers on confluence and as a reference link beside requirements in the Security Checklist.

## What is a Solution?
Solution is an article that focuses on a single security issue and answers all questions about it in an accessible way. Each article is identified with associated code of OWASP requirement and is using unified format to provide information about all related platforms. The content of the articles is divided into five parts that walks you step-by-step by the process of understanding and increasing the security of your project. Those steps are:

1. The Risk
This introductory part presents an explanation to what is the risk of a given security requirement not being implemented. This has two purposes, firstly it explains to the developer why he should take care of this issue, secondly it provides means for convincing clients to put security tasks into the sprint.

2. Security Qualification
When we are deciding security requirements for a project, we are looking at it from various perspectives:

 - To which area it belongs — is it an entertainment app, is it used for banking or maybe it is processing medical data?

 - What features it implements — does it offer login/signup, does it allow for files upload or it displays web content?

 - Who is the target — will the app be used during conferences, by kids in school or at the user’s home?

 There’s multiple factors deciding required security measures and one feature in a project can be targeted by multiple issues. This part of the solution is helping you to double-check which part of the project you create a need to implement this security solution.

3. Problem/Desired effect
This is similar to the format known from Jira AS IS/ TO BE, that presents you a security summary of what your project does by default (Problem) and how it should behave after implementing the solution (Desired Effect).

4. The Solution
The core part of the solution is the information how to implement it into your project. Depending on the presented problem you will find here an explanation of what you need to do to improve security of your project. It can be in a form of general and abstract instructions (eg. “extract logout function to be able to run it from anywhere”) or code snippets with general solution. Beside this we always try to include codestories that already touched this security topic and link to a repo that has this feature implemented, so you can check a live example. All of it split between all mobile platforms that we are using — iOS, Android and ReactNative (we hope to also include Flutter in the future).

5. Testing guide
Last part of the solution is a step-by-step instruction on how to “hack” your project. This can be used by both developers and QAs and it provides detailed instruction how to test if the security issue got properly mitigated. We try to list all tools needed for testing and point parts of the application that you should observe.

## How do you use the Mobile Security Handbook?
The best way to use Security Handbook is in tandem with Security Checklist. Going through the checklist you should already have tickets in Jira to improve security of your project and reference links to associated Handbook Solutions, otherwise check the content table below to find the proper article. After you use the risk introduction to convince the client about taking the ticket into the next sprint, you can skip the qualification part (checklist already tells you that you need to implement this), and move directly to implementing a given solution.

When you are done with implementation, you can drop a link to the Testing guide part into the ticket, to let your QA know what and how he needs to test it.

## Your feedback
Security Handbook is created for you, developers that need to improve security of their apps and QAs that will later test it, and to ensure the best experience we need your feedback. If you already had a chance to work with any of our Solutions please tell us what can be improved or added via issues or pull request.

## Want to contribute?
If you want to contribute and help us grow our mobile security knowledgebase, please check our [contribution guide](how_to_contribute.md).