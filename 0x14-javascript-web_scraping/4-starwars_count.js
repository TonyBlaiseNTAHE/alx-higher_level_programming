#!/usr/bin/node
/**
 * script that prints the title of a star Wars movie
 */
const request = require('request');
// Extract the movie ID from the command-line arguments

// Construct the API URL with the provided movie ID
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode >= 200 && response.statusCode < 300) {
    const data = JSON.parse(body);
    let count = 0;

    data.results.forEach(movie => {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        // Increment the counter
        count++;
      }
    });
    console.log(count);
  } else {
    console.log('Resquest failed with status code:', response.statusCode);
  }
});
