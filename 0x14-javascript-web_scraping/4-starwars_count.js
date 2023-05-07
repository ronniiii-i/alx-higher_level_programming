#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/', function (error, response, body) {
  console.log(error || JSON.parse(body).count);
});
