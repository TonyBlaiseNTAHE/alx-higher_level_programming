#!/usr/bin/node
/**
 * script that sends a GET request
 */
const request = require('request');
request(process.argv[2], function (error, response) {
    if (error == null) {
        console.log('code:' + response.statusCode);
    }
});
