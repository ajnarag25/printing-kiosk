$(document).ready(function () {
    $("#show_hide_password_1 a").on('click', function (event) {
        event.preventDefault();
        var open = document.getElementById("open_eye1");
        var close = document.getElementById("closed_eye1");
        if ($('#show_hide_password_1 input').attr("type") == "text") {
            $('#show_hide_password_1 input').attr('type', 'password');
            close.style.display = "block";
            open.style.display = "none";
        } else if ($('#show_hide_password_1 input').attr("type") == "password") {
            $('#show_hide_password_1 input').attr('type', 'text');
            close.style.display = "none";
            open.style.display = "block";
        }
    });
    $("#show_hide_password_2 a").on('click', function (event) {
        event.preventDefault();
        var open = document.getElementById("open_eye2");
        var close = document.getElementById("closed_eye2");
        if ($('#show_hide_password_2 input').attr("type") == "text") {
            $('#show_hide_password_2 input').attr('type', 'password');
            close.style.display = "block";
            open.style.display = "none";
        } else if ($('#show_hide_password_2 input').attr("type") == "password") {
            $('#show_hide_password_2 input').attr('type', 'text');
            close.style.display = "none";
            open.style.display = "block";
        }
    });
    $("#show_hide_password_3 a").on('click', function (event) {
        event.preventDefault();
        var open = document.getElementById("open_eye3");
        var close = document.getElementById("closed_eye3");
        if ($('#show_hide_password_3 input').attr("type") == "text") {
            $('#show_hide_password_3 input').attr('type', 'password');
            close.style.display = "block";
            open.style.display = "none";
        } else if ($('#show_hide_password_3 input').attr("type") == "password") {
            $('#show_hide_password_3 input').attr('type', 'text');
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
fileInput.addEventListener("change", function () {
    if (fileInput.value) {
        document.getElementById("upload-form").submit();
    }
});


