#!/usr/bin/node

fd = require('fs');
const filePath = process.argv[2];
const string = process.argv[3] + '\n';
fd.writeFile(filePath, string, {
  encoding: 'utf8'
}, function (err, file) {
  if (err) throw err;
})
