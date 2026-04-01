console.log("register.js loaded");

const type = document.getElementById("type");
const batchField = document.getElementById("batchField");
const volunteerField = document.getElementById("volunteerField");
const paymentBox = document.getElementById("paymentBox");
const batch = document.getElementById("batch");
const form = document.getElementById("registerForm");

// Show/hide fields based on the selected type
if (type) {
  type.addEventListener("change", function () {
    batchField.classList.add("hidden");
    volunteerField.classList.add("hidden");
    paymentBox.classList.add("hidden"); // hide initially

    if (this.value === "attendee") {
      batchField.classList.remove("hidden");
    }

    if (this.value === "volunteer") {
      volunteerField.classList.remove("hidden");
    }
  });
}

// Log submission to confirm the form is actually submitting
if (form) {
  form.addEventListener("submit", function () {
    console.log("register form submit triggered");
  });
}

// DO NOT prevent default submission!
// Form will submit to Django and redirect to success page.