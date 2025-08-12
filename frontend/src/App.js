import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setResult("Please upload a file first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/api/classify", formData);
      setResult("Predicted: " + res.data.label);
    } catch (err) {
      setResult("Error: " + err.message);
    }
  };

  return (
    <div className="container">
      <h2>Waste Classifier</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Classify</button>
      <p>{result}</p>
    </div>
  );
}

export default App;