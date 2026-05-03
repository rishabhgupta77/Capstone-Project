const BASE_URL = "http://127.0.0.1:5001/products";

window.onload = () => {
    loadSongs();
};

async function loadSongs() {
    try {
        const res = await fetch(BASE_URL);
        if (!res.ok) {
            throw new Error(`Server returned ${res.status}`);
        }

        const songs = await res.json();
        renderSongs(songs);
    } catch (err) {
        const container = document.getElementById("songsContainer");
        container.innerHTML = `<p class="error-message">Unable to load songs. ${err.message}</p>`;
        console.error("Error:", err);
    }
}

function renderSongs(songs) {
    const container = document.getElementById("songsContainer");
    container.innerHTML = "";

    if (!Array.isArray(songs) || songs.length === 0) {
        container.innerHTML = "<p>No songs available right now.</p>";
        return;
    }

    songs.forEach(song => {
        const div = document.createElement("div");
        div.className = "song-card";

        div.innerHTML = `
            <img src="${song.thumbnail}" alt="${song.name}">
            <h3>${song.name}</h3>
            <p><strong>Artist:</strong> ${song.artist}</p>
            <p><strong>Price:</strong> ₹${song.price}</p>
        `;

        container.appendChild(div);
    });
}