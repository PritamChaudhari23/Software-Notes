# Node.js & Express Notes

Contents:

1. Node
2. Express
3. Web server
4. Nodemon, NVM and PM2
5. Package manager: NPM & YARN
6. Debugging node applications in VS Code
7. File upload to AWS S3
8. Framework and Library
9. Notes: personal projects and backend knowledge
10. Node JS topics
11. Libraries

---

- Javascript **runtime environment** which runs on **Google** **chrome's V8 javascript engine**.
- Executes **outside** the browser.
- **Single threaded**: It executes one main thread sequentially so the code runs line by line.
- **Event loop:** Async tasks are handled by the **event loop** , so the main thread never blocks.
- Has **Non blocking I/O**: Uses **libuv** library to perform I/O operations.
- **Worker threads:** For CPU-heavy tasks, Node.js supports **worker threads** to run JavaScript in **parallel** from a thread pool.
- **Event driven**: Supports **asynchronous code** execution - Uses promises, callbacks and async/await.
- Has **built in modules** for various functionalities - like file handling, encryption, data fetching etc.
- Modules are written in JavaScript & C++ language
- Cross platform, Rich ecosystem, Scalable, real time applications
- Free, open-source
- Current version: v24.x (Dec 2025)

---

EXPRESS:

- Fast, lightweight, minimalist framework
- Buidiling **web applications** and **APIs** with Node js
- Supports **middlewares** to intercept and process requests and responses
- express.json() for JSON and express.static() for serving static files
- Supports **routing**
- Supports templating engines
- RESTful API Development
- Static file serving
- Unopinionated - so we don't have to follow a fixed project structure
- Current version: v5.x (Dec 2025)

---

Nodemon:

---

NVM – Node version manager

- Used to work with multiple node js versions in the system. Useful for testing, debugging, checking new features.
- Download and install exe.
- nvm --version: Check nvm version
- nvm list: List all node js versions
- nvm install 18.20.2 OR nvm install 22.23.1 OR nvm install 24.18.0 : Install specific versions
- nvm use 18.20.2 OR nvm use 22.23.1 OR nvm use 24.18.0 : Use specific version among installed
- nvm install lts: Install latest LTS node
- nvm install latest: Install latest node

Switch versions for projects:

cd my-old-project
nvm use 18.20.2

cd ../my-new-project
nvm use 24.18.0

---

PM2 in node js - Process manager for node applications

---

PACKAGE MANAGER: NPM & YARN

1. Install: npm install `<package-name>`@`<version>`, yarn add `<package-name>`@`<version>`. npm install lodash@^4.0.0, yarn add lodash@^4.0.0 => ^ is used to install version range, - install minor updates and ~ for patches
2. Uninstall: npm uninstall foo, yarn remove foo
3. dev dependencies: --save-dev

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

WEB SERVER:

- Computer software installed on server hardware that serves HTTP requests.
- Apache HTTP server: Node
- Apache Tomcat: Java
- IIS (Internet Information Services): Microsoft .NET
- nginx
- WAMP server: PHP
- Web server: A software that handles http requests and sends response. Eg: Apache HTTP Server, Nginx, Microsoft IIS, Express (Node.js)

---

## 6. Debugging node applications in VS Code: Set breakpoints

1. Without launch.json: VS Code toolbar => Run => Start debugging
2. With launch.json: VS code - Side panel => Run and debug => create launch.json file
3. `node --inspect app.js`, then open `chrome://inspect` to debug in Chrome DevTools. `--inspect-brk` pauses on the first line.

---

## 7. File upload to AWS S3

- Upload through your server: multer (memory storage) plus the AWS SDK v3 (@aws-sdk/client-s3, PutObjectCommand), or multer-s3.
- Better for large files: your server generates a presigned URL and the client uploads directly to S3.

---

## 8. Framework and Library

FRAMEWORK:

