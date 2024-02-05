/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @returns {boolean} If the strings are equal or not.

 */
function caseInsensitiveStringCompare(strA, strB) {
    // your code here
    if(strA.toLowerCase() === strB.toLowerCase()){
        return True
        // console.log(expected())
    }else
        return false
    // console.log(expected())

    // ✨ Hint: There is a built-in function with JS to convert cases in strings.
}
console.log(expected1)
console.log(expected2)
console.log(expected3)

/*****************************************************************************/

/* 
    String: Reverse
    Given a string,
    return a new string that is the given string reversed
*/

const str4 = "creature";
const expected4 = "erutaerc";

const str5 = "dog";
const expected5 = "god";

const str6 = "hello";
const expected6 = "olleh";

const str7 = "";
const expected7 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    //your code here
    //✨ try to do it with and without built-in methods
    let empty = []
    for(let i = 0; i < str.length ; i++){
        let loop = str[i];
        
        empty.push(loop);
        // console.log(loop)

        // newstr = str[i]
        // str[i] =newstr
        // return newstr
    }
    return empty
    console.log()

    //✨ try to do it looping forwards only!



    // done with built in methods
    // var splitString = str.split("");  //makes explicit array for string
    // console.log(splitString)

    // var reverseArray = splitString.reverse();  //creates array with each character as an index
    // console.log(reverseArray)

    // var joinArray = reverseArray.join(""); //puts array back together as single string
    // console.log(joinArray)
    // if (str === joinArray) // checks if the two strings are equivalent 
    // {
    //     return true
    // }
    // else {
    //     return false
    // }
}

//TEST CODE FOR REVERSE
console.log(reverseString(str4)) // Expected: erutaerc
console.log(reverseString(str5)) // Expected: god
console.log(reverseString(str6)) // Expected: olleh
console.log(reverseString(str7)) // Expected: ""