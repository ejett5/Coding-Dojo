/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    // This can be a bit of a brain teaser. A Frequency table might come to mind, but this might not work for VALID parenthesis. (like str3)

    // Hint: You can attempt to use a "stack"-style data structure for this.
    // Using pop() and push() you can mimic a stack's ability to quickly add and remove values from the "top" of the array.

    const pStack = [];


    for (const char of str) {

        if (char === '(') {
            pStack.push(char);
        } else if (char === ')') {
            if (pStack.length === 0) {
                return false;
            } else {
                pStack.pop();
            }
        }

    }
    // Return true if the stack is empty, false if it has a orphaned opening parenthesis!
    return pStack.length === 0;

}


console.log(parensValid(str1), "should equal", expected1);
console.log(parensValid(str2), "should equal", expected2);
console.log(parensValid(str3), "should equal", expected3);
console.log(parensValid(str4), "should equal", expected4);

/*****************************************************************************/


/* 
Braces Valid

Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str5 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected5 = true;

const str6 = "D(i{a}l[ t]o)n{e";
const expected6 = false;

const str7 = "A(1)s[O (n]0{t) 0}k";
const expected7 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {

    const stack = [];
    const opens = "({[";
    const closes = {
        ")": "(",
        "}": "{",
        "]": "["
    };


}

console.log(parensValid(str5), "should equal", expected5);
console.log(parensValid(str6), "should equal", expected6);
console.log(parensValid(str7), "should equal", expected7);

/*****************************************************************************/