import { useState } from "react";
import axios from "axios";

function App() {
  const [songName, setSongName] = useState("");
  const [lyrics, setLyrics] = useState({ english: "", tamil: "" });
  const [loading, setLoading] = useState(false);

  const fetchLyrics = async () => {
    if (!songName.trim()) {
      alert("Enter a song name");
      return;
    }
    setLoading(true);
    try {
      const res = await axios.post("http://localhost:5001/api/translate", { song_name: songName });
      setLyrics(res.data);
    } catch (err) {
      console.error(err);
      alert("Error fetching lyrics");
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Song Translator</h1>
      <input
        type="text"
        placeholder="Enter song name"
        value={songName}
        onChange={(e) => setSongName(e.target.value)}
      />
      <button onClick={fetchLyrics}>Translate</button>

      {loading ? <p>Loading...</p> : null}

      {lyrics.english && (
        <div>
          <h2>English Lyrics:</h2>
          <p>{lyrics.english}</p>
          <h2>Tamil Lyrics:</h2>
          <p>{lyrics.tamil}</p>
        </div>
      )}
    </div>
  );
}

export default App;
