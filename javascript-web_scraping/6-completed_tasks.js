#!/usr/bin/node
const request = require('request');

let userList = [];
request('https://jsonplaceholder.typicode.com/users', function (err, response, body) {
  if (err) console.log(err);
  userList = JSON.parse(body);
  const tempDict = {};
  userList.forEach(user => {
    tempDict[user.id] = 0;
  });
  request(process.argv[2], function (err, response, body) {
    if (err) console.log(err);
    const list = JSON.parse(body);
    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        const temp = tempDict[list[i].userId];
        tempDict[list[i].userId] = temp + 1;
      }
    }
    const endDict = {};
    Object.keys(tempDict).forEach(key => {
      if (tempDict[key] !== 0) {
        endDict[key] = tempDict[key];
      }
    })
    console.log(endDict);
  });
});
