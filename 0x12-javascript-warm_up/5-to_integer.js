#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else if (typeof Number(args[2]) === 'number') {
  console.log('My number: ' + Math.trunc(args[2]));
}
