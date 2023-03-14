#!/usr/bin/node
const args = process.argv.slice(2);
const val1 = parseInt(args[0]);
const val2 = parseInt(args[1]);

function add (a, b) {
  console.log(a + b);
}
add(val1, val2);
