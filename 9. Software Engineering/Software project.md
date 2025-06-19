SOFTWARE DEVELOPMENT:

PRODUCT DESIGN, PRODUCT DEVELOPMENT

SDLC - Software Development Lifecycle
STLC - Software Testing Lifecycle

ENVIRONMENTS:

1. Development
2. UAT, Test environment
3. Production

Environments: Usually for API based projects
Sandbox - Dev (Development and testing on dev)
Production - Test (For production testing)
Production - Live

Migration activity - Migrating backend or cloud platform

---

SOFTWARE PROJECT:

- Kickoff meeting: Initial
- Release management and Business approval
- Project documentation. MD file or story book. Developer guide. For new devs joining the team. Giving KTs
- Project wikis: Knowledge article for others reference
- Query logs: for any questions to be answered by client
- Project management board - Azure Devops, JIRA
- Project culture - The way we do things around here to succeed. Represents the shared norms, beliefs, values, and assumptions of the project team. How are the team members, how is the manager. Who is good who is bad? Who is helpful, who is reliable? who has attitude? how is coordination between dev and QA? Such things
- Set a process, follow a process. Process: Sequence of actions. What to do, what steps to follow when something happens.
- Audit
- Escalations
- Change requests (CRs)

Practices:

- POC - small demo to gain customer confidence. POC is prepared before starting a project and shown to customer.
- Daylight saving meeting time adjustments
- Holiday deployment and code freeze
- No pushing to prod on Friday
- Code freeze

---

MERGE & DEPLOYMENT

After PR is merged => Jenkins automated pipeline triggered => new build created and deployed on dev instance

- Production deployments are done by DevOps member.
- DevOps person co-ordinates with the developer of the feature to push the code changes from dev branch to production branch.

---

Steps:

1. Take pull of the repo in a folder and switch to dev branch.
2. Take pull of same repo in another folder and switch to UAT branch.
3. Open the two folders in WinMerge tool to compare them.
4. Confirm with the developer about the code changes made in dev branch and the push the code changes in UAT branch.
5. Raise a merge request to merge UAT branch into prod branch.
6. Once approved UAT is merged into prod branch. UAT and prod branches are always in sync.

---

WinMerge:

- Used to compare the same folder/ repo but two different branches.
- Left panel contains code from dev branch.
- Right panel contains code from UAT branch.
- Compare a particular file. If the code changes made by the developer are regarding the ticket being deployed, shift the snippet from left to right.
- Sometimes both files are made completely identical i.e. whole file is shifted from left to right.
- Sometimes small snippets are shifted. Sometimes new files are added.
- Then commit and push on the UAT branch. And raise merge request.

---

1. Deploy on NitorAWS - code pushed on develop branch
2. Deploy on UAT - code pushed on UAT branch
3. Deploy on production - code pushed on prod branch

Dev => Unit testing => Merge, build and deploy on Dev server => QA on dev server by dev => Merge, build and deploy on UAT server => QA on production => Merge, build and deploy on production server => QA on production => UAT on production => QC on production => Assign to CS team to verify with the client

Dev => QA => QC => CS Team => Client

---
