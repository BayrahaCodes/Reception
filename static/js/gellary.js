// Add subtle sparkle effect on hover
const items = document.querySelectorAll(".gallery-item");

items.forEach(item=>{
    item.addEventListener("mouseenter", ()=>{
        item.style.boxShadow="0 0 30px gold,0 0 50px orange";
    })
    item.addEventListener("mouseleave", ()=>{
        item.style.boxShadow="";
    })
});