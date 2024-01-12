/* 
  Zip Arrays into Map
  
  
  Given two arrays, create an associative array (aka hash map, an obj / dictionary) containing keys from the first array, and values from the second.

  Associative arrays are sometimes called maps because a key (string) maps to a value 
 */

const keys1 = ["abc", 3, "yo"];
const vals1 = [42, "wassup", true];
const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
};

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
    // const array = [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']];
    function zipArraysIntoMap(keys, values) {
        const dictionary = {};

        for (let i = 0; i < keys.length; i++) {
            dictionary[keys[i]] = values[i];
        }

        return dictionary;
    }

    console.log(zipArraysIntoMap(keys1, vals1));
    console.log(zipArraysIntoMap(keys2, vals2));

    //     var keysArray = keys.split(",")
    //     //looping through first array and making index as key; store in temp dicitonary
    //     for (i = 0; i <= keys.length; i++) {
    //         // keys[i] = keys

    //         console.log(keysArray)
    //         // keys = key
    //         // console.log(keys)
    //         //loop second and make value;store in emptyy dictionary
    //         // for (j = 0; j <= values.length; i++) {
    //         //     var valuesArray = value.split(",")
    //         //     // values[j] = values
    //         //     // values = value
    //         //     // console.log(values)
    //         // }
    //         //make  combined dictionary
    //         // dicitonary = {[keysArray[i], valuesArray[j]]}

    //     }
    //     // return dicitonary
    //     // console.log(dicitonary)   
}

// // const array = [[keys, values]]
// console.log(zipArraysIntoMap(keys1, vals1))
/*****************************************************************************/