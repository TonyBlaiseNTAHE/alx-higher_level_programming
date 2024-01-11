#!/usr/bin/node
exports.converter = function converter (base) {
  return num => num.toString(base);
};
