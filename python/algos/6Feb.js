/* 

Acronyms

Crate a function that, given a string, returns the string's acronym (first letter of each word capitalized).

Do it with .split() first if you need to, then try to do it without

*/

const str1 = 'object oriented programming';
// const myArray = text.split(" ");
// console.log(myArray)

// const expected1 = 'OOP';

// The 4 pillars of OOP

const str2 = 'abstraction polymorphism inheritance encapsulation';
// const expected2 = "APIE";

const str3 = 'software development life cycle';

// const expected3 = 'SDLC';

//BONUS: ignore extra spaces

const str4 = 'global information tracker';
// const expected4 = "GIT";

// Turns the given str into an acronym.Turns
// Time : 0(?) n(0)
// Space: 0(?) n(0)

// @param {String} str A string to be turned into an acroynm
// @returns {String} The Acroynm

function acronymize(str) {
    // Step 1: trim the input string to remove any extra spaces at the start and the end - .trim()

    // Step 2: Initialize a variable to hold the acronym, initially empty
    var tempstr = "";
    // Step 3: Split the input into an array of words - .split()
    var wordArray = str.split(" ") //.split is a C++ function that is abstracted in JS and the functionality takes place behind the scenes
    // console.log(wordArray)
    // Step 4: Loop through each word in the array
    //   Step 4.1: Check if the current word is not an empty string
    //   Step 4.2: Take the first character of the word, convert it to uppercase, and add it to the acroynm
    for (var i = 0; i < wordArray.length; i++) {
        // console.log(wordArray[i][0].toUpperCase())
        tempstr += wordArray[i][0].toUpperCase()   //takes holding var and tell to go through var wordArray and take the index 0 of each array we created
    };

    //Step 5: Return the constructed acroynm
    return tempstr
}

const result1 = acronymize(str1);
console.log(result1);

const result2 = acronymize(str2);
console.log(result2);

const result3 = acronymize(str3);
console.log(result3)

const result4 = acronymize(str4);
console.log(result4)


// solving without using split method
function noneSplit(str) {
    //starting the count loop
    for (var i = 0; i < str.length; i++)

        // look for empty space 
        var placeHolder = []
    if (i == 0 && str[i+1 != ' ']) {
        placeHolder +=  str[0];
    } //TODO figure out why line 81 has an expected expression when an expression is given after.
    else if (str[i] == && str[i + 1] != ' ' && i < str.length -1) {
        placeHolder = + str[i + 1]
    };

    // return (!str || str.length ===0);  // way to show if there is an empty space in the string but does not display the value



}
console.log(noneSplit(str1))
console.log(noneSplit(str2))
console.log(noneSplit(str3))
console.log(noneSplit(str4))