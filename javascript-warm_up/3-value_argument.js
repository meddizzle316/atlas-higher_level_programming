#!/usr/bin/node

for (let i = 0; i <= 3; i++) {
  if (i === 2) {
    try {
      console.log(process.argv[i]);
    } catch (e) {
      console.log('No argument');
    }
  }
}
