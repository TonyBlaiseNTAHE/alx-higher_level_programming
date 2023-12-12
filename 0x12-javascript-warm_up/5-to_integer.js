#!/usr/bin/node

const n = process.argv[2];

if (n === undefined) {
  console.log('Not a number');
} else if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(n));
}
