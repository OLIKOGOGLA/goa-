// // შექმენით პატარა მონაცემთა ბაზა, სადაც შეინახავთ მომხმარებლის შემოტანილ მნიშვნელობებს
// . მაგ: name: levani, last_name: samsonidze... და შემდეგ გამოიტანეთ ეს console.log() JS

console.log(user);

const users = {
    first_name: '',
    last_name: '',
    age:'',
    grade:'',
};

users.first_name = prompt('Enter your name:');
users.last_name = prompt('Enter your lastname:');
users.age = prompt("Enter your age:");
users.grade = prompt("Enter your grade:");

console.log(users);