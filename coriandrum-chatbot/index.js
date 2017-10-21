var bodyParser = require('body-parser');
//var express = require('express');
var makeRequest = require('request');
var requestDebug = require('request-debug');

var urls = require('./helpers/urls.js');
var methods = require('./helpers/methods.js');
requestDebug(makeRequest);

//var app = express();
app.set('port', (process.env.PORT || 5000));
//app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());

app.post('/', function(request, response) {
  var body = request.body;

  ///console.log("msg from callback", body.object.attachments);
  if (body.type === 'confirmation') {
    response.send(process.env.CONFIRM_TOKEN);
  } else if (body.type === 'message_new') {
    methods.handleNewMessage(body.object);
    response.send('ok');
  }
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


