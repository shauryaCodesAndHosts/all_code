'use strict'


/*
let a = 0;
function logger() {
    console.log("i am shaurya  " + a++);
}

logger();
logger();
logger();
logger();


function calcAge(birthYear) {
    return 2023 - birthYear;
}


//this is an expression and we assign the value to the variable
const calcAgeVar = function (birthYear) {
    return 2023 - birthYear;
}

console.log(calcAge(2002), calcAgeVar(2002))

// we can call function definition anywhere in the code ,
// even before the daclaration but we can only call expression,
// after they have been declared



// arrow functions
const age = birthYear => 2023 - birthYear;
console.log(age(2002));



const retireInfo = (nameVar, birthYear) => {
    const age = 2023 - birthYear;
    const timeToRetire = 65 - age;
    console.log(`the time to retire is ${timeToRetire} and name is ${nameVar} and age is ${age}`)
}
retireInfo("shaurya", 2002)

function checkWinner(av1, av2) {
    if (av1 > av2 * 2)
        console.log(`koala is the winner`);
    if (av2 > av1 * 2)
        console.log(`dolphin is the winner`);
    else
        console.log(`nobody wins`)
}

const calcAverage = (s1, s2, s3) => (s1 + s2 + s3) / 3;

const avKoala = calcAverage(44, 23, 71);
const avDolphin = calcAverage(65, 54, 49);

checkWinner(avKoala, avDolphin);




// arrays

const friend1 = "shaurya";
const friend2 = "vansh";
const friend3 = "sidd";

const friends = [friend1, friend2, friend3, "sarthak", "saksham"];

console.log(friends);

//another way

const newFriends = new Array(friend1, friend2, 7, friends);
console.log(newFriends);

newFriends.push("naya dost");
newFriends.unshift("purana dost baadme yaad aaya");
newFriends.pop();
newFriends.shift();
console.log(newFriends.indexOf(7));
console.log(newFriends.includes(7));


console.log(newFriends);

const tipCalc = (bill) => {
    if (bill > 50 && bill < 300) {
        return bill * 0.15;
    }
    else
        return bill * 0.2;
}

const final = [125 + tipCalc(125), 555 + tipCalc(555), 44 + tipCalc(44)]

console.log(final);


// object jus tlike dictionary (key value pairs )
// keys is also called property 

const shaurya = {
    firstName: "Shaurya",
    lastName: "Yamdagni",
    age: 21,
    job: "berozgar",
    friends: ["loneliness", "movies", "anxiety"],


    calcBirthyear: function (age) {
        return 2023 - age;
    },

    calcBirthyearTHIS: function () {
        return 2023 - this.age;
    }
}

console.log(shaurya.calcBirthyear(shaurya.age));
console.log(shaurya.calcBirthyearTHIS())


console.log(shaurya);
console.log(shaurya.lastName);
console.log(shaurya["lastName"]);

console.log(`${shaurya.firstName} has ${shaurya.friends.length} friends and ${shaurya.friends[0]} is his best friend`);
*/

/*
const calcBmi = (mass, height) => mass / (height * 2);

const mark = {
    namee: "Mark",
    height: 1.69,
    weight: 78,
    calcBmi: ()
}


const john = {
    namee: "John",
    height: 1.95,
    weight: 92
}


const shaurya = {
    firstName: "Shaurya",
    lastName: "Yamdagni",
    age: 21,
    job: "berozgar",
    friends: ["loneliness", "movies", "anxiety"],

    calcBirthyearTHIS: function () {
        return 2023 - this.age;
    },

    calcBirthyear: function () {
        this.yearOfBirth = 2023 - this.age;
    }

};
shaurya.calcBirthyear();


console.log(shaurya.yearOfBirth);


const calcBmi = (mass, height) => mass / (height * 2);

const mark = {
    namee: "Mark",
    height: 1.69,
    weight: 78,
    calcBmi: function () {
        this.bmi = this.weight / (this.height * 2);
        return this.bmi;
    }
}


const john = {
    namee: "John",
    height: 1.95,
    weight: 92,
    calcBmi: function () {
        this.bmi = this.weight / (this.height ** 2);
        return this.bmi;
    }
}

mark.calcBmi(); john.calcBmi();
console.log(`${mark.bmi > john.bm1 ? mark.namee : john.namee}'s bmi is higher`);


for (let i = 0; i <= 10; i++) {
    console.log(`bhaiii ${i}`);
}

*/

const tipCalc = (bill) => {
    if (bill > 50 && bill < 300) {
        return bill * 0.15;
    }
    else
        return bill * 0.2;
}

function calcAverage(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum = sum + arr[i];
    }
    return sum / arr.length;
}

const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];

const tips = [], totals = [];
for (let i = 0; i < bills.length; i++) {
    tips.push(tipCalc(bills[i]));
    totals.push(tips[i] + bills[i]);
}

console.log(tips)
console.log(bills)
console.log(totals)

console.log(calcAverage(totals));



