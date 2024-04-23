#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (l) {
    if (l === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(l.repeat(this.width));
    }
  }
};
