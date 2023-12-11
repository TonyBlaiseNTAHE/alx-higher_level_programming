#!/usr/bin/node

const n = process.argv[2];

if (n === undefined) {
  console.log('Missing size');
} else if (n >= 'a' && n <= 'z') {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    if (i < n - 1) {
      console.log();
    }
  }
  console.log();
}
