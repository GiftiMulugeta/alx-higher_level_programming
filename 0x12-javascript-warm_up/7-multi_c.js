#!/usr/bin/node
const args = process.argv;
let i = 0;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else if (args[2] >= 0) {
  for (; i < args[2]; i++) {
    console.log('C is fun');
  }
}
