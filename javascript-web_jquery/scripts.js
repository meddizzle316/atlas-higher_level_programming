#!/usr/bin/node
$(function () {
  $.ajax({
    type: 'GET',
    url: '/api/orders',
    success: function (data) {
      console.log('success', data);
    }
  });
});
