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

var getReply = function (text) {
  var reply;

  switch (text) {
    case '1':
      console.log('1');
      reply = '1111';
      break;
    default:
      console.log('default');
      reply = 'default';
  }

  return reply;
};

var handleNewMessage = function (object) {
    var userId = object.user_id;
    var text = object.body;
    var attachments = object.attachments;
    var reply;
    var dbUser;
    var dbUserid;

    //reply = getReply(text);

    reply += '🌚';

    findUser(userId, function (error, response, body) {
      if (!error && response.statusCode == 404) {
        createNewUser(userId, function (error, response, body) {
          console.log("create new user body", body);
          if (body && body.id) {
            dbUserId = body.id;
            console.log("new user id", dbUserId);
            sendToDb(dbUserId, text, attachments);

            // reply to chat
            reply += ' new user';
            replyToChat(reply, userId, function (error, response, body) {
              if (!error && response.statusCode == 200) {
                var dbUserId;
                console.log("bot success");
              } else {
                console.log("bot error", error);
              }
            });
          }
        });
      } else {
        console.log("EXISTING USER", JSON.parse(body).id);
        dbUser = JSON.parse(body);
        dbUserId = dbUser.id;

        console.log("parse", dbUser);
        reply += 'hello, ' + dbUser.vk_name ;


        //console.log("dbuserid", dbUserId);
        sendToDb(dbUserId, text, attachments);

        // reply to chat
        replyToChat(reply, userId, function (error, response, body) {
         // console.log(body);
          if (!error && response.statusCode == 200) {
            var dbUserId;
            console.log("bot success");
          } else {
            console.log("bot error", error);
          }
        });
      }

    });





};

module.exports = {
  handleNewMessage: handleNewMessage
};