function changeTitle() {
      document.title = "სათაური შეიცვალა!";
      alert("სათაური წარმატებით შეიცვალა!");
}

    
const a = true;
const b = false;
const andResult = a && b;
const orResult = a || b;

document.getElementById("logic-output").innerText =
`true && false = ${andResult}\ntrue || false = ${orResult}`;


let num = 42;
let str = "123";
let bool = true;

const asString = String(num);
const asNumber = Number(str);
const boolToNum = Number(bool); 

 document.getElementById("conversion-output").innerText =
`Number → String: "${asString}"\nString → Number: ${asNumber}\nBoolean → Number: ${boolToNum}`;

    
    function checkCheckbox() {
      const isChecked = document.getElementById("myCheckbox").checked;
      console.log("Checkbox მონიშვნა:", isChecked);
      alert(`Checkbox არის მონიშნული? ${isChecked}`);
    }