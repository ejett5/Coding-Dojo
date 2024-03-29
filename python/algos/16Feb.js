/* 
    Given a string that may have extra spaces at the start and the end,
    return a new string that has the extra spaces at the start and the end trimmed (removed)
    do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    // 💭 Note: Empty spaces can be resolved as 'falsey'.
    // if empty space after end then remove
    // console.log(str1.trim())

    // Remember strings are immutable! 
}
console.log(str1.trim())
/*****************************************************************************/

/* 
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Is there a quick way to determine if they aren't an anagram before spending more time?

    Given two strings
    return whether or not they are anagrams
*/

const strA1 = "yes";
const strB1 = "eys";
const expected2 = true;

const strA2 = "yes";
const strB2 = "eYs";
const expected3 = true;

const strA3 = "no";
const strB3 = "noo";
const expected4 = false;

const strA4 = "silent";
const strB4 = "listen";
const expected5 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    // We'll want to account for letter casing.
    if (strA == strB){
        console.log(true)
    }else{
        console.log(false)
    }
    // Also tracking letters/counts of letters sounds familiar. Maybe we did an algo related to this recently? 🤔
}
console.log()
console.log()
console.log()
console.log()
/*****************************************************************************/