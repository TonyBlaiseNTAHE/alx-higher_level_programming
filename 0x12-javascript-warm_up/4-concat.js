#!/usr/bin/node

const is = ' is ';
const args = process.argv;
let i = 2;

if (process.argv[i] === undefined) {
  console.log(process.argv[i] + is + process.argv[i]);
}
for (i = 2; i < args.length; i++) {
  console.log(process.argv[i] + is + process.argv[i + 1]);
}
