var makeRequest = require('request');

var requestDebug = require('request-debug');

var get = requestDebug({
    url: 'https://api.heroku.com/apps/coriandrum-chatbot/config-vars',
    method: 'POST',
    headers: {
      'Accept': 'application/vnd.heroku+json; version=3'
    }
  }, function(type, data, r) {
    console.log("TYPE", type);
    console.log("DATA,", data);
    console.log("R", r);
});

// var get = function (callback) {
//   makeRequest({
//     url: 'https://api.heroku.com/apps/coriandrum-chatbot/config-vars',
//     method: 'POST',
//     headers: {
//       'Accept': 'application/vnd.heroku+json; version=3'
//     }
//   }, function (error, response, body) {
//     if (!error) {
//      // console.log("TOKENS BODY", body);
//       callback();
//     } else {
//      // console.log("TOKENS ERROR", error);
//     }
//   });
// };

module.exports = {
  get: get
};