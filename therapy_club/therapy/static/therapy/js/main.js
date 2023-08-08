document.addEventListener('DOMContentLoaded', function() {

  const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
    effect:'flip',
    speed:1000,
    loop: true,
    grabCursor:true,
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
  
  });
  
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

 modalButton = document.querySelector('#js-open-modal')
 miniModalButton = document.querySelector('#mini-js-open-modal')
 modalContent = document.querySelector('.modal-content')
 overlay = document.querySelector('.overlay')
 closeCrist = document.querySelector('.js-modal-close')

 
 miniModalButton.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.add('active-modal');
  modalContent.classList.add('active-modal');
 });
  
 modalButton.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.add('active-modal');
  modalContent.classList.add('active-modal');
 });
  
 closeCrist.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.remove('active-modal');
  modalContent.classList.remove('active-modal');
 });
  
 overlay.addEventListener('click', function() {
  document.querySelector('.modal-content.active-modal').classList.remove('active-modal');
  this.classList.remove('active-modal');
});

 dropdown = document.querySelectorAll('.dropdown-menu');
 nav = document.querySelector('.nav-menu');
 burger = document.querySelector('.burger');

 dropdown.forEach(function(item){
  item.addEventListener('click', function(){
    nav.classList.remove('open');
    burger.classList.remove('burger-active');
  });

 });




});


