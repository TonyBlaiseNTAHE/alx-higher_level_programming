#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const result = add(parseInt(arg1), parseInt(arg2));

console.log(result);
