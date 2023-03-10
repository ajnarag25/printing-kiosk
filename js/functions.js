$(document).ready(function() {
    $("#show_hide_password a").on('click', function(event) {
        event.preventDefault();
        var open = document.getElementById("open_eye");
        var close = document.getElementById("closed_eye");
        if($('#show_hide_password input').attr("type") == "text"){
            $('#show_hide_password input').attr('type', 'password');
            close.style.display = "block";
            open.style.display = "none";
        }else if($('#show_hide_password input').attr("type") == "password"){
            $('#show_hide_password input').attr('type', 'text');
            close.style.display = "none";
            open.style.display = "block";
        }
    });
});

// this function clear all the values
function clearScreen() {
    document.getElementById("result").value = "";
}

// this function display values
function display(value) {
    document.getElementById("result").value += value;
}

// button of adding and subtracting for black & white
let number_black = 0;
let addButton_black = document.getElementById("addButton_black");
let numberDisplay_black = document.getElementById("black_display");
let minusButton_black = document.getElementById("minusButton_black");

addButton_black.addEventListener("click", function() {
    number_black++;
    numberDisplay_black.value = number_black;
});
minusButton_black.addEventListener("click", function() {
    number_black--;
    numberDisplay_black.value = number_black;
});

// button of adding and subtracting for colored
let number_colored = 0;
let addButton_colored = document.getElementById("addButton_colored");
let numberDisplay_colored = document.getElementById("colored_display");
let minusButton_colored = document.getElementById("minusButton_colored");

addButton_colored.addEventListener("click", function() {
    number_colored++;
    numberDisplay_colored.value = number_colored;
});
minusButton_colored.addEventListener("click", function() {
    number_colored--;
    numberDisplay_colored.value = number_colored;
});

// button of adding and subtracting for time
let number_time = 0;
let addButton_time = document.getElementById("addTime");
let numberDisplay_time = document.getElementById("time_display");
let minusButton_time = document.getElementById("minusTime");

addButton_time.addEventListener("click", function() {
    number_time++;
    numberDisplay_time.value = number_time;
});
minusButton_time.addEventListener("click", function() {
    number_time--;
    numberDisplay_time.value = number_time;
});


// image button
$("#upload-img").click(function () {
    $("#uploadfile").click();
});

// current time
window.onload = displayClock();
function displayClock() {
  var display = new Date().toLocaleTimeString();
  $("#LiveTime").text(display);
  setTimeout(displayClock, 1000);
}

// redirect if there is a file uploaded
const fileInput = document.getElementById("uploadfile");
fileInput.addEventListener("change", function() {
    if (fileInput.value) {
        document.getElementById("upload-form").submit();
    }
});
