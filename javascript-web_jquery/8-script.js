#!/usr/bin/node

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  dataType: 'json',
  success: function (data) {
    const results = data.results;
    for (const key in results) {
      $('UL#list_movies').append('<li>' + results[key].title + '</li>');
    }
  }
});
