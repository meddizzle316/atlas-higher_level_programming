#!/usr/bin/node

const characterUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
console.log(characterUrl);
let object = {};
$.ajax({
  url: characterUrl,
  dataType: 'json',
  success: function (data) {
    // console.log(data)
    object = data;
    console.log(object);
    for (const key in object) {
      // console.log(object[key]);
      $('DIV#character').append('<div>' + object[key] + '</div>');
    }
  }
});
