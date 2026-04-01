const cards = document.querySelectorAll(".contact-card");

cards.forEach(card=>{
    card.addEventListener("mouseenter", ()=>{
        card.style.boxShadow="0 0 30px #0f9d58,0 0 50px #ffd700"; // green + gold magical glow
    });
    card.addEventListener("mouseleave", ()=>{
        card.style.boxShadow="";
    });
});