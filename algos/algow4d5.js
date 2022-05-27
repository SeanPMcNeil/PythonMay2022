/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/
// Non-working
// function binaryStringExpansion(str, l = 0, r = str.length, workingArr = []) {
//     var workingStr = "";
//     // console.log(str);
//     if (str[l] == "?") {
//         str[l] = "1";
//     }
//     workingArr.push(str[0])
//     console.log(workingArr)
//     var newStr = str.slice(l + 1, r);
//     return binaryStringExpansion(newStr)
// }

// Solution

function binaryStringExpansion(str, solutions = [], partial = ""){
    const index = str.indexOf("?");

    if (index < 0) {
        solutions.push(partial + str);
    } else {
        const front = str.slice(0, index);
        const back = str.slice(index + 1);
        const prefix = partial + front;

        binaryStringExpansion(back, solutions, prefix + "0");
        binaryStringExpansion(back, solutions, prefix + "1");
    }
    return solutions;
}

console.log(binaryStringExpansion("1?0?"))
// ['1000', '1100', '1001', '1101']