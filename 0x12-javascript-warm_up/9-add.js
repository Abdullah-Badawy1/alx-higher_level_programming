#!/usr/bin/node
function add (a, b) {
  const addNum = a + b;
  console.log(addNum);
}
add(Number(process.argv[2]), Number(process.argv[3]));
