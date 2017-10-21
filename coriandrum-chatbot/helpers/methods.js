var urls = require('./urls.js');
var makeRequest = require('request');
var requestDebug = require('request-debug');

var sendToDb = function (dbUserId, text, attachments) {
  makeRequest({
    url: urls.CRNDRM_POST,
    method: 'POST',
    form: {
      author: dbUserId,
      text: text,
      attachments: JSON.stringify(attachments)
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



var createNewUserHandler = function (error, response, body) {
  if (body && body.id) {
    dbUserId = body.id;
  }
};

var findUserHandler = function (error, response, body) {
  if (!error && response.statusCode == 404) {
    createNewUser(userId, createNewUserHandler);
  } else {
    console.log("EXISTING USER", JSON.parse(body).id);
    dbUserId = JSON.parse(body).id;
  }
  // send to db

  console.log("dbuserid", dbUserId);
  sendToDb(dbUserId, text, attachments);
};

var replyHandler = function (error, response, body) {
  console.log(body);
  if (!error && response.statusCode == 200) {

    var dbUserId;

    // find user
    findUser(userId, findUserHandler);

  } else {
   // console.log("ERROR", error);
  }
};

var handleNewMessage = function (object) {
    var userId = object.user_id;
    var text = object.body;
    var attachments = object.attachments;
    var reply;

    switch (text) {
      case '1':
        console.log('1');
        reply = '11112';
        break;
      default:
        console.log('default');
        reply = 'default2';
    }

    // reply to chat
    replyToChat(reply, userId, replyHandler);
};

module.exports = {
  handleNewMessage: handleNewMessage
};