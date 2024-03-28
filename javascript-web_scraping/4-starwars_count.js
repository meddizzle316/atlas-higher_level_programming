#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];
request(baseUrl, {
  encoding: 'utf8'
}, function (err, response, body) {
  if (err) console.log(err);
  const http = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < http.results.length; i++) {
    if (http.results[i].characters.includes('18')) {
      count++;
    }
  }
  console.log(count);
});
