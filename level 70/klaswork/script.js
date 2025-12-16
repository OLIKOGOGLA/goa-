function addParagraph() {
  let div = document.getElementById("content");
  let p = document.createElement("p");
  p.textContent = "This is a new paragraph!";
  div.appendChild(p);
}

let counter = 1;
function addItem() {
  let div = document.getElementById("list");
  let item = document.createElement("p");
  item.textContent = "Item " + counter++;
  div.appendChild(item);
}
function removeItem() {
  let div = document.getElementById("list");
  if (div.lastChild) {
    div.removeChild(div.lastChild);
  }
}

let photoCount = 1;
function addPhoto() {
  let gallery = document.getElementById("gallery");
  let img = document.createElement("img");
  img.src = "https://picsum.photos/200?random=" + photoCount++;
  img.alt = "Random Photo";
  img.width = 200;
  gallery.appendChild(img);
}
