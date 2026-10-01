const statusElement = document.getElementById("status");
const refreshButton = document.getElementById("refresh");

async function checkBackend() {
    statusElement.textContent = "Checking...";

    try {
        const response = await fetch("http://127.0.0.1:5000/api/status");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        statusElement.textContent = data.status;
    } catch (error) {
        statusElement.textContent = "Backend unavailable";
        console.error(error);
    }
}

refreshButton.addEventListener("click", checkBackend);

checkBackend();
