var urls = require('./urls.js');
var makeRequest = require('request');
var requestDebug = require('request-debug');
var texts = require('./texts.js');

var sendToDb = function (dbUserId, text, attachments) {
  makeRequest({
    url: urls.CRNDRM_POST,
    method: 'POST',
    form: {
      author: dbUserId,
      text: text,
      raw_vk_attachments_payload: JSON.stringify(attachments)
    }
  });
};

var createNewUser = function (userId, callback) {
  makeRequest({
    url: urls.CRNDRM_USERS,
    method: 'POST',
    form: {
      vk_user_id: userId
    }
  }, function (error, response, body) {
    callback(error, response, body);
  });
};

var findUser = function (userId, callback) {
  makeRequest({
    url: urls.CRNDRM_USERS + userId,
    method: 'GET'
  }, function (error, response, body) {
    callback(error, response, body);
  });
};

var replyToChat = function (reply, userId, callback) {
  makeRequest({
    url: urls.VK_MESSAGES_SEND,
    method: 'POST',
    form: {
      'message': reply,
      'access_token': process.env.ACCESS_TOKEN,
      'user_id': userId
    }
  }, function (error, response, body) {
    callback(error, response, body);
  });
};

// var getReply = function (text) {
//   var reply;

//   switch (text) {
//     case '1':
//       console.log('1');
//       reply = '1111';
//       break;
//     default:
//       console.log('default');
//       reply = 'default';
//   }

//   return reply;
// };

var handleNewMessage = function (object) {
    var userId = object.user_id;
    var text = object.body;
    var attachments = object.attachments;
    var reply = '🌚';
    var dbUser;
    var dbUserId;


    var handle = function (reply, dbUser) {
      if (!dbUser || !dbUser.id) {
        return;
      }

      sendToDb(dbUser.id, text, attachments);

      replyToChat(reply, userId, function (error, response, body) {
        if (!error && response.statusCode == 200) {
          console.log("bot success");
        } else {
          console.log("bot error", error);
        }
      });
    };

    findUser(userId, function (error, response, body) {
      if (!error && response.statusCode == 404) {
        createNewUser(userId, function (error, response, body) {
          dbUser = JSON.parse(body);
          //console.log("new user", dbUser.n_all_posts);
          reply = texts.onFirstMsg();

          handle(reply, dbUser);
        });
      } else {
        dbUser = JSON.parse(body);
        //console.log("existing user", dbUser);
        if (dbUser.n_all_posts == 0) {
          reply = texts.onFirstMsg();
        } else if (dbUser.n_all_posts == 1) {
          reply = texts.onFirstSuggest();
        } else {
          reply = texts.onSuggest();
        }

        handle(reply, dbUser);
      }

    });

};

module.exports = {
  handleNewMessage: handleNewMessage
};