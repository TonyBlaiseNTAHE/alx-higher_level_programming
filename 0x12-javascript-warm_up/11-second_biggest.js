#!/usr/bin/node

const len = process.argv.length;

if (len < 4) {
  console.log(0);
} else {
  const array = process.argv;
  let firstMax = Number(array[2]);
  let secondMax = Number(array[3]);

  if (secondMax > firstMax) {
    [firstMax, secondMax] = [secondMax, firstMax];
  }
  for (let i = 4; i < len; i++) {
    const currentNumber = Number(array[i]);
    if (!isNaN(currentNumber)) {
      if (currentNumber > firstMax) {
        secondMax = firstMax;
        firstMax = currentNumber;
      } else if (currentNumber < firstMax && currentNumber > secondMax) {
        secondMax = currentNumber;
      }
    }
  }
  console.log(secondMax);
}
