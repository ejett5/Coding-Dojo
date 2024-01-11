/* 
String: Is Palindrome

Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards

Do not ignore spaces, punctuation and capitalization
 */

const str1 = "a x a";
const expected1 = true;

const str2 = "racecar";
const expected2 = true;

const str3 = "Dud";
const expected3 = false;

const str4 = "oho!";
const expected4 = false;

/**
 * Determines if the given str is a palindrome (same forwards and backwards).
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given str is a palindrome or not.
 */
function isPalindrome(str) {
    // for (var i=0; i<str.length; i++){}
    var splitString = str.split("");  //makes explicit array for string
    console.log(splitString)

    var reverseArray = splitString.reverse();  //creates array with each character as an index
    console.log(reverseArray)

    var joinArray = reverseArray.join(""); //puts array back together as single string
    console.log(joinArray)
    if (str === joinArray) // checks if the two strings are equivalent 
    {
        return true
    }
    else {
        return false
    }
    // return joinArray == str
}



// console.log(isPalindrome)
console.log(isPalindrome(str3))
// console.log(str3)
// console.log(isPalindrome)