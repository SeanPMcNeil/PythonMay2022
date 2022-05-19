function bookIndex(pages) {
    var strArr = [];
    var str = "";
    var seqStart;

    for (var i = 0; i < pages.length; i++) {
        seqStart = pages[i]
        var seqEnd = undefined;

        for (var j = i + 1; j < pages.length; j++) {
            if (pages[j] == pages[j - 1] + 1) {
                seqEnd = pages[j];
                if (j == pages.length - 1) {
                    i = j;
                    break;
                }
            } else if (seqEnd == undefined) {
                i = j - 1;
                break;
            } else {
                i = j - 1;
                break;
            }
        }
        if (seqEnd != undefined) {
            strArr.push(seqStart + '-' + seqEnd)
        } else {
            strArr.push('' + seqStart)
            // strArr.push(seqStart.toString())
        }
    }
    for (var k = 0; k < strArr.length; k++) {
        if (k == strArr.length - 1) {
            str += strArr[k]
        } else {
            str += strArr[k] + ", ";
        }
    }

    return str;

}

// Instructor Solution
// function bookIndex(pages){
//     var strArray = []

//     for (var i = 0; i < pages.length; i++){
//         var left = pages[i];
//         var right = pages[i];

//         while (pages[i] = pages[i+1]){
//             i++;
//             right = pages[i]
//         }

//         if (left == right){
//             strArray.push(left.toString());
//         } else {
//             strArray.push(left + "-" + right);
//             // strArray.push(`${left}-${right}`);
//         }
//     }
//     // return strArray.join(', ');
//     return buildIndexString(strArray)
// }

// function buildIndexString(strArray){
//     var output = '';

//     for (i in strArray){
//         output += strArray[i]
//         if (i != strArray.length - 1){
//             output += ', ';
//         }
//     }

//     return output;
// }
