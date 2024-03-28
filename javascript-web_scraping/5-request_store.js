#!/usr/bin/node
const request = require('request');
const fd = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, {
  encoding: 'utf8'
}, function (err, response, body) {
  if (err) console.log(err);
  fd.writeFile(filePath, body, {
    encoding: 'utf8',
    flag: 'w'
  }, function (err) {
    if (err) throw err;
  });
});
