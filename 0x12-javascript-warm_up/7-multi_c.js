#!/usr/bin/node
const numberArgument = process.argv[2];
if (!isNaN(numberArgument)) {
  if (numberArgument >= 0) {
    for (let i = 0; i < numberArgument; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
