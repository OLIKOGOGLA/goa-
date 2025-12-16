1
    const btn1 = document.getElementById('btn1');

    function showNumber() {
      console.log(5);
    }

    btn1.addEventListener('click', showNumber);

    
    setTimeout(() => {
      btn1.removeEventListener('click', showNumber);
      console.log("Listener წაიშალა");
    }, 3000);


    // 2
    const img = document.getElementById('photo');
    const btn2 = document.getElementById('btn2');

    btn2.addEventListener('pointerdown', function() {
      img.src = "c3e9f8af5aa29e528ba769fa66bf3825.jpg";
    });


    //  3 
    const btn3 = document.getElementById('btn3');

    btn3.addEventListener('mousedown', function() {
      console.log("Clicked! Don't let go!");
    });

    btn3.addEventListener('mouseup', function() {
      console.log("you lost!");
    });