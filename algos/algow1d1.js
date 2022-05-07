//function rotateArray(arr, shiftBy) {
//     var newArr = [];
//     for (var i = 0; i < arr.length; i++){
//         if (shiftBy > arr.length) {
//         if (arr.length - (shiftBy % arr.length) + i < arr.length){
//             newArr.push(arr[arr.length - (shiftBy % arr.length) + i]);
//         } else {
//             newArr.push(arr[i - (shiftBy % arr.length)]);
//         }
//         } else if (shiftBy > 0) {
//         if (arr.length - shiftBy + i < arr.length){
//             newArr.push(arr[arr.length - shiftBy + i]);
//         } else {
//             newArr.push(arr[i - shiftBy]);
//         }
//         } else if (shiftBy < 0) {
//         if (arr.length + shiftBy + i < arr.length){
//             newArr.push(arr[arr.length + shiftBy + i]);
//         } else {
//             newArr.push(arr[i + shiftBy]);
//         }
//         }
//     }
// return newArr;
//}

// function rotateArray(arr, shiftBy) {
//     // modify array given instead of creating a new array
//     var lastItem = arr[arr.length - 1];
//     for (var i = arr.length - 1; i >= 0; i--){
//         arr[i] = arr[i - 1];
//     }
//     arr[0] = lastItem;
//     return arr;
// }

// var result = rotateArray([1 ,2, 3, 4, 5], 1)
// console.log(result);

// function rotateArray(arr, shiftBy) {
//     // modify array given instead of creating a new array
//     for (var j = 0; j < shiftBy; j++){
//         var lastItem = arr[arr.length - 1];
//         for (var i = arr.length - 1; i >= 0; i--){
//             arr[i] = arr[i - 1];
//         }
//         arr[0] = lastItem;
//     }
//     return arr;
// }

// result = rotateArray([1 ,2, 3, 4, 5], 2);
// console.log(result);

// always better to have something that works than nothing that doesn't work
// better to have a solution (even imperfect) then to try to do it perfectly and have nothing

function rotateArray(arr, shiftBy){
    let newArr = [];
    if (shiftBy > arr.length) {
        shiftBy = shiftBy % arr.length; //some modification
    }
    for (var i = 0; i < arr.length; i++){
        newArr.push(arr[((arr.length + i - shiftBy) % arr.length)]);
    }
    arr.length = 0;
    arr = [... newArr];
    return arr;
}

var result = rotateArray([1 ,2, 3, 4, 5], 1)
console.log(result);

result = rotateArray([1 ,2, 3, 4, 5], 2);
console.log(result);

result = rotateArray([1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 13);
console.log(result);

result = rotateArray([1 ,2, 3, 4, 5], -2);
console.log(result);

result = rotateArray([1 ,2, 3, 4, 5], 16);
console.log(result);