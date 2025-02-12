BACKEND THINGS:

- API Design
- Schema validation
- DB and schema design
- Security
- Performance
- Deployment

---

NODE:

- Asynchronous
- Event driven
- Non blocking io
- Single threaded - It executes the code line by line - sequentially - for async operations it uses event loop
- Javascript engine - v8
- Nodemon
- NVM – Node version manager – used to work with multiple node js versions
- Monorepo in MERN

---

Javascript engine:

- Call stack
- Event loop
- Heap
  .....

Javascript execution:
Parsing -> AST -> .....

Event loop:

- Call stack
- Event/Callback queue
- Microtask/job queue

---

NPM & YARN:
1]uninstall:

- npm uninstall foo
- yarn remove foo

2]installing specific version:

- npm install <package-name>@<version>
- yarn add <package-name>@<version>

npm install lodash@^4.0.0
yarn add lodash@^4.0.0

^ is used to install version range - install minor updates and ~ for patches

3]dev dependencies:
--save-dev

---

Debugging node applications in VS Code: Set breakpoints
1]Without launch.json: VS Code toolbar -> Run -> Start debugging
2]With launch.json: VS code - Side panel -> Run and debug -> create launch.json file

---

- What are different HTTPS status codes????
- What is blocking vs non-blocking code?

---

MODULE SYSTEM:
1.Common JS:
const fs = require('fs')

const someFunction = () => {}

module.exports = someFunction;

#Name exports in common js:
named imports:
const myModule = require('./module'); // Importing the entire module

named exports:
module.exports = {
function1: someFunction1(),
function2: someFunction2(),
}

---

2.Module JS:
import fs from "node:fs"

const someFunction = () => {}

export default someFunction;

#Name exports in module js:
named imports: import {..., ....} from "..."
named exports: export default {...., .....} <-- Used when multiple functions are defined in single file.

- Use a type: 'commonjs' or type: 'module' in package.json. commonjs type is default

---

EXPRESS:
next(), middleware - app.use(), templating engine, static rendering?

Request methods:

- req.body
- req.params
- req.query
- req.method
- req.url
- req.session - used to manage session

Response methods:

- res.send() - send string in response
- res.json() - send json in response
- res.status()
- res.redirect()
- res.render()
- res.set()
- res.cookie()

---
