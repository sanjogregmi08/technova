const name = document.getElementById('name')
const form = document.getElementById('form')
const errorElement = document.getElementById('nameerror')
var intonumber = parseInt(document.getElementById('name'))
const phnumber = document.getElementById('number')
const username = document.getElementById('username')
const email = document.getElementById('email')
const password = document.getElementById('password')
const confirmpassword = document.getElementById('confirmpassword')


form.addEventListener('submit' ,(e)  => {
    let messages =[]
    if( name.value =="" ){
        messages.push("**Name is required")
    }
    if(name.value.length<=5){
        messages.push("Full Name is too Short")
    }
    if(email.value.length>=30){
        messages.push("Email cannot be too long")
    }
    if(password.value.length<=6){
        messages.push("password must be longer than 6 ")
    }
    if(password.value.length >=20){
        messages.push("password must be less than 20 character")
    }
    if(password.value=='password'){
        messages.push("Password cannot be password")
    }

    if(messages.length >0){
        e.preventDefault()
       
        errorElement.innerHTML = messages.join(' , ' )
    }
})
$(window).on('load',function(){
    $(".loader").fadeOut(1000);
    $(".container").fadeIn(1000);
});
