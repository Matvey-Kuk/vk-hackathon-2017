var makeRequest = require('request');

var get = function (callback) {
  makeRequest({
    url: 'https://api.heroku.com/apps/coriandrum-chatbot/config-vars',
    method: 'POST'
  }, function (error, response, body) {
      if (!error && response.statusCode == 200) {

        console.log("TOKENS RESPONSE", response);
          callback();
      } else {
          console.log("TOKENS ERROR", error);
      }
  });
};

module.exports = {
  get: get
};