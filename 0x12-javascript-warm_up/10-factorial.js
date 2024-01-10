#!/usr/bin/node

function fact (n) {
  if (n === undefined) {
    console.log(1);
    return;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const arg1 = process.argv[2];
const result = fact(arg1);
console.log(result);
