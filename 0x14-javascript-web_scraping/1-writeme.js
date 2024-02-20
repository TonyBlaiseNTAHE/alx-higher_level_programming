#!/usr/bin/node
/**
 * a script that write on a file
 */

const fs = require('fs');

const fileName = process.argv[2];
const content = process.argv[3];
// Open the file
fs.open(fileName, 'w', (err, fd) => {
  if (err) {
    console.error('Error opening the file:', err);
    return;
  }
  // write data to the file
  fs.write(fd, content, (err) => {
    if (err) {
      console.error('Error writting to the file:', err);
    } else {
      console.log('Data written successfully.');
    }
    // close the file
    fs.close(fd, (err) => {
      if (err) {
        console.error('Error closing the file:', err);
      }
    });
  });
});
