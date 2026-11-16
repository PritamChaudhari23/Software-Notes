### Contents:

1. Model View Controller
2. Layered architecture, and Clean vs Layered
3. Clean Architecture
4. How the three relate

---

## 1. Model View Controller

- MVC is a design pattern that separates an application into Model, View, and Controller.
- The Model manages data, business rules, and application logic.
- Models are typically defined using Mongoose, which maps MongoDB documents to JavaScript objects.
- The Model handles database operations like CRUD, schema validation, and business logic.
- MongoDB’s schema-less nature fits well with MVC, allowing flexible model evolution.
- Mongoose brings a schema back on the application side, so the flexibility is a choice, not the default.
- The same Model can be reused for multiple Views, such as web pages and API responses.
- The View is responsible only for presenting data to the user.
- Views are built using HTML and CSS, often with templating engines like EJS or Handlebars.
- Client-side JavaScript enhances the View with dynamic behavior and DOM manipulation.
- The Controller handles user input and coordinates between the Model and View.
- Controllers receive requests from the frontend, process data, and return responses or rendered views.
- In a Node.js application, Express handles routes and HTTP requests, and the Controller layer is the route handler (controller) functions you write on top of it.
- Middleware in Express integrates smoothly with MVC for authentication, logging, and validation.
- MVC helps keep routing logic separate from database queries, improving maintainability.
- Using MVC in Express makes APIs cleaner and more modular, especially for RESTful services.
- This separation improves code organization and readability.
- MVC makes applications easier to maintain and scale, making it easier to add new features or endpoints.
- Overall, MVC enables a clean code structure, faster development, and easier collaboration.

### MVC in practice:

- Request flow: Client => Route => Controller => Model => Database, then the Controller picks the View (rendered HTML) or sends JSON.
- In a REST API there is no HTML View. The JSON response is the View.
- Typical folders: `models/`, `views/`, `controllers/`, `routes/`.
- MVC has no separate service layer. Business logic ends up in the Model or the Controller. Layered architecture (section 2) adds that layer.

---

## 2. Layered architecture

- Separation of concerns.
- Horizontal layers each with clear responsibility.
- Request and response pass from one layer to next.
- Typical 3-layer architecture: Presentation layer => Business / Domain Layer => Data Layer. Layers are logical groups of code. Tiers are physical deployments (client, app server, database server). This is a 3-layer architecture.
- Request flow (top to bottom) => Client => Controller => Service => Repository => Database <= Response flow (bottom to top)

### LAYERS:

1. Presentation Layer (Controller / API)
2. Application / Service / Domain Layer (Business Logic)
3. Data Access / Persistence / Infrastructure Layer (Repository / DAO)
4. Database

### COMPONENTS

Controller:

- Handles HTTP request/response, input validation, routing.
- Serialization (Object => JSON) and Deserialization (JSON => Object) happens at the controller layer but it’s done by web framework (Express.js, Springboot etc.).
- Converted JSON is then sent to client.

Service:

- Contains business logic, orchestrates multiple repositories.

Repository:

- Contains DB queries, keeping db logic out of controllers or models.
- Fetches and persists data without exposing database details.
- Once we get data from DB, it is plugged in as per our model by repository and returned to service.
- Encapsulates all data access logic.

Model:

- Represents data or business concepts in a specific layer.
- Each layer has its own form of model. It represents same data but in different form at different layers.
- Presentation layer - DTO (Data Transfer Object)
- Domain layer (Entity / Business object)
- Data layer (Persistence model - ORM / ODM)

**Controllers handle requests, Services decide what to do, Repositories handle data, and Models carry information between them.**

### Layered architecture in a Node app:

```
src/
  routes/         (maps URLs to controllers)
  controllers/    (Presentation: req and res)
  services/       (Business logic)
  repositories/   (Data access: queries)
  models/         (Mongoose schemas)
  middlewares/
```

- A layer talks only to the layer directly below it.
- No database code in controllers. No `req` or `res` in services.
- Validation of the request shape belongs in the controller or a validation middleware. Business rules belong in the service.

---

### Clean architecture vs Layered architecture:

- Layer arch. has flow from top to bottom, clean arch. has flow from outward to inward.
- Inner layers know nothing about outer layers.
- Business logic is fully independent.
- Main difference is dependency inversion.
- Presentation => Application (Use Cases) => Domain (Entities & Rules) <= Infrastructure (DB, Frameworks)
- In layered architecture the business layer depends on the data layer, so business code ends up depending on the database. In Clean Architecture the data layer depends on the domain instead, so the database can be swapped without touching business rules.

Layers:

1. Presentation Layer (Controller / API)
2. Application Layer (Service / Use Cases)
3. Domain Layer (Entities, Business Logic)
4. Data Access / Persistence / Infrastructure Layer (Repository / DAO)
5. Database

---

## 4. How the three relate

|                         | MVC                               | Layered                                   | Clean                                                         |
| ----------------------- | --------------------------------- | ----------------------------------------- | ------------------------------------------------------------- |
| Splits the app into     | Model, View, Controller           | Controller, Service, Repository, Database | Entities, Use Cases, Interface Adapters, Frameworks & Drivers |
| Dependency direction    | Controller uses Model and View    | Top to bottom                             | Outside to inside                                             |
| Business logic lives in | Model (or Controller)             | Service layer                             | Entities and Use Cases                                        |
| Database knowledge      | In the Model                      | Service depends on the data layer         | Only in the outermost layer                                   |
| Best for                | Small apps, server-rendered pages | Most Node and Express APIs                | Large apps, long-lived, swappable infrastructure              |

---
