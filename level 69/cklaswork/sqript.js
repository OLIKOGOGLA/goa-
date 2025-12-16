let images = [
    "003aa081b30621854e84dc719c08e5a2.jpg",
    "24c4043113d7f365b62dbc38e2196ec3.jpg"
  ];
  
  let index = 0;
  let scale = 1;
  let rounded = false;
  
  const imgEl = document.getElementById("1");
  const prevBtn = document.getElementById("4");
  const nextBtn = document.getElementById("5");
  const zoomInBtn = document.getElementById("zoomIn");
  const zoomOutBtn = document.getElementById("zoomOut");
  const roundBtn = document.getElementById("round");
  const resetBtn = document.getElementById("reset");
  
  function showImage() {
    imgEl.src = images[index];
    imgEl.style.transform = `scale(${scale})`;
    imgEl.style.borderRadius = rounded ? "20px" : "0px";
  }
  

  prevBtn.onclick = function() {
    index = (index - 1 + images.length) % images.length;
    showImage();
  };
  nextBtn.onclick = function() {
    index = (index + 1) % images.length;
    showImage();
  };
  

  zoomInBtn.onclick = function() {
    scale = Math.min(3, scale + 0.2);
    showImage();
  };
  zoomOutBtn.onclick = function() {
    scale = Math.max(0.4, scale - 0.2);
    showImage();
  };
  

  roundBtn.onclick = function() {
    rounded = !rounded;
    showImage();
  };
  

  resetBtn.onclick = function() {
    scale = 1;
    rounded = false;
    showImage();
  };
  

  showImage();
  