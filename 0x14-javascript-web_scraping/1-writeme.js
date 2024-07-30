#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('node:fs');

fs.writeFile(`${argv[2]}`, `${argv[3]}`, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
