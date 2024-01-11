#!/usr/bin/node
let n = 0;
exports.logMe = function logMe (item) {
  console.log(`${n++}: ${item}`);
};
