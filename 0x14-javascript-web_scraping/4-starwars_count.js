#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  let count = 0;
  const myObj = JSON.parse(body);
  const results = myObj.results;
  for (let i = 0; i < results.length; i++) {
    const characters = results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const num = characters[j].substr(-3);
      if (num === '18/') {
        count++;
      }
    }
  }
  console.log(count);
});
