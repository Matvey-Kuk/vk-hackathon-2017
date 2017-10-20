var makeRequest = require('request');

var get = function (callback) {
  makeRequest({
    url: 'https://api.heroku.com/apps/coriandrum-chatbot/config-vars',
    method: 'POST',
    form: {
      'Accept': 'application/vnd.heroku+json; version=3'
    }
  }, function (error, response, body) {
    if (!error) {
      console.log("TOKENS BODY", body);
      callback();
    } else {
      console.log("TOKENS ERROR", error);
    }
  });
};

module.exports = {
  get: get
};