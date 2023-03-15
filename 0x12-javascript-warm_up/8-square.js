#!/usr/bin/node
const args = process.argv;
let i = 0;
let j = 0;
let x = '';
if (isNaN(args[2])) {
  console.log('Missing size');
} else if (args[2] > 0) {
  for (; i < args[2]; i++) {
    for (; j < args[2]; j++) {
      x += 'x';
    }
    console.log(x);
  }
}
