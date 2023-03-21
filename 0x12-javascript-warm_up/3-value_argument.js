#!/usr/bin/node
const args = process.argv;
if (typeof args[2] === 'undefined') {
  console.log('No argument');
} else if (args[2] !== 'undefined') {
  console.log(args[2]);
}
