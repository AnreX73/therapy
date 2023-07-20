document.addEventListener('DOMContentLoaded', function() {
  sunAdd = document.querySelectorAll('.decor-div');
  redButton = document.querySelector('.btn-5');
  setTimeout(() => {
    
    redButton.classList.add('slide-from-right');
    redButton.classList.add('active');

  }, 500);
  
  sunAdd.forEach(function(item){
    setTimeout(() => {
        item.classList.add('active');
        item.classList.add('slide-from-right');

      }, 1000);
    
  })
  
});