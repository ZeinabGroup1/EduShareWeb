

/**
 * Gallery Category Filter
 */
const filterCategory = () =>{
    var cats = document.querySelectorAll('#gallery #gallery-categories .btn')
    cats.forEach(cat=>{
        cat.addEventListener('click', e=>{
            e.preventDefault()
            if(cat.parentElement.querySelector('.active') != undefined){
                cat.parentElement.querySelector('.active').classList.remove('active')
            }
            cat.classList.add('active')
            var catName = cat.dataset.category || 'all'
            var catItems = document.querySelectorAll('#gallery-container .gallery-item')
            catItems.forEach(el => {
                if(el.dataset.category == catName || catName == 'all'){
                    if(el.classList.contains('hide'))
                    el.classList.remove('hide')
                }else{
                    if(!el.classList.contains('hide'))
                    el.classList.add('hide')
                }
            })
        })
    })
}


$(document).ready(function() {
    // Fetch the latest skills and display them in the Discover section
    $.get('https://api.example.com/latest-skills', function(data) {
      var skills = data.skills;
      var skillCards = '';
  
      // Create HTML for each skill card
      for (var i = 0; i < skills.length; i++) {
        var skill = skills[i];
        var card = '<div class="col-md-4">' +
                     '<div class="card">' +
                       '<img src="' + skill.image + '" class="card-img-top" alt="' + skill.title + '">' +
                       '<div class="card-body">' +
                         '<h5 class="card-title">' + skill.title + '</h5>' +
                         '<p class="card-text">' + skill.description + '</p>' +
                         '<a href="#" class="btn btn-primary">Learn More</a>' +
                       '</div>' +
                     '</div>' +
                   '</div>';
  
        skillCards += card;
      }
  
      // Append the skill cards to the Discover section
      $('#discover-cards').html(skillCards);
    });
  });
  
