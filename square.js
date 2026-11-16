// Tests the square function by calling it with several different arguments.
function start() {
    square(5);     // 25
    square(0);     // 0
    square(-3);    // 9
    square(10);    // 100
    square(2.5);   // 6.25
}

// Takes in a number x, squares it (multiplies it by itself),
// and prints the result.
function square(x) {
    var result = x * x;
    println(result);
}
