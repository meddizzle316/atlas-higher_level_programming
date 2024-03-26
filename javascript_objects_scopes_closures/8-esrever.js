#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  for (let i = 0; i < list.length; i++) {
    reverseList.unshift(list[i]);
  }
  return reverseList;
};
