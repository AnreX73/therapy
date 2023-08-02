document.addEventListener('DOMContentLoaded', function() {
  redButton = document.querySelector('.btn-5');
  setTimeout(() => {
    
    redButton.classList.add('slide-from-right');
    redButton.classList.add('active');

  }, 700);
  

 
});
// category = document.querySelector('#massazh');
// console.log(category)
// let observer = new MutationObserver(function(mutations) {
//   mutations.forEach(function(mutationRecord) {
//       console.log('mutationRecord');
//   });    
// });




// observer.observe(category, { childList : true, subtree : true, attributes : true});