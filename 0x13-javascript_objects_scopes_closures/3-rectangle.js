#!/usr/bin/node

module.exports = class Rectangle {
	constructor (w , h) {
		this.width = w;
		this.height = h;
		if (w > 0 && h > 0) {
		
		}
	}

	print (u = 'X') {
		or (let i = 0; i < this.height; i++) {
      console.log(u.repeat(this.width));
    }
  }
};
