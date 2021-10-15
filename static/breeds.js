$.get('/api/breed'), (res) =>{
  console.log(res.result);
  for (const breed of res['result']){
    $('#breeds').append(`<li>${breed['name']}</li>`);
  }
};

