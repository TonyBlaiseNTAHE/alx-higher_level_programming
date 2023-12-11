#!/usr/bin/node

const i = parseInt(process.argv[2]);

function fact (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const result = fact(i);
console.log(result);
