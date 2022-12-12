// var, let, const
// var is OLD way

let x = 0;
x = 1;
x = "apple"

const dontReassignMe = "banana"

// dontReassignMe = "cucumber"

const constList = []

// constList = "something else"
// constList = []

constList.push("new stuff")

const constObj = {foo:'bar'}

constObj.foo == 'baz';


for(let i = 0; i < 5; i++) {
    let innerVar = "apple";
    console.log(innerVar)
}

// console.log(innerVar);

innerVar = "banana";

console.log(innerVar);


function oldSchool(a,b) {
    console.log(this)
}

oldSchool();

// contextual this here applies inside arrow function
const newSchool = (a,b) => console.log(this);

newSchool();




