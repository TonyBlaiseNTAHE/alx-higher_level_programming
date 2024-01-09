#!/usr/bin/node

const arg1 = process.argv[2];
if (isNaN(arg1) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ', parseInt(arg1));
}
