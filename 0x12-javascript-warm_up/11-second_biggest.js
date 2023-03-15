#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let i = 0;
  let max = args[i + 2];
  for (; i < args.length; i++) {
    if (args[i + 3] > args[i + 2]) {
      max = args[i + 3];
    }
  } console.log(max);
}
