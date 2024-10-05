<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $subject = htmlspecialchars($_POST['subject']);
    $message = htmlspecialchars($_POST['message']);

    // Here you would typically send the email or save the data
    // For now, we can just redirect to a thank you page
    header("Location: contactthankyou.html");
    exit(); // Ensure no further code is executed after redirection
} else {
    echo "Invalid request method.";
}
?>
