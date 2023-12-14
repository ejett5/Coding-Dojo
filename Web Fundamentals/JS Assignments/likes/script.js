console.log("test script")


// setting up counter for like button
//naming the function
var button = document.getElementById("clicked")
    //count = 0;
//connecting to the button input
// function clicked() {
    
//     //after each click send to a display
//     count += 1
//     //display each click starting from 0 and tallying click of the button
//     button.innerText = "clicked" + count;
// };


//syntax according to language documentation and does not work
// element.addEventListener("clicked", likes);
// function likes(){
//     button = document.getElementById("clicked");
//     count ++;
//     button.innerText = likes + count
// }


function likes(selector){
   // var element = document.querySelector(selector)
    selector.innerText++;
}