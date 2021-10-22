function showFavorite(evt) {
    // TODO: get the fortune and show it in the #fortune-text div
    $.get('/favorite_dogs', (res) => {
      $('#favorite_dogs').html(res);
    });
  }