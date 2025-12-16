//1) შექმენით person ობიექტი, რომელსაც ექნება 6 კუთვნილება: name, surname, age, academy, hobby, sports
let person ={
    name: "mari"
    surname: "ADMIN"
    age:"15"
    academy: "goa"
    hobby: "Dance"
    sports: "Volleyball "
}
//2) შექმენით h1, p, button შემდეგ js-ში წამოიღეთ document.GetElementById-ის საშვალებით, თითოეული შეინახეთ ცვლადში და გამოიტანეთ კონსოლში
//დანარჩენებსაც მიწერეთ რომ შემოვიდნენ
let goa =document.GetElementById("goa")
let orientid=document.GetElementById('orientid')
let academi =document.GetElementById('academi')

console.log(goa)
console.log(orientid)
console.log(academi)
//3) შექმენით HTML-ის დოკუმენტი და დაამატეთ 2 პარაგრაფი, პირველ პარაგრაფს მიანიჭეთ უნიკალური id, 
// შემდეგ კი გახსენით script element-ი და წამოიღეთ კონკრეტული ელემენტი id-ის დახმარებით,
//  შეცვალეთ წამოღებული ელემენტის ვიზუალური მხარე, მაგალითად შიგთავსი და ფერი

let level=document.GetElementById('level')
level.style.color= "red"
let level61=document.GetElementById('61')
level61.style.color= "green"
//იმფუთით მომხმარებელს შემოატანინეთ ორი რიცხვი და დიდს გამოაკელით პატარა
let number1 = NUMBER(prompt("შეიყვანეთ პირველი რიცხვი:"));
let number2 = NUMBER(prompt("შეიყვანეთ მეორე რიცხვი:"));


if (number1 > number2) {
    alert(number1-number2)
} 
else if (number2 > number1){
    alert(number2-number1)
}
else {
    alert('0')
}

let difference = maxNum - minNum;


