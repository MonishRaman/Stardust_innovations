document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function (event) {
        // Optional: You could add a confirmation dialog here instead of an alert
        alert("Your message is being sent...");
    });
});
