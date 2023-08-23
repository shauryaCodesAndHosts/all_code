'use strict';
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelectorAll('.show-modal');

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

const openModal = function () {
  modal.classList.remove('hidden'); //Dont use dot here
  //we can also use this :
  //modal.style.display = 'block';
  overlay.classList.remove('hidden'); //to make overlay visible
};

/// this loop will just add the event listner to the each button
for (let i = 0; i < btnOpenModal.length; i++) {
  btnOpenModal[i].addEventListener('click', openModal);
}

btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

// for adding close functionality using keyboard
document.addEventListener('keydown', function (e) {
  // e can be anything it just get the object of the keypress
  console.log(e.key);
  if (e.key === 'Escape') if (!modal.classList.contains('hidden')) closeModal();
});
