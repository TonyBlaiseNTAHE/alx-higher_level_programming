#!/usr/bin/node

const arg = process.argv[2];

if (arg === undefined || isNaN(arg) === true) {
  console.log('Missing size');
}
for (let i = 0; i < arg; i++) {
  let row = '';
  for (let j = 0; j < arg; j++) {
    row += 'X';
  }
  console.log(row);
}
