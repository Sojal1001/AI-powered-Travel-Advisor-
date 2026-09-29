document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("searchForm");
  const resultsDiv = document.getElementById("results");
  const statusDiv = document.getElementById("status");

  form.addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent reload

    const mood = document.getElementById("mood").value.trim();
    const budget = document.getElementById("budget").value.trim();
    const days = document.getElementById("days").value.trim();
    const source = document.getElementById("source").value.trim();

    resultsDiv.innerHTML = "";
    statusDiv.textContent = "Fetching recommendations...";

    try {
      const response = await fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mood, budget, days, source }),
      });

      const data = await response.json();

      if (data.error) {
        statusDiv.textContent = "";
        resultsDiv.innerHTML = `<div class="error">${data.message}</div>`;
      } else if (data.results && data.results.length > 0) {
        statusDiv.textContent = `Found ${data.results.length} matching destinations 🌍`;

        resultsDiv.innerHTML = data.results
          .map(
            (r) => `
              <div class="card destination">
                <img src="${r.image_url || '/static/images/default.jpg'}"
                     alt="${r.destination || 'Destination'}"
                     onerror="this.src='/static/images/default.jpg'">
                <h3>${r.destination || 'Unknown Destination'}</h3>
                <p><strong>Category:</strong> ${r.category || 'N/A'}</p>
                <p><strong>State:</strong> ${r.state || 'N/A'}</p>
                <p><strong>Avg Cost:</strong> ₹${r.avg_cost || 'N/A'}</p>
                <p>${r.description || 'No description available.'}</p>
              </div>`
          )
          .join("");
      } else {
        statusDiv.textContent = "";
        resultsDiv.innerHTML = `<div class="empty">No destinations found for that mood.</div>`;
      }
    } catch (error) {
      console.error(error);
      statusDiv.textContent = "";
      resultsDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
    }
  });
});
