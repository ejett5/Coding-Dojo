
/*
var produceList = ["apples", "oranges", "jalapenos"];
//Array 2
var accountBalances = [5000, 10, 2500];
//Array 3
//arrays are zero indexed collections of elements
//                    0          1            2               3            4      5
var auntsContact = ["Jayne", "Smithe", "123 Main Street", "Springfield", "MO", 12345];

//get count for auntsContact
console.log(auntsContact.length)
//use subscript syntax to access or reassign individual elements
console.log(auntsContact[4])
auntsContact[1] = 'Doe'

//adding and removing from arrays
// pop and push both operate at the end of the array
//push adds
accountBalances.push(1000000)

//pop will return the element it removes
var tooSpicy = produceList.pop()
console.log(tooSpicy)

function jamesFunction(){
    var x = 5
    x = x*25
    console.log(x)
    return "Apple sauce"
}

var storedResult = jamesFunction()


//practicing rounding
num1 = 7.2
num2 = 7.2
num3 = 9.2

console.log(Math.floor(num1))
console.log(Math.floor(num3))
console.log("\n")

console.log(Math.ceil(num2))
console.log(Math.ceil(num3))
console.log("\n")

console.log(Math.round(num3))
//trunc goes to ceil if a negative but floor if a positive
console.log(Math.trunc(num3))


//loops
for(
    
    var i=0; //this line initializes the loop and declare any variables if necessary; urns once at the beginning
    
    i<10; //expression the checks to keep loop active; checked at start of each iteration;
    
    i++){ //final statement; runs at the end of each iteration
    console.log(i)
}


var num = 0
//increase num by one methods
num++ 
num = num+1 
num += 1


//methods to find even numbers
for (var i=0; i<=10; i+=2){
    console.log(i)
    
}

console.log('\n')
//using modulo to only show even; if put to 3 will show odds
for (var i=0; i<=10; i++){
    if( i % 2 == 0){
        console.log(i)
    }
}

console.log('\n')
//using modulo if put to 3 will show odds
for (var i=0; i<=10; i++){
    if( i % 3 == 0){
        console.log(i)
    }
}
*/
/*
var x = []
x[0]="hello";
x[1]= "world";
x[2] = 100;
console.log(x.length + ' '+x[0]);*/
/*
var x = 2;
var points = [40,100,1,5,25,10];
if(points[x] == 1){
    console.log(points[x-2]);
}else{
    console.log('hello');
}*/

/*// the position in y arrary is given from stated x var and from there it is figuring out based upon those positions their sum
var x=2;
var y = [1,2,3,4,5];
var z = [6,7,8,9,10];

if (y[x] +z[1] == z[4]){
    console.log('Dojo');
}else{
    console.log("Hello world");
}*/
/*
var x = 'boom';
var y = ['hi','hello','hey'];

if(x.length ==3){
    y.push(x);
    console.log(x[3]);
}else{
    console.log(x);
}

var x =['John','Chris', 'Mark','PJ'];

if(x.length == 4){
    console.log(x[x.length -3 ]);
}else{
    console.log('Dojo');
}


function countDown(start, stop){
    if (start > stop){
    var temp = start;
    start = stop;
    stop= temp;
}
for (var i= start; i <stop; i++){
    console.log(i)
}
}

countDown(1,10)
*

function countUp(start,stop){
    var countArray = []
    if(start>stop){
        var temp = start;
        start= stop;
        stop= temp;
    }
    for (var i = start; i <stop; i++){
        countArray.push(i)
    }
    return countArray
}
var result = countUp(7,45)
console.log(result)

//break keyword: used to stop a loop

var length = 99999;
for(var i=0; i<length;i++){
    if(i>10){
        break;
    }
    console.log("hello");
}


var x = 10, y = 20;
function abc(x,y){
    x = x+10;
    y= y+10;
        return x*10;
}

z = abc(x,y) + abc(y,x);
console.log(z);


var x = [1,3,5,7];

function abc(){
    var x = [0,1,2,3];
    for(var i=0; i<x.length; i++){
        x[i] = x[i] + 2;
    }
    return x;
}

x =abc();
console.log(x)
*/

function abc(number){
    var sum = 0;
    for(var i=0; i<number; i++){
        sum = sum + i;
        }
        console.log(sum);
        return sum+10;
}

output = abc(2);
console.log(output);


//vs git and  github plus bash notes
/*
git = version control system, locally done on the local drive
git -v to check version 
git bash terminal is Linux based and usese same commands for all systems
git works in snapshots when a file is saved = only worries about what is new
fetch is for pulling from github and is especially useful in collaborative work; commits are done in two stages with the push followeed by commit.
new files not uploaded are indicated by U; 

*/