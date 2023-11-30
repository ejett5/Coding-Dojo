//making variable for a loop to keep track of distance to know if we are within range of a reward
var mileRun = 4.0;
var runSpeed = 5.4;
    if (mileRun >=2 && mileRun <= 6){  //start and end point to track distance range, any distance outside this range is not rewarded
        console.log("here is your reward!");
            }else if(runSpeed >= 5.5, mileRun +2){  //end of loop as condition is not met on either end of range
        console.log("Keep up the great work!");
    }else 
        {console.log(mileRun)}
    /*
    The loop checks for the conditions of distance ran and if below 2 but greater than 6 will not need to run the code
    the iteration increment is from the source such as a treadmill to track distance, could be set to only track whole numbers ideally.
    */