#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let c = 0; c < body.length; ++c) {
    const characters = body[c].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
