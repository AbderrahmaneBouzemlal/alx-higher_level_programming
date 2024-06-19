#!/usr/bin/node
const { argv } = require('node:process');
const x = argv[2];
const argc = argv.length;

if (argc < 3 || isNaN(x)) {
  console.log('Missing size');
} else if (!(isNaN(x)) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
