function arrayBalanceIndex(arr){
    if (arr.length < 3) {
        return -1;
    }
    for (var index = 1; index < arr.length-1; index++){
        var sumLeft = 0;
        var sumRight = 0;
        for (var left = 0; left < index; left++){
            sumLeft += arr[left];
        }
        for (var right = index+1; right < arr.length; right++){
            sumRight += arr[right];
        }
        if (sumLeft == sumRight){
            return index;
        }
    }
    return -1;
    // Write your solution here!
}