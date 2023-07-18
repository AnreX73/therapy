document.addEventListener('DOMContentLoaded', function() {
  sunAdd = document.querySelectorAll('.decor-div');
  
  sunAdd.forEach(function(item){
    setTimeout(() => {
        item.classList.add('active');
        item.classList.add('slide-from-right');
      }, 1000);
    
  })
  
});