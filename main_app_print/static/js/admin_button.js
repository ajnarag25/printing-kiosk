// button of adding and subtracting for black & white

let addButton_black = document.getElementById("addButton_black");
let numberDisplay_black = document.getElementById("black_display");
let number_black = numberDisplay_black.value;
let minusButton_black = document.getElementById("minusButton_black");

addButton_black.addEventListener("click", function () {
    number_black++;
    numberDisplay_black.value = number_black;
});
minusButton_black.addEventListener("click", function () {
    number_black--;
    numberDisplay_black.value = number_black;
});

// button of adding and subtracting for colored
let addButton_colored = document.getElementById("addButton_colored");
let numberDisplay_colored = document.getElementById("colored_display");
let number_colored = numberDisplay_colored.value;
let minusButton_colored = document.getElementById("minusButton_colored");

addButton_colored.addEventListener("click", function () {
    number_colored++;
    numberDisplay_colored.value = number_colored;
});
minusButton_colored.addEventListener("click", function () {
    number_colored--;
    numberDisplay_colored.value = number_colored;
});

// button of adding and subtracting for time
let addButton_time = document.getElementById("addTime");
let numberDisplay_time = document.getElementById("time_display");
let number_time = numberDisplay_time.value;
let minusButton_time = document.getElementById("minusTime");

addButton_time.addEventListener("click", function () {
    number_time++;
    numberDisplay_time.value = number_time;
});
minusButton_time.addEventListener("click", function () {
    number_time--;
    numberDisplay_time.value = number_time;
});
