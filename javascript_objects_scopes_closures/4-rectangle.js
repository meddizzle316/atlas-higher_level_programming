#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      /* */
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = (2 * this.height);
    this.width = (2 * this.width);
  }
}

module.exports = Rectangle;
