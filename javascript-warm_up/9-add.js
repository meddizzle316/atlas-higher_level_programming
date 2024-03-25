#!/usr/bin/node
const firstString = process.argv[2];
const secondString = process.argv[3];

const firstNum = Number(firstString);
const secondNum = Number(secondString);

function add (a, b) {
  return a + b;
}

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log('NaN');
} else {
  const result = add(firstNum, secondNum);
  console.log(result);
}
