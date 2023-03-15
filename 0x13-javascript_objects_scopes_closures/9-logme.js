#!/usr/bin/node
// const args = process.argv.slice(2);
let count = 0;

exports.logMe = function (item) {
  // args.push(item)
  count += 1;
  // console.log(`${args.length - 1}: ${item}`);
  console.log(`${count - 1}: ${item}`);
};
