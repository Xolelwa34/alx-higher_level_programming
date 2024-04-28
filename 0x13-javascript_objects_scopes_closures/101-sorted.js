#!/usr/bin/node

const dict = require('./101-data.js').dict;
let listed = {};
for (let key in dict) {
  if (listed[dict[key]] === undefined) {
    listed[dict[key]] = [key];
  } else {
    listed[dict[key]].push(key);
  }
}
console.log(listed);
