/* 
    Given an array of integers
    return the first integer from the array that is not repeated anywhere else
    If there are multiple non-repeated integers in the array,
    the "first" one will be the one with the lowest index.
*/

const nums1 = [3, 5, 4, 3, 4, 6, 5];
const expected1 = 6;

const nums2 = [3, 5, 5];
const expected2 = 3;

const nums3 = [3, 3, 5];
const expected3 = 5;

const nums4 = [5];
const expected4 = 5;

const nums5 = [];
const expected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {
    if (nums.length  < 1){
        return null
    }

    var freqTable = {};
    for (var num of nums){
        if (!freqTable[num]){
            freqTable[num] = 1;
        } else {
            freqTable[num]++;
        }
    }

    for (var num of nums){
        if (freqTable[num] == 1){
            return num
        }
    }

    return null
}

// Instructor Solution

function firstNonRepeated(nums){
    
}

console.log(firstNonRepeated(nums1))
console.log(firstNonRepeated(nums2))
console.log(firstNonRepeated(nums3))
console.log(firstNonRepeated(nums4))
console.log(firstNonRepeated(nums5))