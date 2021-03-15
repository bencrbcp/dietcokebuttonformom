var contextClass = (window.AudioContext || window.webkitAudioContext || window.mozAudioContext || window.oAudioContext || window.msAudioContext);
var dance = document.getElementById("everybodydance");
if (contextClass) {
  var context = new contextClass();
} else {
  onError;
}

function onError() { console.log("Bad browser! No Web Audio API for you"); }

function unpress() { dance.classList.remove("pressed"); }

// function post() {

//     // The rest of this code assumes you are not using a library.
//     // It can be made less wordy if you use one.
//     const form = document.createElement('form');
//     form.method = 'post';
//     form.action = '/submit';

//     document.body.appendChild(form);
//     form.submit();
// }

function playSound() {
 dance.classList.add("pressed");
  var audio = new Audio('../static/swoosh.mp3');
  audio.play();
  var delay = 500;
  setTimeout(unpress,delay);
  // setTimeout(post, 1000)
}

dance.addEventListener('click', function(event) { playSound(); })