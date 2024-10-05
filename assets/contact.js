//document.addEventListener("DOMContentLoaded", function() {
    //const form = document.querySelector("form");

    //form.addEventListener("submit", function(event) {
        //const name = form.querySelector("[name='name']").value;
        //const email = form.querySelector("[name='email']").value;
        //const subject = form.querySelector("[name='subject']").value;
        //const message = form.querySelector("[name='message']").value;

        //if (!name || !email || !subject || !message) {
            //alert("Please fill out all fields.");
            //event.preventDefault();
        //}
    //});
//});

// contact.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    form.addEventListener("submit", function () {
        alert("Your message is being sent...");
    });
});

