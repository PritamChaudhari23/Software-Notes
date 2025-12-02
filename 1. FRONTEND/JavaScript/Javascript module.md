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

- Concept of default and named import/export
- Named alias for default and named import/export

// Default export
export default function add(a, b) {
return a + b;
}

// Named exports
export function subtract(a, b) {
return a - b;
}

export function multiply(a, b) {
return a \* b;
}

// Import default export with alias
import sum from './mathUtils'; // 'sum' is an alias for the default 'add' function

// Import named exports with and without alias
import { subtract, multiply as times } from './mathUtils';
// 'subtract' is used as-is
// 'multiply' is aliased locally as 'times'

// Usage
console.log(sum(5, 3)); // 8
console.log(subtract(5, 3)); // 2
console.log(times(5, 3)); // 15

import { TextInput as CDSTextInput } from '@carbon/react';

- Important add this: Examples of relative(from reference of the current file) and absolute paths (from root level)

---
