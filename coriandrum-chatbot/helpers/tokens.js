var makeRequest = require('request');

var requestDebug = require('request-debug');

requestDebug(makeRequest);

console.log("PROCESS.ENV", process.env.API_Key,
 (Buffer.from(process.env.API_Key).toString('base64'));

var get = function (callback) {
  makeRequest({
    url: 'https://api.heroku.com/apps/coriandrum-chatbot/config-vars',
    method: 'GET',
    headers: {
      'Accept': 'application/vnd.heroku+json; version=3',
      'Authorization': 'Basic ' + (Buffer.from(process.env.API_Key).toString('base64')
    }
  }, function (error, response, body) {
    // console.log(error);
    // console.log(response);
    console.log(body);
    if (!error) {
     // console.log("TOKENS BODY", body);
      callback();
    } else {
     // console.log("TOKENS ERROR", error);
    }
  });
};

module.exports = {
  get: get
};