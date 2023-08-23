'use strict';

/*

console.log(document.querySelector('.message').textContent);

document.querySelector('.message').textContent = 'started again';

document.querySelector('.number').textContent = 12;
document.querySelector('.score').textContent = 300;

//to set the value of the given textbox

document.querySelector('.guess').value = 69;




// Start the application

let secretNumber = Math.trunc(Math.random() * 20) + 1;
console.log(secretNumber);
let score = 20;
let highScore = 0;

function highScoreUpdate(score) {
  if (score > highScore) highScore = score;
}

document.querySelector('.check').addEventListener('click', function () {
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess + ' -> ' + typeof guess);
  if (guess == 0) {
    document.querySelector('.message').textContent = 'Number to daal lode';
  } else if (guess === secretNumber) {
    document.querySelector('.message').textContent = 'Sahi hai ';
    document.querySelector('.number').textContent = secretNumber;
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';
    highScoreUpdate(score);
    document.querySelector('.highscore').textContent = String(highScore);
  } else if (guess > secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'TOO HIGH ';
      score--;
      document.querySelector('.score').textContent = String(score);
    } else {
      document.querySelector('.message').textContent = 'You fucking loser';
      document.querySelector('.score').textContent = 0;
    }
  } else if (guess < secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'TOO LOW';
      score--;
      document.querySelector('.score').textContent = String(score);
    } else {
      document.querySelector('.message').textContent = 'You fucking loser';
      document.querySelector('.score').textContent = 0;
    }
  }
});

document.querySelector('.again').addEventListener('click', function () {
  document.querySelector('.message').textContent = 'Start guessing...';
  document.querySelector('.score').textContent = '20';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
  document.querySelector('.number').textContent = '?';
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  document.querySelector('.score').textContent = '20';
  score = 20;
  console.log(secretNumber);
});

*/
