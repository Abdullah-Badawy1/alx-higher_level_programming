#!/usr/bin/node
const numberArgument = process.argv[2];
if (!isNaN(numberArgument)) {
  if (numberArgument >= 0) {
    for (let i = 0; i < numberArgument; i++) {
      let lineEmpty = '';
      for (let o = 0; o < numberArgument; o++) {
        lineEmpty += 'X';
      }
      console.log(lineEmpty);
    }
  }
} else {
  console.log('Missing size');
}
