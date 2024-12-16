// Custom cursor logic
const cursor = document.querySelector(".custom-cursor");

document.addEventListener("mousemove", e => {
    cursor.style.left = `${e.clientX}px`;
    cursor.style.top = `${e.clientY}px`;
});

// Enlarge cursor when hovering over interactive elements
document.addEventListener("mouseover", e => {
    if (['A', 'BUTTON', 'INPUT', 'TEXTAREA'].includes(e.target.tagName)) {
        cursor.style.transform = "translate(-50%, -50%) scale(1.7)";
    } else {
        cursor.style.transform = "translate(-50%, -50%) scale(1)";
    }
});

// Booking services
function bookService(service) {
    alert(`You have booked the service: ${service}. We will contact you shortly!`);
}

// Contact form submission
document.getElementById("contact-form").addEventListener("submit", function(e) {
    e.preventDefault();
    alert("Thank you for reaching out! We will get back to you soon.");
    this.reset();
});
