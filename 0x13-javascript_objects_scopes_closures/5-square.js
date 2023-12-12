#!/usr/bin/node
class square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = square;
