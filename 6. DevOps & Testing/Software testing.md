SOFTWARE TESTING:

- UAT - client does it

Project Testing:

1. Alpha testing
2. Beta testing
3. Sanity testing
4. Regression testing
5. Unit testing
6. Smoke testing
7. Adhoc testing
8. Penetration testing

Unit testing - done by developers before commiting and creating a merge request
Testing happens in both Dev and production environments.
Once deployed on dev - then test.
Then deployed on prod - then test.

QA - Quality Assurance - Done during software development life cycle
QC - Quality Control - Done during software testing life cycle, after production release.
QC done by Client side software tester.

Intermittent issues - Issues unable to reproduce on dev and QA end.

- Try to force the error, try o simulate it if there are no steps to reproduce it. And then fix the code or handle such errors and situations in the code.

---

Regression testing: Done to check if fix does not break existing
Sanity testing:
Unit Testing - Test a feature before releasing to QA. Fixing a bug or developin a feature should not break something else.

RTM:Requirements Traceability Matrix - Used for testing

QA shares the test plan while development is in progress

- FVT test cases
- Test suite

---

- Try out, install new softwares
- Explore its features
- Test it, find its limitations and bugs

---

Exploring apps similar to what we are building.
Testing and exploring the features of our competitor apps.

---

QA sequence => Test Sandbox(dev) => Test Production Validation
QC => Test Production Live => QA should not place orders on live
