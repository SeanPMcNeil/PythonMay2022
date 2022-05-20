// Your input is an array of N integers that, if ordered, would form a sequence with one value missing. Return that missing value. For example, the array [2, 1, 0, 4], if ordered, would be [0, 1, 2, 4] - the integer missing from the sequence is 3, which is what you would return. The sequence of integers can include negative numbers as well; given the array [2, -3. -2, 0, 3, 1], the missing integer is -1.

function findMissingValue(input) {

    var lowest = input[0];
    var highest = input[0];
    var sum1 = 0;

    for (var i = 0; i < input.length; i++) {
        if (input[i] < lowest) {
            lowest = input[i];
        } else if (input[i] > highest) {
            highest = input[i];
        }
        sum1 += input[i]
    }


    var sum2 = 0;
    for (var k = lowest; k <= highest; k++) {
        sum2 += k;
    }

    return sum2 - sum1;
}

