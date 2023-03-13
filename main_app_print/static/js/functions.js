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


