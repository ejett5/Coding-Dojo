/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/

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

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) { 

// make variable to hold the str in the checked index
var dict = {}

// initialise for loop to iterate through index
for (i=0; i <= arr.length; i++){

// count how many times that str appears in other indexes
if (dict[ele])

// output the number of times it appears

// go up an index position and resume loop for counting
}


}

// function anotherSolution(arr){
//     var sample = 0
//     for (i=0; i<arr.length; i++){
//         if(arr[i] == i)
//         sample++
//     }
// }

/*****************************************************************************/