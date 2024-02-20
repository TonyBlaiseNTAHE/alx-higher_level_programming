#!/usr/bin/node
/**
 * script that sends a GET request
 */
const axios = require('axios');

const url = process.argv[2];

axios.get(url)
  .then(response => {
    console.log('code:', response.status);
  })
  .catch(error => {
    console.error('Error:', error);
  });
