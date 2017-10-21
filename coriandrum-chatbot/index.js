var bodyParser = require('body-parser');
var express = require('express');
var app = express();
var makeRequest = require('request');
var requestDebug = require('request-debug');
var URLS = require('./helpers/urls');

requestDebug(makeRequest);

//var MESSAGES_SEND_URL = 'https://api.vk.com/method/messages.send';

app.set('port', (process.env.PORT || 5000));
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());

app.post('/', function(request, response){
  ///console.log("REQUEST BODY:", request.body);

  var body = request.body;

  if (body.type === 'confirmation') {
    response.send(process.env.CONFIRM_TOKEN);
  } else if (body.type === 'message_new') {
    var userId = body.object.user_id;
    var text = body.object.body;
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

    makeRequest({
      url: URLS.VK_MESSAGES_SEND,
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

    response.send('ok');
  }

});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


