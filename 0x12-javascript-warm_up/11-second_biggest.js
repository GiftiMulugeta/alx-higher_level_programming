#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let i = 0;
  let max = 0;
  for (; i < args.length; i++) {
    if (args[i + 2] < args[i + 3]) {
      max = args[i + 3];
      args[i + 3] = max;
    }
  } console.log(max);
}
