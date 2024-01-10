#!/usr/bin/node

function fact (n) {
  if (n === undefined || isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const arg1 = process.argv[2];
const result = fact(parseInt(arg1));
console.log(result);
