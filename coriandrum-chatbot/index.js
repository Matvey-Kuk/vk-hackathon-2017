var bodyParser = require('body-parser');
var express = require('express');
var makeRequest = require('request');
var requestDebug = require('request-debug');

var urls = require('./helpers/urls.js');
var methods = require('./helpers/methods.js');
var texts = require('./helpers/texts.js');
requestDebug(makeRequest);

var app = express();
app.set('port', (process.env.PORT || 5000));
app.use(bodyParser.json());

app.post('/update', function (request, response) {
  console.log(request.body);
  var body = request.body;
  var reply;

  if (body.type === 'someone_considered') {
    reply = texts.onConsider();
  } else if (body.type === 'invalid') {
    reply = texts.onValidationFail();
  } else if (body.type === 'trashed') {
    reply = texts.onTrashFail();
  } else if (body.type === 'almost_published') {
    reply = texts.onAlmostPublished();
  } else if (body.type === 'published') {
    if (body.new_level_achieved) {
      reply = texts.onPublishAndAchieve(body.publications);
    } else {
      reply = texts.onPublish(body.publications);
    }
  }

  if (reply) {
    methods.replyToChat(reply, body.vk_user_id, function () {
      console.log('success');
    });
  }
  response.send('ok');
});


app.post('/', function (request, response) {
  var body = request.body;
  console.log(body);

  if (body.type === 'confirmation') {
    response.send(process.env.CONFIRM_TOKEN);
  } else if (body.type === 'message_new') {
    methods.handleNewMessage(body.object);
    response.send('ok');
  }
});

app.listen(app.get('port'), function () {
  console.log('Node app is running on port', app.get('port'));
});


