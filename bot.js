const chatbotToggler = document.querySelector('.chatbot-toggler');
const chatbot = document.querySelector('.chatbot');
const closeBtn = document.querySelector('.close-btn');

chatbotToggler.addEventListener('click', () => {
    chatbot.style.display = chatbot.style.display === 'none' || !chatbot.style.display ? 'block' : 'none';
});

closeBtn.addEventListener('click', () => {
    chatbot.style.display = 'none';
});