#!/usr/bin/node

const n = process.argv[2];

if (n === undefined) {
  console.log('Not a number');
} else if (n >= 'a' && n <= 'z') {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(n));
}
