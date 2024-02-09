/* 
    Zip Arrays into Map
    
    Given two arrays, create an associative array (aka hash map, an obj / dictionary) 
    containing keys from the first array, and values from the second.

    Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};
console.log("abc" in expected1);
const keys2 = [];
const vals2 = [];
const expected2 = {};

/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys, values) {
    // Fun Tip: You can check if a key exists in something with: console.log("abc" in expected1);


}
// obj = {};
// obj[key] = value;

/*****************************************************************************/


/* 
    Invert Hash
 
    A hash table / hash map is an obj / dictionary
 
    Given an object / dict,
    return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj_1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected_1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, any>} obj
 * @return The given object with key value pairs inverted.
 */
function invertObj(obj) {
    // Hint: we can use Object.entries(obj) similar to how we use .items() in Python. 
    // MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
    var answer = []
for(const [key,value] of Object.entries(obj)){
    answer[value] = key
    

}
console.table(answer)  //a way to view the data in a more visual way
return answer
}
console.table(obj_1)
invertObj(obj_1)

/*****************************************************************************/