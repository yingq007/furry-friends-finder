function showFavorite(evt) {
  $.get('/favorite_dogs', (res) => {
      
    let fav = res.favorite;
    let user = res.user;
    // let css_style_line = "<link rel='stylesheet' href='/static/mystyle.css'>";
    // $('#favorite_dogs').append(css_style_line);
    let container_div = "<div class='container'>";
    $('#favorite_dogs').append(container_div);
    for (let i=0; i < fav.length; i++) {
      current_fav = fav[i]

      let out = "<div id='name-card'>" + `<h1>${current_fav['animal_name']}</h1>` 
       + `Animal id: ${current_fav['animal_id']}<br>`
       + `Description: ${current_fav['animal_description']}<br>`
       + `Spayed or Neutered: ${current_fav['spayed_neutered']}<br>`
       + `Age: ${current_fav['age']}<br>`
       + `Gender: ${current_fav['gender']}<br>`
       + `Primary Breed: ${current_fav['primary_breed']}<br>`
       + `Email: ${current_fav['email']}<br>`
       + `Phone: ${current_fav['phone_number']}<br>`
       + `Petfinder URL: <a href ="${current_fav['url']}">Click Me</a><br>`
       + `Organization Animal ID: ${current_fav['organization_animal_id']}<br>`
       + `<img src=${current_fav['photo']} width="330" height="280">`
       + "</div>";

     $('#favorite_dogs').append(out);
     $('#email').text(user.email);
    }  
    $('#favorite_dogs').append("</div>");

  });

  $('#animals_available').hide();
  console.log(out)
}   

$.get('/favorite_dogs', (res) => {
  $('#email').text(res.user.email);
})

$("#email").css("margin-left", "600px");
$("#email").css("font-size", "20px");

// function newShowFav(res){
//   let fav = res.favorite;
//   let user = res.user;
//   for (let i=0; i < fav.length; i++) {
//     current_fav = fav[i]

//     let out = "<p>" + `<h1>${current_fav['animal_name']}</h1>` 
//      + `Animal id: ${current_fav['animal_id']}<br>`
//      + `Description: ${current_fav['animal_description']}<br>`
//      + `Spayed or Neutered: ${current_fav['spayed_neutered']}<br>`
//      + `Age: ${current_fav['age']}<br>`
//      + `Gender: ${current_fav['gender']}<br>`
//      + `Primary Breed: ${current_fav['primary_breed']}<br>`
//      + `Email: ${current_fav['email']}<br>`
//      + `Phone: ${current_fav['phone_number']}<br>`
//      + `URL: ${current_fav['url']}<br>`
//      + `Organization Animal ID: ${current_fav['organization_animal_id']}<br>`
//      + `<img src=${current_fav['photo']} image.style.width = '90'>`
//      + "</p>";

//    $('#favorite_dogs').append(out);
//    $('#email').text(user.email);
//   }
// }
$('#get-favorite-button').on('click', showFavorite);
$("#get-favorite-button").css("margin-left", "576px");
$("#get-favorite-button").css("font-size", "25px");
$("#get-favorite-button").css("margin-top", "20px");
$("#get-favorite-button").css("background-color", "tomato");
$("#get-favorite-button").css("color", "white");
