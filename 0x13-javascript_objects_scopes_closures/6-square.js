#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
