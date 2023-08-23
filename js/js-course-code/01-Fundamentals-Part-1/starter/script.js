/*let js = "amazing";
//if (js === "amazing") alert("js is funnnn");
console.log("i am in console");
let firstName = "shaurya";
console.log(firstName);
console.log(typeof (firstName));
firstName = true;
console.log(typeof (firstName));

// undefined
let varr;
console.log(typeof varr);

// error (legacy)
console.log(typeof null); //should give undefined


let age = 30;
age = 31;

const dob = 12319

var name = "shaurya"
name = "sjsjsjsj"


let massMark = 78;
let massJohn = 92;
let heightMark = 1.69;
let heightJohn = 1.95;
let bmiMark = massMark / heightMark ** 2;
let bmiJohn = massJohn / heightJohn ** 2;
console.log(bmiJohn, bmiMark)
console.log(bmiMark > bmiJohn);


//template literal
const firstName = "shaurya";
const lastName = "yamdagni";
const temp_literal = `my first name is ${firstName}, i am a ${lastName}`;
console.log(temp_literal)


//multiline strings
console.log("string with \n\
many lines \n\
many many lines");

//multiline using back quotations
console.log(`string with
multiline
comments and data`);



//if else


let massMark = 78;
let massJohn = 92;
let heightMark = 1.69;
let heightJohn = 1.95;
let bmiMark = massMark / heightMark ** 2;
let bmiJohn = massJohn / heightJohn ** 2;
console.log(bmiJohn, bmiMark)
if (bmiMark > bmiJohn) {
    console.log(`mark bmi(${bmiMark}) is higher`);
}
else
    console.log(`john bmi ${bmiMark} is higher `);


    

// type conversion 
//string to numbers 

const year = "2002";
console.log(typeof Number(year), Number(year), year);
console.log(Number("shaurya"));
console.log(typeof NaN); //not a number


//number to string 

console.log(String(1233))

//cant do with boolean values cause they behave different

//type coercion 
console.log("i am " + 23 + " years new");
console.log('23' + 2);  // plus sign makes it a string 
console.log('23' - 2); //minus sign makes it a number 
console.log('23' * 3);  //makes it a number 



console.log(Boolean(0));
console.log(Boolean('0'));
console.log(Boolean(null));
console.log(Boolean(NaN));
console.log(Boolean(undefined));
console.log(Boolean({}));


console.log(10 == "10");
console.log(10 === "10");


const fav = Number(prompt("what is your fav"));
if (fav !== 0) console.log("Not 0 like your mental problems");
else console.log("0 like your bitches ");


// Boolean logic 
// And  Or  Not 
// &&   ||  !



const t1 = Number(prompt("enter the score"))
const t2 = Number(prompt("enter the score"))
const t3 = Number(prompt("enter the score"))


const s1 = Number(prompt("enter the score"))
const s2 = Number(prompt("enter the score"))
const s3 = Number(prompt("enter the score"))

const averageDol = (t1 + t2 + t3) / 3;
const averageKol = (s1 + s2 + s3) / 3;

if (averageS > averageT) {
    if (s1 > 100 || s2 > 100 || s3 > 100)
        console.log("team Koala is the winner");
}
else if (averageT > averageS) {
    if (t1 > 100 || t2 > 100 || t3 > 100)
        console.log("team Dolphin is the winner");
}
else {
    if (s1 > 100 || s2 > 100 || s3 > 100)
        if (t1 > 100 || t2 > 100 || t3 > 100)
            console.log("its a fuckiung draw");
}
*/

const bill = Number(prompt("enter the value"));
console.log(`the tip is ${bill > 50 && bill < 300 ? 0.15 * bill : 0.2 * bill} and your bill is ${bill > 50 && bill < 300 ? bill + 0.15 * bill : bill + 0.2 * bill}`)




