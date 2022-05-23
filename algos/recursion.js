// recursion - calling a function inside itself

// non-recursive function
// sigma(n)
// returns sum of numbers from 1 to n
// 3 -> 3 + 2 + 1 = 6
// 4 -> 4 + 3 + 2 + 1 = 10

function sigma(n) {
    var sum = 0;
    var i = 0;

    while (i <= n) {
        sum += i;
        i++;
    }

    return sum;
}

//recursive version

function sigmaRecursive(n) {

    // console.log('called sigmaRecursion with an argument of ${n}');
    // establish a base case
    // base cases stop recursion
    if (n <= 0) {
        // console.log('base case reached');
        return 0;
    } 
    // otherwise perform recursive call
    else {
        var x = sigmaRecursive(n - 1);
        // console.log('completed function call to sigmaReursive with argument of ${n} and returning value');
        return n + x;
    }

}