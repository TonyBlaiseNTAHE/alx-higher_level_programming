#!/usr/bin/node

const args = process.argv;
let i = 2;

while (args[i] !== undefined) {
  console.log(args[i]);
  i++;
}
if (i === 2) {
  console.log('No argument');
}
