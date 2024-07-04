async function processText() {
    const userInput = document.getElementById('user_input').value;
    const preferredLang = document.getElementById('preferred_lang').value;
    const includeEntities = document.getElementById('include_entities').checked;

    const response = await fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            user_input: userInput,
            preferred_lang: preferredLang,
            include_entities: includeEntities
        }),
    });

    const data = await response.json();

    if (data.error) {
        alert(`Error: ${data.error}`);
        return;
    }

    document.getElementById('translated_text').innerHTML = data.translated_text;
    document.getElementById('summary').innerHTML = data.summary;

    if (data.entities) {
        highlightEntities(data.translated_text, data.entities);
    }
}

function highlightEntities(text, entities) {
    let highlightedText = text;
    entities.forEach(entity => {
        const entityText = text.substring(entity.start, entity.end);
        let link = entityText;
        if (entity.entity === 'I-LOC') {
            link = `<a href="https://www.google.com/maps/search/${entityText}" target="_blank">${entityText}</a>`;
        } else if (entity.entity === 'I-ORG' || entity.entity === 'I-PER') {
            link = `<a href="https://en.wikipedia.org/wiki/${entityText}" target="_blank">${entityText}</a>`;
        }
        highlightedText = highlightedText.replace(entityText, `<span class="highlight">${link}</span>`);
    });
    document.getElementById('translated_text').innerHTML = highlightedText;
}
