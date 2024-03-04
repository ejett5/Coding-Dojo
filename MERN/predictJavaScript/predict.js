// console.log("test")  // this is just here to verify it loaded and worked correctly

// // problem 1
// const cars = ['Tesla', 'Mercedes', 'Honda']
// const [randomCar] = cars
// const [, otherRandomCar] = cars
// //Predict the output
// console.log(randomCar)
// console.log(otherRandomCar)
// //This code should output: Honda, I think that because otherRandomCar is a variable that is being sought at an unknown index position but not beyond the last position but also not the first position, and is a way to try and assign that as that variable
// // all are the output because it was searching rather than attempting to assign a value to that variable, works on both variables, {did a shallow scope take place assigning to the new variable as a literal array?}

// // \problem 2
// const employee = {
//     employeeName: 'Elon',
//     age: 47,
//     company: 'Tesla'
// }
// const { employeeName: otherName } = employee;
// //Predict the output
// console.log(otherName);
// console.log(employeeName);
// // it appears that the literal array is having a new var be assigned to the property of name for employee. This will allow the name the be updated even though the const is used since this is a shallow 
// // Wrong I was as I missed that the employeeName is block and the employee is at the function level and is global so the employeeName is not accessible to the Global



// // problem 3
// const person = {
//     name: 'Phil Smith',
//     age: 47,
//     height: '6 feet'
// }
// const password = '12345';
// const { password: hashedPassword } = person;
// //Predict the output
// console.log(password);
// console.log(hashedPassword);
// // adding a password to the literal array under hashedPassword and allow future updates under this name 
// // also returned the undefined property as the state was not given - I missed this in analysis

// // problem 4
// const numbers = [8, 2, 3, 5, 6, 1, 67, 12, 2];
// const [,first] = numbers;
// const [,,,second] = numbers;
// const [,,,,,,,,third] = numbers;
// //Predict the output
// console.log(first === second);
// console.log(first === third);
// // it appears they are trying to find values at the  2,4 and 9 indices while assigning those values to the variables first, second and third. If successful then: 2,5,2 should be displayed
// //  false and true are returned but I cannot explain why

// // problem 5
// const lastTest = {
//     key: 'value',
//     secondKey: [1, 5, 1, 8, 3, 3]
// }
// const { key } = lastTest;
// const { secondKey } = lastTest;
// const [ ,willThisWork] = secondKey;
// //Predict the output
// console.log(key);
// console.log(secondKey);
// console.log(secondKey[0]);
// console.log(willThisWork);
// // should return all values as expected. just a simple console.log working with their respective scopes and not trying to reach to the scope below itself
// console.log(secondKey[5]);

// // problem 6
// var beatles = ['Paul', 'George', 'John', 'Ringo'];
// function printNames(names) {
//     function actuallyPrintingNames() {
//         for (var index = 0; index < names.length; index++) {
//             var name = names[index];
//             console.log(name + ' was found at index ' + index);
//         }
//         console.log('name and index after loop is ' + name + ':' + index);
//     }
//     actuallyPrintingNames();
// }
// printNames(beatles);
// there are 4 scopes, global beatles -> function printNames -> another function actuallyPrintingNames -> then the innner for loop which is the inner most scope and can see all the above scopes and read their data but is hidden to the others

// problem 7
function actuallyPrintingNames() {
    for (let index = 0; index < names.length; index++) {
        let name = names[index];
        console.log(name + ' was found at index ' + index);
    }
    console.log('name and index after loop is ' + name + ':' + index);
}
// there is no global variable called names for the inner for loop to reference and use to call therefore it should produce an undefined result, if not a syntax error as it goes to call just index asd a variable
//Actual result => Empty which is a type of undefined.
