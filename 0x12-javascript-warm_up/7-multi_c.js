#!/usr/bin/node

const arg = process.argv[2];
const s = 'C is fun';

if (arg === undefined) {
  console.log('Missing number occurences');
}
for (let i = 0; i < arg; i++) {
  console.log(s);
}
