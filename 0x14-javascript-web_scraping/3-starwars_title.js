#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`)
  .on('data', (d) => {
    console.log(d);
  });
