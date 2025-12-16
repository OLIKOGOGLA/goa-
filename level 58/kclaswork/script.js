function showInput() {
  const inputValue = document.getElementById("myInput").value;
  console.log("შეყვანილი ტექსტი:", inputValue);
  document.getElementById("outputParagraph").innerText = inputValue;
}

function interact() {
  const name = prompt("შეიყვანე შენი სახელი:");
  alert("მოგესალმებით, " + name + "!");

  const age = prompt("შეიყვანე შენი ასაკი:");
  if (age >= 18) {
    alert("თქვენ სრულწლოვანი ხართ.");
  } else {
    alert("თქვენ არასრულწლოვანი ხართ.");
  }

  const confirmed = confirm("გსურს გაგრძელება?");
  console.log("confirm()-ის პასუხი:", confirmed);
}

function checkGender() {
  const isMale = document.getElementById("male").checked;
  console.log("მონიშნულია male?:", isMale);
  document.getElementById("genderResult").innerText = "Male მონიშვნა არის: " + isMale;
}
