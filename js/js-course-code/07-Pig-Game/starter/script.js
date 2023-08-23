'use strict';

const score0El = document.querySelector('#score--0');
const score1El = document.getElementById('score--1');

const currentScore0El = document.getElementById('current--0');
const currentScore1El = document.getElementById('current--1');

const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');
const btnNewGame = document.querySelector('.btn--new');

const diceEl = document.querySelector('.dice');

let currentScore = 0;
let totalScore = 0;
let activePlayer = 0;
const arr = [0, 0];
let state = true;

//init condition
score0El.textContent = score1El.textContent = 0;
diceEl.classList.add('hidden');

function switchPlayer() {
  currentScore = 0;
  if (activePlayer === 1) {
    document.querySelector('.player--1').classList.remove('player--active');
    document.querySelector('.player--0').classList.add('player--active');
    document.getElementById(`current--${activePlayer}`).textContent = 0;
    activePlayer = 0;
  } else {
    document.querySelector('.player--0').classList.remove('player--active');
    document.querySelector('.player--1').classList.add('player--active');
    document.getElementById(`current--${activePlayer}`).textContent = 0;
    activePlayer = 1;
  }
}
// rolling the dice
btnRoll.addEventListener('click', function () {
  // genrate random number
  if (state) {
    const diceRand = Math.trunc(Math.random() * 6) + 1;
    //const diceRand = 6;
    console.log(diceRand);
    //display dice
    if (diceEl.classList.contains('hidden')) {
      diceEl.classList.remove('hidden');
    }
    diceEl.src = `./img/dice-${diceRand}.png`;

    //check for 1
    if (diceRand == 1) {
      //switch

      // we can also use toggle method(if present then remove, if not there then add )
      //document.querySelector('.player--1').classList.toggle('player--active');
      //document.querySelector('.player--2').classList.toggle('player--active');
      switchPlayer();
    } else {
      currentScore = currentScore + diceRand;
      document.getElementById(`current--${activePlayer}`).textContent =
        currentScore;
    }
  }
});

btnHold.addEventListener('click', function () {
  if (state) {
    document.getElementById(`current--${activePlayer}`).textContent = 0;
    arr[activePlayer] += currentScore;
    document.getElementById(`score--${activePlayer}`).textContent =
      arr[activePlayer];

    if (arr[activePlayer] >= 100) {
      state = false;
      console.log(`${activePlayer} won the game !!`);
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.add('player--winner');

      document
        .querySelector(`.player--${activePlayer}`)
        .classList.remove('player--active');

      diceEl.classList.add('hidden');
    } else {
      switchPlayer();
    }
  }
});

btnNewGame.addEventListener('click', function () {
  state = true;
  currentScore = 0;
  arr[0] = arr[1] = 0;
  currentScore0El.textContent = 0;
  currentScore1El.textContent = 0;
  score0El.textContent = 0;
  score1El.textContent = 0;
  activePlayer = 0;
  document.querySelector(`.player--0`).classList.remove('player--winner');
  document.querySelector(`.player--1`).classList.remove('player--winner');
  document
    .querySelector(`.player--${activePlayer}`)
    .classList.add('player--active');
});
