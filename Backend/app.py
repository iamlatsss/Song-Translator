from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dummy endpoint to test
@app.route('/api/translate', methods=['POST'])
def translate_song():
    data = request.json
    song_name = data.get('song_name')
    
    # Replace this with your NLP model logic
    english_lyrics = "This is the English lyrics of " + song_name
    tamil_lyrics = "இது " + song_name + " பாடலின் தமிழ் பாடல் வரிகள்"
    
    return jsonify({
        "english": english_lyrics,
        "tamil": tamil_lyrics
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)
