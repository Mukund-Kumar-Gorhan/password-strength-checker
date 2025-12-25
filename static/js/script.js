document.getElementById('checkBtn').addEventListener('click', function() {
    const password = document.getElementById('passwordInput').value;
    const modal = document.getElementById('resultModal');

    if (!password) {
        alert("Please enter a password first.");
        return;
    }

    // Send data to Flask backend
    fetch('/check-strength', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password: password })
    })
    .then(response => response.json())
    .then(data => {
        // Update Modal UI
        document.getElementById('strengthPercent').innerText = data.percentage + "%";
        document.getElementById('strengthLabel').innerText = data.label;
        document.getElementById('explanationText').innerText = data.explanation;

        // Dynamic Color for Label
        const labelEl = document.getElementById('strengthLabel');
        if (data.percentage <= 40) labelEl.style.color = "#ef4444";
        else if (data.percentage <= 79) labelEl.style.color = "#f59e0b";
        else labelEl.style.color = "#10b981";

        // Show Modal
        modal.style.display = "block";
    })
    .catch(error => console.error('Error:', error));
});

// Close Modal logic
document.querySelector('.close-btn').onclick = function() {
    document.getElementById('resultModal').style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById('resultModal');
    if (event.target == modal) {
        modal.style.display = "none";
    }
}