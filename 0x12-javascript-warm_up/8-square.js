#!/usr/bin/node
const args = process.argv.slice(2);
const val = parseInt(args[0]);

if (isNaN(val)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[0]; i++) {
    let row = '';
    for (let j = 0; j < args[0]; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
