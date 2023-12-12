#!/usr/bin/node
class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
