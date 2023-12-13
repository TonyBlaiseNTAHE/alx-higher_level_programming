#!/usr/bin/node
const map1 = require('./100-data.js').list;
console.log(map1);
console.log(map1.map((item, index) => item * index));
