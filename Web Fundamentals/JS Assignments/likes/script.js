// setting up counter for like button
function (likeCounter){
    let count = 0;
    let btn = document.getElementById("btn");
    let disp = document.getElementById("display");
    
    btn.addEventListener("click",function (likeCounter){
        count++;
        disp.innerHTML = count;
    });
}

