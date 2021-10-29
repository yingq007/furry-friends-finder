function showFavorite(evt) {
    // TODO: get the fortune and show it in the #fortune-text div
  $.get('/favorite_dogs', (res) => {
      
    let fav = res.favorite;
    
    for (let i=0; i < fav.length; i++) {
      current_fav = fav[i]

      let out = "<p>" + `<h1>${current_fav['animal_name']}</h1>` 
       + `Animal id: ${current_fav['animal_id']}<br>`
       + `Description: ${current_fav['animal_description']}<br>`
       + `Spayed or Neutered: ${current_fav['spayed_neutered']}<br>`
       + `Age: ${current_fav['age']}<br>`
       + `Gender: ${current_fav['gender']}<br>`
       + `Primary Breed: ${current_fav['primary_breed']}<br>`
       + `Email: ${current_fav['email']}<br>`
       + `Phone: ${current_fav['phone_number']}<br>`
       + `URL: ${current_fav['url']}<br>`
       + `Organization Animal ID: ${current_fav['organization_animal_id']}<br>`
       + `<img src=${current_fav['photo']} image.style.width = '90'>`
       + "</p>";

     $('#favorite_dogs').append(out);
    }   
  });

  $('#animals_available').hide();
}   

$('#get-favorite-button').on('click', showFavorite);
