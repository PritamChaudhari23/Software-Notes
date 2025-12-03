REACT:

1. How to create a custom hook?

- How to create a reusable UI component, maybe from a UI library?
- How to create datatable component and reuse it for list api
- Interview question types - 1.Given code snippet - Find error, 2.Given code snippet - find output
- Common react situation; UI renders before API response in arrived.
- React project - colour constants and string constants for entire project
- Testing react application - Test on all browsers and mobile
- Passing data between components - lifting state up and prop drilling (add prop drilling in notes)
- Frequently asked javascript and react code interview questions - Type: Spot error, tell output - check with chatgpt

---

JAVASCRIPT:

- What are default parameters in a javascript function?
- Finding out which elements from one array belong to other array using some object property => Running loop over two arrays - No, Use filter and some

CLOSURE:

**Function nesting** is when a function is defined inside another function, and the inner function's scope is limited to the outer function unless returned or passed out.

A **closure** is a function that retains access to variables from its **lexical scope** , even after the outer function has finished executing.

---

https://www.freecodecamp.org/news/learn-typescript-beginners-guide/

Performance:
Use memoization
Debouncing
Lazy loading

Error handling:
Error boundaries
try/catch

Security:
HTTPs

---

const MyComponent = ({ name, ...props }) => { // rest in function signature in argument
return <div {...props}>{name}`</div>`; // Spread the received props onto the div
};

- using rest in the argument and spread inside the component
- used for generic components where any number of props are required
- prop types & default props

---

SHB:
1.Security
2.Authentication and authoraisation:
3.Form validation for lab requisition
4.What is an auth server?

1.An API call is made to EHR to fetch HL7 data of the patient.
2.The HL7 is parsed using a parser.
3.The patient details are populated on the form and rendered to the browser.
4.The user chooses the test and submits form.
5.The form data is collected in backend.

---

AWS, CLOUD:

- how to ssh into an ec2?
- how to use lambda fn using vs code?
  https://www.cloudskillsboost.google/paths/8
- For bash - https://guide.bash.academy/
- learn shell scripting. required for CICD, Cloud computing etc.
- Kubernetes used for scaling and load balancing containers
- Pub sub

---
