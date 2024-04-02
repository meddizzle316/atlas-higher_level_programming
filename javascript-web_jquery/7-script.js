#!/usr/bin/node

const character_url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
console.log(character_url);
let object = {};
$.ajax({
  url: character_url,
  dataType: 'json',
  success: function(data) {
    // console.log(data)
    object = data;
    console.log(object);
    for (let key in object) {
      // console.log(object[key]);
      $('DIV#character').append('<div>' + object[key] + '</div>');
    }
  }
})

