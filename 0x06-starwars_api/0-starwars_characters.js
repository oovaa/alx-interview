#!/usr/bin/node

import fetch from 'node-fetch';

const movieId = process.argv[2];

async function fetchData (movieId = 3) {
  const URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  const res = await fetch(URL);

  const resJson = await res.json();

  // console.log(resJson['characters'])
  const charactersList = resJson.characters;

  for (const characterURL of charactersList) {
    // console.log(characterURL)
    const charactersREQ = await fetch(characterURL);
    const charactersJSON = await charactersREQ.json();
    // console.log(charactersJSON)
    const charactersNAME = charactersJSON.name;
    console.log(charactersNAME);
  }
}

fetchData(movieId).catch(console.error); // Added catch to handle potential errors
