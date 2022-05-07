// De-duplicate a Sorted Array

function deduplicateSortedArray(arr) {
    if (arr.length < 2){
        return arr;
    }

    var newArr = [];
    newArr.push(arr[0]);

    for (var i = 1; i < arr.length; i++){
        if (arr[i] != arr[i-1]){
            newArr.push(arr[i]);
        }
    }

    arr = newArr;
    return arr;

    // Alternative Method #1
    // for (var i = 0; i < arr.length; i++){
    //     var j = i+1;
    //     if (arr[i] == arr[j]){
    //         arr.splice(i,1);
    //         i--;
    //     }
    // }
    // return arr;

    // Alternative Method #2
    // var i = 0;
    // var j = 1;

    // while (j < arr.length){
    //     if (arr[j] != arr[i]){
    //     i++;
    //     arr[i] = arr[j]
    //     j++;
    //     } else {
    //     j++;
    //     }
    // }
    // arr.length = i + 1;
    // return arr;
}