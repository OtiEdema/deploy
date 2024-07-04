document.getElementById('submitBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    const preferredLang = document.getElementById('preferredLang').value;

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_input: userInput,
            preferred_lang: preferredLang
        }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('lang').innerText = data.lang;
        document.getElementById('translatedText').innerText = data.translated_text;
        document.getElementById('entities').innerText = JSON.stringify(data.entities, null, 2);
        document.getElementById('summary').innerText = data.summary;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
