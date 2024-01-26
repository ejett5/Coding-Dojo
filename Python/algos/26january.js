// import Math
/* 
Given an int to represent how much change is needed
calculate the fewest number of coins needed to create that change,
using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

dict = [
    penny = 1,
    nickel = 5,
    dime = 10,
    quarter = 25
]

function fewestCoinChange(cents) {
    // compare the value of what is given and divide that from biggest and find any remainder
    while(cents >= 0, i++){
        cents = cents / dict
        return change
    } 
    console.log(change)

    // if no remainder then output the number of quarters

    // Can this be a check for the biggest whole number evenly divisible?

    // return the amount that is needed to 
}
console.log(change)
console.log(change)
console.log(change)
console.log(change)

/*****************************************************************************/