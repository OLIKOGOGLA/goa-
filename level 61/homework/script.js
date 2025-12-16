function changeColor() {
  document.getElementById("p1").style.color = "blue";
}

function checkOddEven() {
  let num = Number(document.getElementById("numInput").value);
  if (num % 2 === 0) {
    console.log("ლუწი");
  } else {
    console.log("კენტი");
  }
}

function toggleParagraphs() {
  document.getElementById("para1").style.display = "none";
  document.getElementById("para2").style.display = "block";
}

function checkWord() {
  let word = document.getElementById("wordInput").value;
  if (word === "admin") {
    document.body.style.backgroundColor = "green";
  } else {
    document.body.style.backgroundColor = "red";
  }
}

function askName() {
  let name = prompt("შეიყვანეთ თქვენი სახელი");
  alert(name);
}

function greetAndAskAge() {
  alert("მოგესალმები!");
  let age = prompt("შეიყვანეთ თქვენი ასაკი");
  console.log("თქვენი ასაკია: " + age);
}
