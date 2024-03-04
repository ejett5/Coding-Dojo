let state = "some value"
const useState = [
    //Array index 0; A Getter Function
    function () {
        console.log(state)
        return state
    },
    //Array index 1; A Setter Function
    function (newStateValue) {
        console.log("new value: " + newStateValue)
        state = newStateValue
        return state
    }
];

// deep copy using the spread operator
const animal = {
    type: "bird"
}
const animalCopy = { ...animal }  // the {} are what define the deep copy object rather than just being an array[] of the original in a new variable name
animalCopy.type = "turtle"
console.log("Original: " + animal.type, "The Copy: " + animalCopy.type)

