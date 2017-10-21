var urls = require('./urls.js');
var makeRequest = require('request');
var requestDebug = require('request-debug');

var handleNewMessage = function (object) {
    var userId = object.user_id;
    var text = object.body;
    var reply;

    switch (text) {
      case '1':
        console.log('1');
        reply = '1111___';
        break;
      default:
        console.log('default');
        reply = 'default____';
    }

    makeRequest({
      url: urls.VK_MESSAGES_SEND,
      method: 'POST',
      form: {
        'message': reply,
        'access_token': process.env.ACCESS_TOKEN,
        'user_id': userId
      }
    }, function (error, response, body) {
      if (!error && response.statusCode == 200) {
        // Print out the response body
        //console.log("BODY", body);

        makeRequest({
          url: urls.CRNDRM_USERS + userId,
          method: 'GET'
        }, function (error, response, body) {
          //console.log("STATUS", response.statusCode);
          if (!error && response.statusCode == 404) {
            console.log("404");
            makeRequest({
              url: urls.CRNDRM_USERS + userId,
              method: 'POST'
            }, function (error, response, body) {
              console.log("post body", body);
            });
          } else {
            console.log("BODY", body);
          }
          //console.log("CRDRMMM::", body);
        });
      } else {
        console.log("ERROR", error);
      }
    });
};

module.exports = {
  handleNewMessage: handleNewMessage
};