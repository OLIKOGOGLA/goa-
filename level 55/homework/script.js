function mathOperations() {
  let a = 10;
  let b = 5;

  console.log("მიმატება:", a + b);
  console.log("გამოკლება:", a - b);
  console.log("გამრავლება:", a * b);
  console.log("გაყოფა:", a / b);
}


mathOperations();


function changeButton() {
  let btn = document.getElementById("myBtn");

  btn.style.color = "white";
  btn.style.backgroundColor = "blue";   
  btn.style.borderRadius = "20px";      
  btn.style.width = "200px";            
}
