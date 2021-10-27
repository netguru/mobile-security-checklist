# Mobile Security Handbook Contribution guide
So you would like to be a part and improve mobile security checklist, great! We are waiting for your contribution! Here you will find all the information needed to begin your journey with Mobile Security Handbooks.

## 1. Choose your topic
- If you came here, because you saw that some requirement in our checklist had no proper implementation guide, then you already have your topic chosen and can continue to the next step.
- If you want to contribute, but have no idea what you could write about, then go to our [checklist](../Checklists/) and look for a requirement without a proper handbook linked in the reference column.
- There is also a chance that you have an idea for a requirement that is not yet added to our checklist, then you should also check the [contribution guide for checklist requirements](../Checklists/how_to_contribute.md).

## 2. Create an issue
To prevent multiple people working on the same topic, please create an issue for your chosen topic before starting your work (user handbook template and provide ID of selected requirement). This way we can avoid duplicates and others will be able to contact you with offers to co-contribute.

## 3. Write your Handbook
When you have a topic that picked your interest it's time to start your contribution.<br>
Begin with doing proper research:
- Each requirement has a point of origin — whether it's OWASP Guidelines, CWE issue or other security directive. Linking it provides a verified reason for the proposed solution to be implemented.
- We want to offer solutions with instructions for developers of all major platforms — Android, Flutter, iOS and React Native, but it's hard to be proficient in all of them. Provide a solution for at least one platform, and for the rest let's leave it to others to co-contribute to your handbook.
- Try to save links to articles used in your research, so you can provide them to developers hungry for more knowledge.

With these preparations done, you can copy our [Handbook template](handbook_template.md), that provides you with an easy to fill outline. If ever feel lost during writing, you can always check out other Handbooks to see examples of used language, formatting or reasoning.
<br>
Remember to place your Handbook file in the proper directory, depending on the chosen requirement category.

## 4. Create the Pull Request
After your Handbook is done, you can move to the last step before your contribution is done:
1. Put your handbook on a new branch named after the chosen requirement ID — `handbook/<requirement_id>`.
2. With your branch pushed to the remote you can create a new [Pull Request](https://github.com/netguru/mobile-security-checklist/compare?template=handbooks.md).
3. Remember to properly fill all required information in the PR template and ensure it has a `Handbook` label.
4. Submit your Pull Request and wait for a review from one of the maintainers.

## 5. Enjoy
If everything went through and you contribution was reviewed successfully you can now enjoy being a part of mobile security checklist contributors community ❤️