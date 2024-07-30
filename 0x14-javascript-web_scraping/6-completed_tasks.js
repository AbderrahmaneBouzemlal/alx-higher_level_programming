#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const object = {};
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  body = JSON.parse(body);
  for (let i = 0; i < body.length; i++) {
    const userId = body[i].userId;
    const completed = body[i].completed;
    if (completed && !object[userId]) {
      object[userId] = 0;
    }
    if (completed) {
      object[userId]++;
    }
  }
  console.log(object);
});
