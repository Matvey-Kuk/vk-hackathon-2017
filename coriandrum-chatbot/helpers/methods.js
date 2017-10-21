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

    // reply to chat
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

        var dbUserId;

        // find user
        makeRequest({
          url: urls.CRNDRM_USERS + userId,
          method: 'GET'
        }, function (error, response, body) {
          if (!error && response.statusCode == 404) {
            console.log("404");

            // if user doesn't exist, create it
            makeRequest({
              url: urls.CRNDRM_USERS,
              method: 'POST',
              form: {
                vk_user_id: userId
              }
            }, function (error, response, body) {
              console.log("post body", body);
              if (body && body.id) {
                dbUserId = body.id;
              }
            });
          } else {
            console.log("EXISTING USER", body);

          }
        });

        console.log("dbUserId", dbUserId);
      } else {
        console.log("ERROR", error);
      }
    });
};

module.exports = {
  handleNewMessage: handleNewMessage
};