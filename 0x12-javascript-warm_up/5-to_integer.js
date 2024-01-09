#!/usr/bin/node

const arg1 = process.argv[2];
if (isNaN(arg1) === true) {
  console.log('Not a number');
} else {
    let n = parseInt(arg1);
  console.log(`My number: ${n}`);
}
