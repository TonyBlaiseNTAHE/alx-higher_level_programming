#!/usr/bin/node

const n = process.argv[2];
let i = 0;

if (n === undefined) {
  console.log('Missing number of occurrences');
}
for (; i < n; i++) {
  console.log('C is fun');
}
