/*
  Input: a 2 dimensional array of integers
  Output: A 1 dimensional array of all the same elements preserving original order
*/

// this given array has a length of 3 because it has 3 arrays as items
const twoDimArr1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];
const expected1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const twoDimArr2 = [[1], [2], [3]];
const expected2 = [1, 2, 3];

const twoDimArr3 = [[], [], [10, 20]];
const expected3 = [10, 20];

/**
 * Flattens a two dimensional array into a new one dimensional array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<Array<any>>} twoDimArr An array of arrays of any data type.
 * @returns {Array<any>} The flattened array that should be one dimensional.
 */
function flatten2dArray(twoDimArr) {
    // code here

    var bigBoy = []
    //as long as there is something in the array put it in a new array
    for(let i = 0; i < twoDimArr.length; i++){
        if(twoDimArr1[i].length > 0){            
            bigBoy.push;
            }

        //this is another idea to look into other loops to then look into others and remove them as individual arrays
        for(let j=0;j<twoDimArr.j; j++){
                bigBoy.push(items[i])
            }
        
        }
        //push new array with all the contents of the other arrays
    return(bigBoy)

}

console.log(flatten2dArray(twoDimArr1))