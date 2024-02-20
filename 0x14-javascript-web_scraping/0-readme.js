#!/usr/bin/node
/**
 * script that read and write data from file
 */

const fs = require('fs');

// Getting the file name from the arguments
const fileName = process.argv[2];

// read data from the file and write then using fs
fs.readFile(fileName, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }
  console.log(data);
});
