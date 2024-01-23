/* 
  Balance Index

  Here, a balance point is ON an index, not between indices.

  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3]; // index position has to be excluded to make the left and right equal each other with a value of 3
const expected1 = 2;

const nums2 = [9, 9]; //neither can equal when one position is omitted as there is no value to compare to
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
function balanceIndex(nums) {


}



/*****************************************************************************/
// example for reference
// const balancedIndex = (array) => {
//     let total = array.reduce((a, b) => a + b);
//     for (let i = 0; i < array.length; i++) {
//         // subtract the total with the current value of array[i]
//         total = total - array[i];
//     }
//     // if there is no balanced index, return -1
//     return -1;
// };
// balancedIndex([1, 2, 5, 3]);
// console.log(balancedIndex)