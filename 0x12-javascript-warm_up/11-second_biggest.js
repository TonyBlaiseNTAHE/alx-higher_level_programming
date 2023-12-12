#!/usr/bin/node

const args = process.argv;

if (args.length <= 2) {
  console.log(0);
} else {
  // Convert arguments to integers
  const numbers = [];
  for (let i = 2; i < args.length; i++) {
    numbers.push(parseInt(args[i]));
  }

  // Find the second largest number
  let firstLargest = numbers[0];
  let secondLargest = Math.min(...numbers);
  for (const num of numbers) {
    if (num > firstLargest) {
      secondLargest = firstLargest;
      firstLargest = num;
    } else if (num > secondLargest && num !== firstLargest) {
      secondLargest = num;
    }
  }
  if (numbers.length === 1) {
    console.log(0);
  } else {
    console.log(secondLargest);
  }
}
