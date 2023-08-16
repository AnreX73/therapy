document.addEventListener('DOMContentLoaded', function() {

  const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
    effect:'cube',
    speed:500,
    
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

  }, 500);
  
  
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

  // закрытие модального окна при клике по крестику
 closeCrist.addEventListener('click', (e) =>{ 
  e.preventDefault();
  overlay.classList.remove('active-modal');
  modalContent.classList.remove('active-modal');
 });

 closeCrist.addEventListener('touchend', (e) =>{ 
  e.preventDefault();
  overlay.classList.remove('active-modal');
  modalContent.classList.remove('active-modal');
 });

 // закрытие модального окна при клике по подложке 
 overlay.addEventListener('click', function() {
  document.querySelector('.modal-content.active-modal').classList.remove('active-modal');
  this.classList.remove('active-modal');
});

 overlay.addEventListener('touchend', function() {
  document.querySelector('.modal-content.active-modal').classList.remove('active-modal');
  this.classList.remove('active-modal');
});

// закрытие бургер-меню при переходе по якорю
 dropdown = document.querySelectorAll('.dropdown-menu');
 nav = document.querySelector('.nav-menu');
 burger = document.querySelector('.burger');

 dropdown.forEach(function(item){
  item.addEventListener('click', function(){
    nav.classList.remove('open');
    burger.classList.remove('burger-active');

  item.addEventListener('touchend', function() {
    nav.classList.remove('open');
    burger.classList.remove('burger-active');

    });

  });

 });



});
// модальное окно страницы категории
document.addEventListener('DOMContentLoaded', function() {
  const openModalGallery = document.querySelector('#js-open-gallery-modal')
  const overlay = document.querySelector('.overlay')
  const modalGallery = document.querySelector('.modal-gallery-content')
  const closeGalleryCrist = document.querySelector('.js-gallery-modal-close')
  

  openModalGallery.addEventListener('click', () =>{    
    overlay.classList.add('active-modal');
    modalGallery.classList.add('active-modal-gallery');
   });
    // закрытие модального окна при клике по крестику
  closeGalleryCrist.addEventListener('click', function() { 
  overlay.classList.remove('active-modal');
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
 });
  closeGalleryCrist.addEventListener('touchend', function() { 
  overlay.classList.remove('active-modal');
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
 });
 // закрытие модального окна при клике по подложке 
 overlay.addEventListener('click', function() {
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
  this.classList.remove('active-modal');
});
 overlay.addEventListener('touchend', function() {
  document.querySelector('.modal-gallery-content.active-modal-gallery').classList.remove('active-modal-gallery');
  this.classList.remove('active-modal');
});

let slides = document.querySelectorAll('.gallery-slide'),
 leftBtn = document.querySelector('.left-gallery-btn'),
 rightBtn = document.querySelector('.right-gallery-btn'),
 slideIndex = 0
    
slides[slideIndex].style.display = ('block');



});