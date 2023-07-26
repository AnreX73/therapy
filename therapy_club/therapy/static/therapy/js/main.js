document.addEventListener('DOMContentLoaded', function() {
  redButton = document.querySelector('.btn-5');
  setTimeout(() => {
    
    redButton.classList.add('slide-from-right');
    redButton.classList.add('active');

  }, 700);
  

  
});