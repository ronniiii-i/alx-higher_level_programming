#!/usr/bin/node
// const request = require('request');
// request.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`)
//   .on('response', function (response) {
//     console.log(`code: ${response.statusCode}`);
//   });

const https = require('https');
https.get(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, res => {
  // console.log('Status Code:', res.statusCode);
  res.on('data', (d) => {
    console.log(d);
  });
//   console.log(data);
});
