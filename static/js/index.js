import "./static/css/index.css"
function scrollToSection(id){

document.getElementById(id).scrollIntoView({
behavior:"smooth"
})

}



document.getElementById("registerForm")
.addEventListener("submit",function(e){

e.preventDefault()

let email=document.getElementById("email").value
let message=document.getElementById("message")

if(!email.endsWith("@uap-bd.edu")){

message.innerText="Use your UAP email"
message.style.color="red"

return

}

message.innerText="Registration successful!"
message.style.color="lightgreen"

})



document.getElementById("ideaForm")
.addEventListener("submit",function(e){

e.preventDefault()

alert("Your magical idea has been sent!")

})



const eventDate=new Date("April 7, 2026 17:00:00").getTime()

setInterval(function(){

const now=new Date().getTime()

const diff=eventDate-now

let days=Math.floor(diff/(1000*60*60*24))

let hours=Math.floor((diff%(1000*60*60*24))/(1000*60*60))

let minutes=Math.floor((diff%(1000*60*60))/(1000*60))

let seconds=Math.floor((diff%(1000*60))/1000)

document.getElementById("countdown").innerHTML=

days+"d "+
hours+"h "+
minutes+"m "+
seconds+"s "

},1000)


const backgrounds = [
"static/images/image_01.jpeg",
"static/images/image_2.jpeg",
"static/images/image_3.jpeg",

];

let index = 0;

const hero = document.querySelector(".hero");

function changeBackground(){

index++;

if(index >= backgrounds.length){
index = 0;
}

hero.style.backgroundImage = `url(${backgrounds[index]})`;

}
    
setInterval(changeBackground, 7000);