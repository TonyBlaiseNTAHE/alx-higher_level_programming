#!/usr/bin/node

const i = parseInt(process.argv[2]);

function fact (n) {
  if (n === 0) {
    return 1;
  } else if (n === 1) {
    return NaN;
  } else {
    return n * fact(n - 1);
  }
}

const result = fact(i);
console.log(result);
