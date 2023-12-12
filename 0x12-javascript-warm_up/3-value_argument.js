#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const args = process.argv.slice(2);
  console.log(args[0].split(' ')[0]);
}
