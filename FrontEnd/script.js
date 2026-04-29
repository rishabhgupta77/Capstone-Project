const BASE_URL = "http://127.0.0.1:5001/products";

window.onload = () => {
    loadSongs();
};

async function loadSongs() {
    try {
        const res = await fetch(BASE_URL);
        const songs = await res.json();
        renderSongs(songs);
    } catch (err) {
        console.log("Error:", err);
    }
}

function renderSongs(songs) {
    const container = document.getElementById("songsContainer");
    container.innerHTML = "";

    songs.forEach(song => {
        const div = document.createElement("div");
        div.className = "song-card";

        // Check that song.thumbnail matches the key name in your Python app.py
        div.innerHTML = `
            <img src="${song.thumbnail}" alt="${song.name}">
            <h3>${song.name}</h3>
            <p><strong>Artist:</strong> ${song.artist}</p>
            <p><strong>Price:</strong> ₹${song.price}</p>
        `;

        container.appendChild(div);
    });
}