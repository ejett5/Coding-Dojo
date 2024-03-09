// let state = "some value"
// const useState = [
//     //Array index 0; A Getter Function
//     function () {
//         console.log(state)
//         return state
//     },
//     //Array index 1; A Setter Function
//     function (newStateValue) {
//         console.log("new value: " + newStateValue)
//         state = newStateValue
//         return state
//     }
// ];

// // deep copy using the spread operator
// const animal = {
//     type: "bird"
// }
// const animalCopy = { ...animal }  // the {} are what define the deep copy object rather than just being an array[] of the original in a new variable name
// animalCopy.type = "turtle"
// console.log("Original: " + animal.type, "The Copy: " + animalCopy.type)

// const obj = {
//     name: "John",
//     es5Method: function () {
//         console.log(obj.name)
//     }
// };
// const newObj = {...obj, name: "Bob"}  //Just calling the already existing function values without assigning a new value at a deep level => just a shallow copy
// //Logs the newObj object's properties
// console.log(newObj)
// //Executes the inherited es5Method on the newObj
// newObj.es5Method()


let a = 4
let b = 19
let c = 21
let d = []
let e = []
let f = []

puzzleA = (c-d+1)/4

puzzleB = a*(e/2)-1
puzzleC = f*9(a-1)-(sqrt(a)+1)
puzzleD = a*a-e
puzzleE = a+d
puzzleF = (c-b) * (e-d)

console.log(puzzleA)
console.log(puzzleB)
console.log(puzzleC)
console.log(puzzleD)
console.log(puzzleE)
console.log(puzzleF)