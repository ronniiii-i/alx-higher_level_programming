#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (value in newDict) {
      newDict[value].push(parseInt(key));
    } else {
      newDict[value] = [parseInt(key)];
    }
  }
}

console.log(newDict);
