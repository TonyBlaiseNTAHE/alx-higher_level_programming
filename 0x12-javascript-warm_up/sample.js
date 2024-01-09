#!/usr/bin/node

/* if not argument are passed print "No argument"*/
if (process.argv[2] === undefined) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}