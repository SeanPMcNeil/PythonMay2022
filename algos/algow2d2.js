/* 
    Given a string,
    return a new string with the duplicates excluded
    Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

/**
 * De-dupes the given string.
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    var strTable = {};
    for (var char of str){
        if (!strTable[char]){
            strTable[char] = 1;
        }
    }
    var dedupeStr = "";
    for (var key in strTable){
        dedupeStr += key;
    }
    return dedupeStr;
}

// Instructor Solution
// function stringDedupe(str) {
//     let distinctStr = "";
//     const seen = {};

//     for (let i = 0; i <= str.length - 1; i++){
//         if (!seen[str[i]]){
//             distinctStr += str[i];
//             seen[str[i]] = true;
//         }
//     }
//     return distinctStr;
// }

var answer1 = stringDedupe(str2);
console.log(answer1);

/*******************************/

/* 
    Given a string containing space separated words
    Reverse each word in the string.
    If you need to, use .split to start, then try to do it without.
*/

const str5 = "hello";
const expected5 = "olleh";

const str6 = "hello world";
const expected6 = "olleh dlrow";

const str7 = "abc def ghi";
const expected7 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */

function reverseWords(str) {
    var strArr = str.split(" ");
    var answer = "";
    var counter = 0;
    for (var string of strArr){
        for (var z = string.length-1; z >= 0; z--){
            answer += string[z]
        }
        counter++;
        if (counter < strArr.length){
            answer += " ";
        }
    }
    return answer;
}

// Instructor Solution
// function reverseWords(str){
//     const words = str.split(" ");
//     let wordsReversed = "";

//     for (const word of words){
//         let reversedWord = "";

//         for (let i = word.length - 1; i >= 0; i--){
//             reversedWord += word[i];
//         }

//         if (wordsReversed.length > 0){
//             reversedWord = " " + reversedWord;
//         }
//         wordsReversed += reversedWord;
//     }
//     return wordsReversed;
// }

var answer2 = reverseWords(str7);
console.log(answer2);

/***********************************/

/* 
    Reverse Word Order
    Given a string of words (with spaces)
    return a new string with words in reverse sequence.
*/

const str8 = "This is a test";
const expected8 = "test a is This";

const str9 = "hello";
const expected9 = "hello";

const str10 = "   This  is a   test  ";
const expected10 = "test a is This";

/**
 * Reverses the order of the words but not the words themselves form the given
 * string of space separated words.
 * @param {string} wordsStr A string containing space separated words.
 * @returns {string} The given string with the word order reversed but the words
 *    themselves are not reversed.
 */
function reverseWordOrder(wordsStr) {
    var strArr = wordsStr.split(/ +/);
    var answer = "";
    var counter = 0;
    for (var i = strArr.length - 1; i >= 0; i--){
        answer += strArr[i];
        if (strArr[counter] != "" && counter < strArr.length){
            answer += " ";
        }
        counter++;
    }
    var string = answer.split(/ $/);
    return string[0];
}

// Instructor Solution
// function reverseWordOrder(wordsStr){
//     if (wordsStr == false){
//         return wordsStr;
//     }

//     const words = wordsStr.split(" ");
//     let reversedWordOrder = "";

//     for (let i = words.length - 1; i >= 0; i--){
//         if (words[i] === ""){
//             continue;
//         }

//         if (reversedWordOrder.length > 0){
//             reversedWordOrder += " ";
//         }

//         reversedWordOrder += words[i];
//     }
//     return reversedWordOrder
// }

var answer3 = reverseWordOrder(str10);
console.log(answer3)