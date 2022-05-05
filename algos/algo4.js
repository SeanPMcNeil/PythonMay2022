// /**
//  * @param arr is a list<int>
//  * @returns list<int>
//  */

// Group Solution

function selectionSort(arr) {
    for (var x = 0; x < arr.length; x ++){
    var biggestNumber = arr[0];
    var indexBigNumber = 0;
    for (var y = 0; y < arr.length - x; y++){
        if (arr[y] > biggestNumber){
            biggestNumber = arr[y];
            indexBigNumber = y;
        }
    }
    let temp = arr[arr.length - 1 - x]
    arr[arr.length - 1 - x] = biggestNumber;
    arr[indexBigNumber] = temp;
    }
    return arr;
}

// Instructor explanation

// for (var i = arr.length - 1; i >= 0; i--){

//     var maxNumber = arr[0];
//     var maxPosition = 0;
//     // can also just keep track of maxPosition because you can swap using that

//     for (var j = 0; j <= i; j++){
//         if (arr[j] > maxNumber){
//             maxNumber = arr[j];
//             maxPosition = j;
//         }
//     }

//     let temp = arr[i]
//     arr[i] = maxNumber;
//     arr[maxPosition] = temp;
// }


// Failed Attempts

// for (var j = 0; j < arr.length - 1 - j; j++){
//   for (var i = 0; i < arr.length - j; i++){
//     var big = arr[j];
//     if (arr[j] < arr[i]){
//       big = arr[i];
//     }    
//   }
//   arr[j] = arr[arr.length - 1 - j];
//   arr[arr.length - 1 - j] = big;
// }

// for (var j = i+1; j < arr.length - i; j++){
//   if (arr[i] < arr[j]){
//     let x = arr[arr.length - 1 - i];
//     arr[arr.length - 1 - i] = arr[j];
//     arr[j] = x;
//   }
// }
// Write your solution here!