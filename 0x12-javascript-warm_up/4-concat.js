#!/usr/bin/node
const args = process.argv;
if (typeof args[2] === 'undefined' && typeof args[3] === 'undefined') {
  console.log(typeof args[2] + ' is ' + typeof args[3]);
} else if (args[2] !== 'undefined' && args[33] !== 'undefined') {
  console.log(args[2] + ' is ' + args[3]);
}
