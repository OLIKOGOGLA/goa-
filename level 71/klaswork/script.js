// 1. ფუნქცია, რომელიც div-ში ამატებს p-ს
function addtext(){
   let div = document.getElementById("div");
   let p = document.createElement("p");
   let text = document.createTextNode("haloo nika!");
   p.appendChild(text);
   div.appendChild(p);
}

// 2. ფუნქცია, რომელიც h1-ს ღილაკით ჩაანაცვლებს
function replace(){
   let div1 = document.getElementById("div1");
   let h1 = document.getElementById("h1");
   let newBtn = document.createElement("button");
   newBtn.textContent = "ახალი ღილაკი";
   div1.replaceChild(newBtn, h1);
}

// 3. იგივე js-იდან listener-ებით
let allButtons = document.querySelectorAll("#buttons button");
allButtons[0].addEventListener("click", ()=>alert("Click from JS!"));
allButtons[1].addEventListener("mouseover", ()=>alert("MouseOver from JS!"));
allButtons[2].addEventListener("click", ()=>console.log("Console from JS!"));