function interleaveArrays(arrayA, arrayB) {
    var newArr = [];
    var i = 0;

    for (var i = 0; i < arrayA.length || i < arrayB.length; i++){
        if (i < arrayA.length){
            newArr.push(arrayA[i]);
        }
        if (i < arrayB.length){
            newArr.push(arrayB[i]);
        }
    }

    // while (i < arrayA.length || i < arrayB.length){
    //     if (i < arrayA.length){
    //         newArr.push(arrayA[i]);
    //     }
    //     if (i < arrayB.length){
    //         newArr.push(arrayB[i]);
    //     }
    //     i++;
    // }

    return newArr;
}

// Instructor Solution

// if (arrayA.length > arrayB.length){
//     var longerArrLength = arrayA.length;
// } else {
//     var longerArrLength = arrayB.length;
// }

// for (var i = 0; i < longerArrLength; i++){...}