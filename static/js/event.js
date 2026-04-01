// You can add magical owl animations on load
const cards = document.querySelectorAll(".event-card");

cards.forEach(card=>{
    card.addEventListener("mouseenter", ()=>{
        // small sparkle effect
        card.style.boxShadow = "0 0 30px gold, 0 0 50px orange";
    })
    card.addEventListener("mouseleave", ()=>{
        card.style.boxShadow = "";
    })
});