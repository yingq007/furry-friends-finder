function showAnimals(evt) {
    $.get('/animals', response => {
      let animalArray = response.result;
      console.log(animalArray)
    });