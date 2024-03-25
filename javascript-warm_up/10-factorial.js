#!/usr/bin/node
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * (factorial(num - 1));
  }
}

if (!isNaN(Number(process.argv[2]))) {
  console.log(factorial(process.argv[2]));
} else {
  console.log(1);
}
