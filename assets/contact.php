<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);

    // Recipients
    $to = "monishr608@gmail.com,shaswatmishra5533@gmail.com,Mdjunaid59946@gmail.com,prashanth3792@gmail.com,mouryachittibabu@gmail.com,shadabsaleem207@gmail.com";

    // Subject and email body
    $email_subject = "New Contact Form Submission: $subject";
    $email_body = "Name: $name\nEmail: $email\n\nMessage:\n$message";

    // Headers
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send email
    if (mail($to, $email_subject, $email_body, $headers)) {
        // Redirect to thank you page if email is sent successfully
        header("Location: contactthankyou.html");
        exit();
    } else {
        echo "Error sending email.";
    }
}
?>
