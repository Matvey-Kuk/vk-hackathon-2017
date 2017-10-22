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

app.post('/', function (request, response) {
  var body = request.body;

  if (body.type === 'confirmation') {
    response.send(process.env.CONFIRM_TOKEN);
  } else if (body.type === 'message_new') {
    methods.handleNewMessage(body.object);
    response.send('ok');
  }
});

app.post('/update', function (request, response) {
  console.log(request.body);
  var body = request.body;
  var reply;
  if (body.type === 'new_post') {
    reply = 'new post send';
  } else if (body.type === 'someone_considered') {
    reply = texts.onConsider();
  }

  methods.replyToChat(reply, body.vk_user_id, function () {
    console.log('success');
  });
  response.send('ok');
});

app.listen(app.get('port'), function () {
  console.log('Node app is running on port', app.get('port'));
});


