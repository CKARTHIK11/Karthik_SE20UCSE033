document.getElementById('next-question').addEventListener('click', function() {
    fetch('http://localhost:5000/question')
        .then(response => response.json())
        .then(data => {
            if (data.question) {
                document.getElementById('question').innerText = data.question;
            } else {
                document.getElementById('question').innerText = 'Error fetching question.';
            }
        })
        .catch(error => {
            document.getElementById('question').innerText = 'Error fetching question.';
        });
});
