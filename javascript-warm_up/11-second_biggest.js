#!/usr/bin/node
let i = 2;
let max = 0;
let secondMax = 0;
while (process.argv[i] !== undefined) {
  if (Number(process.argv[i]) > max) {
    secondMax = max;
    max = Number(process.argv[i]);
  }
  i++;
}
console.log(secondMax);
