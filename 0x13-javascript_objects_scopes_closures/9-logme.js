#!/usr/bin/node
let flag = false;
let i = 0;

exports.logMe = function (item) {
  if (flag) {
    ++i;
    console.log(i, ':', item);
  } else {
    console.log(i, ':', item);
    flag = true;
  }
};
