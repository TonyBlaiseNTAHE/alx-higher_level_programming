#!/usr/bin/node
/**
 * script that prints the title of a star Wars movie
 */
const request = require('request');
// Extract the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode >= 200 && response.statusCode < 300) {
    const data = JSON.parse(body);
    const title = data.title;
    console.log(title);
  } else {
    console.log('Resquest failed with status code:', response.statusCode);
  }
});
