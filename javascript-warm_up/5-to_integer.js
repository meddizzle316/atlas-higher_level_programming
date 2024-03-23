#!/usr/bin/node
const string = process.argv[2];
const num = Number(string);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
