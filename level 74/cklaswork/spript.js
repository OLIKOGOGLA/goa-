let clock = document.getElementById("count");
let btn =document.getElementById("btn")
let time = 10;
let myTimer ;

btn.addEventListener("click" , () => {
    time= 10 ;
    clock.textContent=time;
    time=time-1
})

// add your code below! start with: let myTimer = 
  myTimer = setInterval(time,200) 

function countdown () {
    if (time < 0){
      clearInterval(myTimer);
  } // add else's code here
  else{
    clock.textContent=time;
    time=time-1
  }
  }