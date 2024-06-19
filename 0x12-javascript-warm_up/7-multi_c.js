#!/usr/bin/node
const { argv } = require('node:process');
const x = argv[2];
const argc = argv.length;
if (argc < 3) {
  console.log('Missing number of occurrences');
} else if (argc === 3 && !(isNaN(x)) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
