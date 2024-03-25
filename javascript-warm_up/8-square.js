#!/usr/bin/node
const string = process.argv[2];
const num = Number(string);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let x = 0; x < num; x++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
