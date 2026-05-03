from flask import Flask, request, jsonify
from flask_cors import CORS

# Create Flask App
app = Flask(__name__)

# Enable CORS
CORS(app)

# In-Memory Database
songs = [
    {
        "id": 1,
        "name": "Blinding Lights",
        "artist": "The Weeknd",
        "price": 99,
        "thumbnail": "download.jpeg"
    },
    {
        "id": 2,
        "name": "Shape of You",
        "artist": "Ed Sheeran",
        "price": 89,
        "thumbnail": "Shape of you von.jpeg"
    },
    {
        "id": 3,
        "name": "Levitating",
        "artist": "Dua Lipa",
        "price": 79,
        "thumbnail": "Screenshot 2026-04-29 at 11.02.05 PM.png"
    },
    {
        "id": 4,
        "name": "Kesariya",
        "artist": "Arijit Singh",
        "price": 99,
        "thumbnail": "Kesariya.jpeg"
    },
    {
        "id": 5,
        "name": "Sweater Weather",
        "artist": "The Neighbourhood",
        "price": 89,
        "thumbnail": "Sweat.jpeg"
    },
    {
        "id": 6,
        "name": "505",
        "artist": "Arctic Monkeys",
        "price": 79,
        "thumbnail": "Arctic Monkey.jpeg"
    }
]

# -----------------------------------
# Helper Functions
# -----------------------------------

def get_next_song_id():
    return max((song["id"] for song in songs), default=0) + 1


def validate_song(data, require_all_fields=True):
    if not data:
        return "No data provided"

    if require_all_fields or "name" in data:
        if "name" not in data or not data["name"]:
            return "Name is required"

    if require_all_fields or "artist" in data:
        if "artist" not in data or not data["artist"]:
            return "Artist is required"

    if require_all_fields and "price" not in data:
        return "Price is required"

    if "price" in data and not isinstance(data["price"], (int, float)):
        return "Price must be a number"

    return None


# ----------------------
# GET All Songs API
# ----------------------
@app.route("/products", methods=["GET"])
def get_songs():

    return jsonify(songs), 200


# ----------------------
# GET Single Song API
# ----------------------
@app.route("/products/<int:id>", methods=["GET"])
def get_single_song(id):

    for song in songs:
        if song["id"] == id:
            return jsonify(song), 200

    return jsonify({
        "error": "Song not found"
    }), 404


# ----------------------
# POST New Song API
# ----------------------
@app.route("/products", methods=["POST"])
def add_song():

    data = request.get_json()

    # Validate Input
    error = validate_song(data)

    if error:
        return jsonify({
            "error": error
        }), 400

    # Create New Song
    new_song = {
        "id": get_next_song_id(),
        "name": data["name"],
        "artist": data["artist"],
        "price": data["price"],
        "thumbnail": data.get("thumbnail", "download.jpeg")
    }

    # Add Song
    songs.append(new_song)

    return jsonify({
        "message": "Song added successfully",
        "data": new_song
    }), 201


# ----------------------
# UPDATE Song API
# ----------------------
@app.route("/products/<int:id>", methods=["PUT"])
def update_song(id):

    data = request.get_json() or {}

    for song in songs:

        if song["id"] == id:
            error = validate_song(data, require_all_fields=False)
            if error:
                return jsonify({
                    "error": error
                }), 400

            # Update Values
            song["name"] = data.get("name", song["name"])
            song["artist"] = data.get("artist", song["artist"])
            song["price"] = data.get("price", song["price"])
            song["thumbnail"] = data.get("thumbnail", song["thumbnail"])

            return jsonify({
                "message": "Song updated successfully",
                "data": song
            }), 200

    return jsonify({
        "error": "Song not found"
    }), 404


# ----------------------
# DELETE Song API
# ----------------------
@app.route("/products/<int:id>", methods=["DELETE"])
def delete_song(id):

    for song in songs:

        if song["id"] == id:

            songs.remove(song)

            return jsonify({
                "message": "Song deleted successfully"
            }), 200

    return jsonify({
        "error": "Song not found"
    }), 404


# ----------------------
# Run Flask Server
# ----------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )