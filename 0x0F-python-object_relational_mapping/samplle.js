#!/usr/bin/node

for (let i = 1; i <= 100; i++) {
    let x = "";

    if (i % 3 === 0){
        x += "Fizz";
    }
    if (i % 5 === 0) {
        x += "Buzz";
    }
    else {
        console.log(x || i);
    }
}