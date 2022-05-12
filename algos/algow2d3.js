/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expect1 = true;

const str2 = "N(0(p)3";
const expect2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expect3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expect4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    var countOpen = 0;
    var countClose = 0;

    for (var char of str){
        if (char == "("){
            countOpen++;
            console.log("Opening: " + countOpen);
        } else if (char == ")"){
            countClose++;
            console.log("Closing: " + countClose);
        }
        if (countClose > countOpen){
            return false;
        }
    }
    if (countOpen == countClose){
        return true;
    } else {
        return false;
    }
}

// Instructor Solutions
// #1 - Counting

// function parensValid(str){
//     var counter = 0;

//     for (var i = 0; i < str.length; i++){
//         if (str[i] == '('){
//             counter++;
//         } else if (str[i] == ')'){
//             counter--;
//         }
//         if (counter < 0){
//             return false;
//         }
//     }
//     return counter > 0 ? false : true;
// }

// #2 - Matching Pairs

// function parensValid(str){
//     var checkParens = [];

//     for (var i = 0; i < str.length; i++){
//         if (str[i] === "("){
//             checkParens.push(str[i]);
//         } else if (str[i] === ")" && checkParens[checkParens.length - 1] === "("){
//             checkParens.pop();
//         } else if (str[i] === ")"){
//             return false;
//         }
//     }
//     return checkParens.length > 0 ? false : true;
// }

console.log(parensValid(str1));
console.log(parensValid(str2));
console.log(parensValid(str3));
console.log(parensValid(str4));

/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1a = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2a = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3a = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    var openArr = [];

    for (var char of str){
        if (char == "(" || char == "[" || char == "{"){
            openArr.push(char);
        } else if (char == ")"){
            if (openArr[openArr.length - 1] == "("){
                openArr.pop();
            } else {
                return false;
            }
        } else if (char == "]"){
            if (openArr[openArr.length - 1] == "["){
                openArr.pop();
            } else {
                return false;
            }
        } else if (char == "}"){
            if (openArr[openArr.length - 1] == "{"){
                openArr.pop();
            } else {
                return false;
            }
        }
    }
    if (openArr.length > 0){
        return false;
    } else {
        return true;
    }
}

// Instructor Solution

// function bracesValid(str) {
//     var checker = [];

//     for (var i = 0; i < str.length; i++){
//         if (str[i] == "(" || str[i] == "[" || str[i] == "{"){
//             checker.push(str[i]);
//         } else if (str[i] == ")" && checker[checker.length - 1] == "("){
//             checker.pop();
//         } else if (str[i] == "]" && checker[checker.length - 1] == "["){
//             checker.pop();
//         } else if (str[i] == "}" && checker[checker.length - 1] == "{"){
//             checker.pop();
//         } else if (str[i] == ")" || str[i] == "]" || str[i] == "}"){
//             return false;
//         }
//     }
//     if (checker.length > 0){
//         return false;
//     } else {
//         return true;
//     }
// }

console.log(bracesValid(str1a));
console.log(bracesValid(str2a));
console.log(bracesValid(str3a));