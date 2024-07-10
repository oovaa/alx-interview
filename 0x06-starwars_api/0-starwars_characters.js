#!/usr/bin/node

const request = require('request');

// Check if a movie ID is provided
if (process.argv.length < 3) {
  console.log('Usage: ./script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

// Fetch the movie details
request(
  'https://swapi.dev/api/films/' + movieId + '/',
  function (err, res, body) {
    if (err) throw err;

    // Parse the response body
    const actors = JSON.parse(body).characters;

    // Function to print characters in exact order
    const exactOrder = (actors, index) => {
      if (index === actors.length) return;

      // Fetch each character details
      request(actors[index], function (err, res, body) {
        if (err) throw err;

        // Print the character name
        console.log(JSON.parse(body).name);

        // Recursive call to process the next character
        exactOrder(actors, index + 1);
      });
    };

    // Start the process with the first character
    exactOrder(actors, 0);
  }
);
