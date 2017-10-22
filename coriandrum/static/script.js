var $shareBtn = $("#share-btn");
$(document).ready(function () {
  $shareBtn.on('click', function () {
    location.replace('http://vk.com/share.php?url=' + window.location.href);
  })
});