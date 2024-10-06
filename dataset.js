document.getElementById('image-upload-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    
    // Get the image file from the input
    const imageInput = document.getElementById('image-input');
    const file = imageInput.files[0];
    
    if (file) {
        const formData = new FormData();
        formData.append('image', file);

        // Send the image to the backend Flask server
        const response = await fetch('/scan_image', {
            method: 'POST',
            body: formData
        });

        // Parse the response and show prediction
        const result = await response.json();
        document.getElementById('prediction').innerText = result.prediction;
    } else {
        alert("Please upload an image.");
    }
});
