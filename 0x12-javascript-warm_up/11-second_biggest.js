#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort(function (a, b) { return a - b; });
  console.log(sorted[sorted.length - 2]);
}
