/*
    Recursive Binary Search
    Input: SORTED array of ints, int value
    Output: bool representing if value is found
    Recursively search to find if the value exists, do not loop over every element.
    Approach:
    Take the middle item and compare it to the given value.
    Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5.5, 6, 8, 12, 32, 45, 47, 49, 50, 53];
const searchNum2 = 5.5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

const nums4 = [3];
const searchNum4 = 3;
const expected4 = true;

const nums5 = [];
const searchNum5 = 3;
const expected5 = false;

const nums6 = [8];
const searchNum6 = 3;
const expected6 = false;
/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */

function binarySearch(sortedNums, searchNum) {
    if (sortedNums.length == 0){
        return false;
    } else if (sortedNums.length == 1 && sortedNums[0] != searchNum){
        return false;
    } else if (sortedNums.length == 1 && sortedNums[0] == searchNum){
        return true;
    }

    var halfway = Math.floor(sortedNums.length / 2);

    if (sortedNums[halfway] == searchNum){
        return true;
    } else if (sortedNums[halfway] > searchNum){
        return binarySearch(sortedNums.slice(0, halfway), searchNum);
    } else if (sortedNums[halfway] < searchNum){
        return binarySearch(sortedNums.slice(halfway), searchNum);
    }
}

// Instructor Solution

function binarySearch2(sortedNums, searchNum, l = 0, r = sortedNumsNums.length){
    if (sortedNums.length < 1){
        // return false;
        // return a number if you're looking for the index over true/false
        return -1;
    }

    // as long as our indices are at least 2 elements apart, continue recursion
    if (r - 1 > 1) {
        // declare midpoint
        var mid = Math.floor((r + l) / 2);

        if (sortedNums[mid] == searchNum) {
            // return true;
            // to return index:
            return mid;
        }
        if (searchNum < sortedNums[mid]) {
            return binarySearch2(sortedNums, searchNum, l, mid);
        }

        return binarySearch2(sortedNums, searchNum, mid + 1, r);
    }

    // return sortedNums[l] == searchNum ? true : false;
    // returns the index if true or -1 if false
    return sortedNums[l] == searchNum ? l : -1;
}

// console.log(binarySearch(nums1, searchNum1));
// console.log(binarySearch(nums2, searchNum2));
// console.log(binarySearch(nums3, searchNum3));
// console.log(binarySearch(nums4, searchNum4));
// console.log(binarySearch(nums5, searchNum5));
// console.log(binarySearch(nums6, searchNum6));