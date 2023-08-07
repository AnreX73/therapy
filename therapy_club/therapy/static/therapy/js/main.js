document.addEventListener('DOMContentLoaded', function() {
  redButton = document.querySelector('.btn-5');
  miniButton = document.querySelector('.mini-btn');
  setTimeout(() => {
    
    redButton.classList.add('slide-from-right');
    miniButton.classList.add('slide-from-right');
    miniButton.classList.add('active');
    redButton.classList.add('active');

  }, 700);
  
  
  document.querySelector('.burger').addEventListener('click', function(){
    this.classList.toggle('burger-active');
   document.querySelector('.nav-menu').classList.toggle('open'); 
  })

  modalButtons = document.querySelectorAll('.js-open-modal');
  overlay      = document.querySelector('#overlay-modal');
  closeButtons = document.querySelectorAll('.js-modal-close'); 
  console.log(modalButtons )
  console.log(overlay)
  console.log(closeButtons)
 
});


