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

// This function clear all the values
function clearScreen() {
    document.getElementById("result").value = "";
}

// This function display values
function display(value) {
    document.getElementById("result").value += value;
}

// This function display values
function addblack() {
    var compute = 0;
    console.log(compute++);
    document.getElementById("black_display").value = count;
}