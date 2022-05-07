// Bubble Sort
function bubbleSort(arr) {
    // var temp;
    for (var x = 0; x < arr.length; x++){
        for (var y = 0; y < arr.length - x; y++){
            if (arr[y] > arr[y+1]){
                let temp = arr[y];
                arr[y] = arr[y+1];
                arr[y+1] = temp;
            }
        }
    }
}

var x = [1, 6, 8, 9, 23, 3, 6, 9];
console.log(`Before sort: ${x}`);
bubbleSort(x);
console.log(`After sort: ${x}`);

x = [37, 2, 901, 42, 56, 11, 1, 546];
console.log(`Before sort: ${x}`);
bubbleSort(x);
console.log(`After sort: ${x}`);

x = [Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1), Math.floor(Math.random() * 100 + 1)]
console.log(`Before sort: ${x}`);
bubbleSort(x);
console.log(`After sort: ${x}`)