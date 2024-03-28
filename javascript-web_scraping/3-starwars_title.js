#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.hbtn.io/api/films/';
const requestUrl = baseUrl + process.argv[2] + '/';
request(requestUrl, (err, response, body) => {
  if (err) console.log(err);
  const mainBody = JSON.parse(body);
  const title = mainBody.title;
  console.log(title);
});
