
var urls = require('./urls.js');

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
            console.log("BODY", body);
        } else {
            console.log("ERROR", error);
        }
    });
};

module.exports = {
  handleNewMessage: handleNewMessage
};