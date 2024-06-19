#!/usr/bin/node
const { argv } = require('node:process');
const argc = argv.length;

const args = Array(argc - 2);
for (let i = 0; i < args.length; i++) {
  args[i] = parseInt(argv[i + 2]);
}
function secondBiggest (arr) {
  const a = [0, 0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= a[0]) {
      a[0] = arr[i];
    }
  }
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= a[1] && arr[i] < a[0]) {
      a[1] = arr[i];
    }
  }
  return a[1];
}
console.log(secondBiggest(args));
