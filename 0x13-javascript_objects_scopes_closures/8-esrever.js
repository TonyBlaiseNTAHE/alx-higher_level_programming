#!/usr/bin/node
exports.esrever = function (list) {
  const listCopy = [];
  let j = 0;
  let i = list.length - 1;
  for (; i >= 0; i--) {
    listCopy[j] = list[i];
    j++;
  }
  return listCopy;
};
