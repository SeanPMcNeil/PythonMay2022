// // Given an array of strings
// // return the number of times each string occurs (a frequency / hash table)


const arr1 = ["a", "a", "a"];
const expected1 = {
    a: 3,
};

const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
};

// //  Builds a frequency table based on the given array.
// //  - Time: O(?).
// //  - Space: O(?).
// //  @param {Array<string>} arr
// //  @returns {Object<string, number>} A frequency table where the keys are items
// //     from the given arr and the values are the amnt of times that item occurs.

const arr3 = ["a", "b", "a", "c", "B", "c", "c", "d"];
var expected3 = {};

function makeFrequencyTable(arr) {
    var expected = {};
    for (var i = 0; i < arr.length; i++){
        if (expected[arr[i]] >= 1){
            expected[arr[i]] += 1;
        } else {
            expected[arr[i]] = 1;
        }
    }
    return expected;
}

// Instructor Solution
function makeFrequencyTable2(arr){
    var freqTable = {};
    for (var str of arr){
        // "of" pulls elements of an array
        // "str" points to the actual value of the element, not the index
        if (!freqTable[str]){
            freqTable[str] = 1;
        } else {
            freqTable[str]++;
        }
    }
    return freqTable;
}

expected3 = makeFrequencyTable(arr3);
console.log(expected3);

/*****************************************************************************/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expected4 = 1;

const nums2 = [5, 4, 5];
const expected5 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expected6 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expected7 = 1;

function oddOccurrencesInArray(nums) {
    var expectedObj = {};
    for (var i = 0; i < nums.length; i++){
        var count = 0;
        if (expectedObj[nums[i]] >= 1){
            count += 1;
        } else {
            expectedObj[nums[i]] = 1;
        }
        expectedObj[nums[i]] += count;
    }
    var expected;
    for (var j in expectedObj){
        // "in" pulls keys in an Object
        if ((expectedObj[j] % 2) != 0){
            expected = j;
        }
    }
    return expected;
}

console.log(oddOccurrencesInArray(nums1), "should equal", expected4);
console.log(oddOccurrencesInArray(nums2), "should equal", expected5);
console.log(oddOccurrencesInArray(nums3), "should equal", expected6);
console.log(oddOccurrencesInArray(nums4), "should equal", expected7);

/*****************************************************************************/