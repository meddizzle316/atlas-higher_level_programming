#!/usr/bin/node

const stringList = [
  { string: 'C is fun' },
  { string: 'Python is cool' },
  { string: 'JavaScript is amazing' }
];

for (let i = 0; i < 3; i++) {
  console.log(stringList[i].string);
}
