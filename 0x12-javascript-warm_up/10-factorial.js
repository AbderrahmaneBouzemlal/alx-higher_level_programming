#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  let result = 1;
  const d = parseInt(a);
  if (d > 0) {
    result = d * factorial(d - 1);
    return result;
  } else {
    return result;
  }
}
console.log(factorial(argv[2]));
