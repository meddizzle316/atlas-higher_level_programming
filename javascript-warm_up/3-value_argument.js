#!/usr/bin/node

for (let i = 0; i <= 2; i++) {
  if (i === 2) {
    if (process.argv[i] === undefined) {
      console.log('No argument');
    } else {
      console.log(process.argv[i]);
    }
  }
}
