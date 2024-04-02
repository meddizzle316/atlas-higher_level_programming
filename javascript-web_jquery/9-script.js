#!/usr/bin/node
$(document).ready(function(){
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    dataType: 'json',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
})

