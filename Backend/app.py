from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from deep_translator import GoogleTranslator  # <- new translator

app = Flask(__name__)
CORS(app)

port = int(os.environ.get('PORT', 5000))

df = pd.read_csv("songs.csv")

@app.route("/songs")
def get_songs():
    songs = df["Title"].tolist()
    return jsonify({"songs": songs})


@app.route("/lyrics", methods=["POST"])
def get_lyrics():
    data = request.get_json()
    song_name = data.get("song")

    lyrics_list = df.loc[df["Title"] == song_name, "Lyric"].values
    if len(lyrics_list) > 0:
        english_lyric = lyrics_list[0]
        # Translate to Tamil
        tamil_lyric = GoogleTranslator(source='auto', target='ta').translate(english_lyric)
        return jsonify({"tamil": tamil_lyric})
    else:
        return jsonify({"tamil": ""})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
