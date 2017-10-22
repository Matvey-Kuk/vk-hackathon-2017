VK.init(function() { 
  VK.api("wall.post", {"message": "Hello!"}, function (data) {
    console.log("Post ID:" + data.response.post_id);
  });
}, function() {
}, '5.68')