$(document).ready(function () {
  var btn = $("#share-btn");

  VK.init(function() { 

    btn.on('click', function () {
      VK.api("wall.post", {
        "message": "Я уважаемый человек в Лентаче https://vk.com/app6228819"
      }, function (data) {
        console.log("Post ID:" + data.response.post_id);
      });
    });

  }, function() {

  }, '5.68')
});