- A framework is a set of pre-written code that provides a structure for developing software applications.
- It is a layer between application and OS. More precisely, a framework sits between your application code and the language runtime or platform (Express on Node.js, Spring Boot on the JVM), not directly on the OS.
- A framework is usually built for one language. Express is for JavaScript, Django for Python, Spring Boot for Java. A platform like .NET supports several languages (C#, F#, VB).
- A framework does not convert code into OS or system understandable instructions. That job belongs to the compiler, interpreter or runtime (V8 for Node.js, the JVM for Java). The framework is pre-written code that runs on top of it.
- It speeds up the development process because programmers don't have to write code from scratch.
- It makes applications compatible due to standardisation.
- It's like a frame or a template for application development.
- Popular frameworks for different technologies:
  1. Java: Spring Boot
  2. C#: Microsoft .NET
  3. Node JS: Express, NestJS, Fastify, Koa
  4. Python: Django, Flask
  5. PHP: Laravel, Yii
  6. Ruby: Ruby on Rails
  7. Angular framework
  8. React: Javascript library, Next JS: Framework for React

LIBRARY: Collection of pre-written code that can be used to perform specific tasks.
Framework vs library: you call a library, but a framework calls your code (inversion of control).

Package/Dependencies managers for libraries in different technologies:

1. Java: Maven, Gradle
2. MS .NET: NuGet
3. Node JS: NPM, Yarn, pnpm
4. Python: PIP
5. Dart, Flutter: Pub

---

## 9. Notes: personal projects and backend knowledge

NOTES: Software notes - Backend, Database

What can I do?

1. Create REST API
2. Write CRUD queries
3. Implement layered architecture
4. File upload to AWS S3

Personal projects:

1. Invoice manager
2. medconnect
3. Products typescript
4. Students report - MVC
5. node concurrent
6. mongo query
7. node learning
8. my notes

---

## 10. Node JS topics

1. Introduction and basic javascript
2. Node JS basic concepts and installation
3. Node JS module system
4. File system and command line arguments
5. Asynchronous Node JS, Promises, async await in Node JS
6. Web servers: Express JS
7. Accessing an API from browser
8. Routing in node applications
9. REST APIs
10. Working with dynamic content & adding templating engines
11. The Model View Controller (MVC)
12. SQL introduction
13. Understanding sequalize
14. Working with NoSQL & using Mongo DB
15. Working with Mongoose
16. Authentication and security in node applications
17. Understanding validation
18. Error handling
19. Sorting, Pagination and Filtering
20. File upload & download
21. Sending emails
22. Realtime web applications, websockets & socket.io
23. Payments in node applications
24. Sessions & cookies
25. Working with GraphQL
26. Node JS as a build tool & using npm
27. Modern Javascript & node JS
28. Node JS & typescript
29. Introduction to Deno
30. Deno, CRUD & Databases (MongoDB)
31. Debugging node applications
32. Testing node applications
33. Deploying node applications

---

## 11. Libraries

1. express
2. express-validator
3. express-session
4. express-handlebars
5. ejs
6. pug
7. bcrypt
8. jsonwebtoken
9. nodemon
10. multer
11. mongodb
12. mongoose
13. connect-mongodb-session
14. mysql2
15. sequalize
16. nodemailer
17. nodemailer-sendgrid-transport (Deprecated), now @sendgrid/mail
18. socket.io
19. socket.io-client
20. body-parser (rarely used now), now express.json() and express.urlencoded() are built into Express (4.16 and later).
21. csurf (Deprecated). Use another CSRF protection (for example csrf-csrf) or SameSite cookies.
22. connect-flash
23. pdfkit
24. stripe
25. helmet
26. compression
27. morgan
28. graphql
29. express-graphql (Deprecated). Alternatives: graphql-http, graphql-yoga, Apollo Server.
30. mocha (testing)
31. chai (testing)
32. sinon (testing)
33. typescript
34. @types/node
35. @types/express
36. @types/body-parser
37. chalk
38. validator
39. request (Deprecated). Use the built-in fetch (Node 18 and later) or axios.
40. dotenv (env variables; Node 20.6 and later also has --env-file)
41. cors
42. cookie-parser
43. joi or zod (validation)
44. jest and supertest (testing, API tests)
45. winston or pino (logging)
46. @aws-sdk/client-s3 (S3)

---
