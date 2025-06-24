let title = document.getElementById("title");
let paragraph = document.getElementById("paragraph");

title.style.color = "darkblue";
title.style.fontSize = "32px";
title.style.fontFamily = "Arial";

paragraph.style.color = "green";
paragraph.style.fontSize = "20px";
paragraph.style.fontFamily = "Georgia";

console.log("სათაური:", title);
console.log("პარაგრაფი:", paragraph);

// let – გამოიყენება ცვლადების განსასაზღვრად (მაგალითად: let name = "Ana"). მისი მნიშვნელობა შეიძლება შეიცვალოს.

// document – წარმოადგენს HTML დოკუმენტს, ანუ მთელ გვერდს. მისი მეშვეობით შეგვიძლია ელემენტებზე წვდომა, შექმნა და კონტროლი.

// DOM (Document Object Model) – ეს არის HTML-ის "სტრუქტურული რუკა", რომლის საშუალებითაც ვაკონტროლებთ ვებსაიტის ელემენტებს JavaScript-ით.

// getElementById – ფუნქცია, რომელიც პოულობს HTML ელემენტს მისი ID-ის მიხედვით. მაგ. document.getElementById("title") იპოვის <h1 id="title"> ელემენტს.

