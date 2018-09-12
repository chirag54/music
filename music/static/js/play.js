
//  select  audio 
var audio = document.getElementById('audio1');
list.onclick = function(e) {
  e.preventDefault();

  var elm = e.target;
  // var audio = document.getElementById("audio1");

  var source = document.getElementById('audioSource');
  
  source.src = elm.getAttribute('data-value');

  audio.load(); //call this to just preload the audio without playing
  audio.play(); //call this to play the song right away
  $("#play").hide();
  $("#pause").show();
};


// play and push audio

function playVid() {

    audio.play();
    $("#play").hide();
    $("#pause").show();

} 
function refresh() { 

    document.getElementById("audio1").load();
    $("#play").show();
    $("#pause").hide();

} 

function pauseVid() { 
    audio.pause(); 
    $("#play").show();
    $("#pause").hide();
} 


// next privouse 

var $first = $('tr:first', 'table'),
    $last = $('tr:last', 'table');
$("#next").click(function () {
    var $next, $selected = $(".selected");


    $next = $selected.next('tr').length ? $selected.next('tr') : $first;
    $selected.removeClass("selected");
    $next.addClass('selected');
});

$("#prev").click(function () {
    var $prev, $selected = $(".selected");

    $prev = $selected.prev('tr').length ? $selected.prev('tr') : $last;
    $selected.removeClass("selected");
    $prev.addClass('selected');
});

// alert(document.getElementById("list").getElementsByTagName("a").length);


