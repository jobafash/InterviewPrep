function checkIfEmailInString(text) {
  var re = /(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))/;
  return re.test(text);
}

var test = "The email is 12@unilag.u";

//alert(checkIfEmailInString(test))

var StrObj = "whatever, this is my 12@unilag.edu.ng email jobafash3@gmail.c other text";
var emailsArray = StrObj.match(/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+)/gi);
//console.log(emailsArray);

var str = " some text https://loopdeloop.ng aussie bi-monthly animation challenge site."
var tt = new RegExp("([a-zA-Z0-9]+://)?([a-zA-Z0-9_]+:[a-zA-Z0-9_]+@)?([a-zA-Z0-9.-]+\\.[A-Za-z]{2,4})(:[0-9]+)?(/.*)?")

var urlRE = new RegExp("([a-zA-Z0-9]+://)?([a-zA-Z0-9_]+:[a-zA-Z0-9_]+@)?([a-zA-Z0-9.-]+\\.[A-Za-z]{2,4})(:[0-9]+)?([^ ])+");
const arr = str.match(tt)
console.log(arr);

const arr = str.match(/\d{8}/);
console.log(arr);


var data = [42, 21, undefined, 50, 40, undefined, 9];

data = data.filter(function (element) {
  return element !== undefined;
});

console.log(data);






////////////////////////////////////
account_type: { type: String, enum: ['single', 'organization'], default: 'single' }
role: { type: String, enum: ['admin', 'user'], default: 'user' }