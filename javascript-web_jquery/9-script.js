#!/usr/bin/node
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  dataType: 'json',
  success: function(data) {
    $('DIV#hello').text(data.hello);
  }
})
