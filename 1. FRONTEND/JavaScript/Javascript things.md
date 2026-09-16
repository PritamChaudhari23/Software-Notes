Instead of many if else: use

i.Ternary Operators
ii.Switch Statements
iii.Logical Operators (&& and ||)
iv.Lookup Maps

Lookup maps/lookup object: Eg:

```javascript
function checkBestStudent(subject) {
  var bestStudent = "";

  var lookup = {
    maths: "Adams Milner",
    english: "Akande Olalekan Toheeb",
    chemistry: "Chicago",
    physics: "Denver",
    biology: "Easy",
  };

  bestStudent = lookup[subject];
  console.log(bestStudent);
}

checkBestStudent("maths");
```

---

- Implement a loop counter to avoid getting stuck into infinite loop. On exceeding a count number, take an action to break and come out of loop.
- Store all the strings in a constants file and use constants wherever required.
- Finding out which elements from one array belong to other array using some object property => Running loop over two arrays - No, Use filter and some

---

Use spread operator to copy an object or to duplicate it and manipulate it.

var obj1 = {'key1':'val1', 'key2':'val2'}
var obj2 = {...obj1}
obj2 //{key1: 'val1', key2: 'val2'}

---

Javascript object keys could be in quotes or without quotes.
{
"PageSize": pageSize,
"PageCount": pageCount
}
OR
{
PageSize: pageSize,
PageCount: pageCount
}
if key and value both are same, then shorthand expression - use only one word for both.
{
pageSize: pageSize,
}
could be
{
pageSize
}

---

ARRAY INTERSECTION: let intersection = arr1.filter(x => arr2.includes(x));
ARRAY DIFFERENCE: let difference = arr1.filter(x => !arr2.includes(x));

---

- The this keyword is used to get/access or to set/modify/assign a value to the data member variable of a class, in that class itself.
- The scope of this keyword to be used on a data member is in that particular class.
- this keyword is used on the data member of a class and not on the member function.

Eg:
class Customer{
int customerID;

    void setCustomerID(int ID){
    	this.customerID = ID;
    }

}

---

JSON:
JSON.stringify(Javascript Object) - Convert a JS Object to string
JSON.parse(JSON String) - Convert a JSON String to JS Object
toString(), parseInt(), parseFloat()

---

HTML String:

HTML Document:

1. HTML DOM => HTML String
2. HTML String => HTML DOM
   const parser = new DOMParser();
   var HTMLDocumentDOM = parser.parseFromString(htmlString, "text/html");

To make base64 of an HTML file:
1.Get the string representation of that html file - using DOMParser (its used to create a DOM from any string)
2.Covert that string to base64 - using btoa()

---

BASE 64:

- Encoded format of PDF, image, HTML page etc in the form of long string of characters.
- Binary string: A representation of a file format (Eg: HTML, PDF, Image etc.) as a string of binary numbers.
- Any media type with any extension can be converted to base64 and vice versa.
- File <=> Binary string <=> Base64 <=> File

btoa() - Binary string to Base 64
atob() - Base 64 to Binary string

BLOB file type??

base64 to blob - new Blob()
base64 to file - new File()

---

Type check: ===
Null check: ?. - checks that something should not be null or undefined. used to fix error - cannot read property of undefined or use an empty array with OR condition (SomedatainArray || [])

- ...args - array of aruguments - rest operator - when it's not known beforehand how many props would be there. In react it's ...props - object of props when number of props is not known

---

URL string functions:

1. window.location.href - gives URL
2. window.location.pathname - path of URL
3. window.location.search - query string parameters

---

Basic:

1. Typescript vs Javascript
2. == vs === (equality and type checking)
3. Type coercion in javascript
4. Type casting - converting an object of one datatype into another

- parseInt(): string => integer
- parseFloat(): string => float,
- toString(): data => string
- JSON.parse(): String => JSON
- JSON.stringify(): JSON => string

5. generic type, any, T
6. null check in Javascript - ?.
7. typeof operator
8. delete operator
9. Scope: Global scope, function scope, block scope

---

Data structures, collections:

1. Javascript arrays

- Indexed collections
- Methods: push, pop, shift, unshift, filter, map, slice, splice
- Iterations: for, forEach, for...in, for...of loops

2. Javascript objects

- Property accessors
- Methods

3. Javascript Strings - Template literals (Template strings)
4. Javascript Collections: Maps, Sets
5. Date object
6. Math object

---

Advanced:

1. async/await function
2. Promises
   (Promise.all - https://nextjs.org/learn/dashboard-app/fetching-data)
3. setInterval, clearInterval, setTimeout, clearTimeout methods
4. Classes and javascript OOPs concepts
5. Import, Export & Modules in Javascript
6. anonymous functions and IIFEs
7. prototypal inheritance

---

ES6:

1. Block scope: let, const, var
2. Arrow functions
3. Object/Array destructuring
4. spread and rest operators
5. this keyword, super keyword

---

DOM:

1. HTML
2. CSS
3. jQuery, AJAX
4. Bootstrap
5. Document object
6. DOM Traversal

- document.querySelector
- document.querySelectorAll
- document.getElementById
- document.getElementByTagName

7. DOM Manipulation
8. DOM - Event handling

- addEventListner
- event.target.name
- event.target.value
- event.preventDefault
- event.stopPropogation

---

Testing & Debugging:

- print stack trace

---

Browser environment:

- localStorage and sessionStorage
- CORS
- event loop

---

JAVASCRIPT LIBRARIES:

- moments
- lodash

---
