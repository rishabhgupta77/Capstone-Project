from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory DB (Added 'price' to match frontend expectations)
# In-memory DB with corrected thumbnails
songs = [
    {
        "id": 1, 
        "name": "Blinding Lights", 
        "artist": "The Weeknd", 
        "price": 99, 
        "thumbnail": "https://i.scdn.co/image/ab67616d0000b273881297eaa7d7e3014744842b"
    },
    {
        "id": 2, 
        "name": "Shape of You", 
        "artist": "Ed Sheeran", 
        "price": 89, 
        "thumbnail": "https://i.scdn.co/image/ab67616d0000b273881297eaa7d7e3014744842b"
    },
    {
        "id": 3, 
        "name": "Levitating", 
        "artist": "Dua Lipa", 
        "price": 79, 
        "thumbnail": "/thumbnail/Screenshot 2026-04-29 at 11.02.05 PM.png"
    },
    {
        "id": 4, 
        "name": "Kesariya", 
        "artist": "Arijit Singh", 
        "price": 99, 
        "thumbnail": "https://i.scdn.co/image/ab67616d0000b273c50926d83764835c2a13f01b"
    },
    {
        "id": 5, 
        "name": "Tum Hi Ho", 
        "artist": "Arijit Singh", 
        "price": 89, 
        "thumbnail": "https://i.scdn.co/image/ab67616d0000b273b062be556d35b91b92e3532f"
    }
]

# Helper: Validate Data
def validate_song(data):
    if not data:
        return "No data provided"
    if "name" not in data or not data["name"]:
        return "Name is required"
    if "artist" not in data or not data["artist"]:
        return "Artist is required"
    if "price" not in data:
        return "Price is required"
    if not isinstance(data["price"], (int, float)):
        return "Price must be a number"
    return None

# GET all songs
@app.route("/products", methods=["GET"])
def get_songs():
    return jsonify(songs), 200

# POST new song
@app.route("/products", methods=["POST"])
def add_song():
    data = request.get_json()

    error = validate_song(data)
    if error:
        return jsonify({"error": error}), 400

    new_song = {
        "id": len(songs) + 1,
        "name": data["name"],
        "artist": data["artist"],
        "price": data["price"],
        # Provide a fallback thumbnail for new songs
        "thumbnail": data.get("thumbnail", "https://via.placeholder.com/150") 
    }

    songs.append(new_song)

    return jsonify({
        "message": "Song added successfully",
        "data": new_song
    }), 201

# Run server
if __name__ == "__main__":
    app.run(port=5001, debug=True)