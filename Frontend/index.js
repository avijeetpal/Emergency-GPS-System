 function startSpeechRecognition() {
  const lang = document.getElementById('language').value; // Get selected language
  const recognition = new webkitSpeechRecognition() || new SpeechRecognition(); // Create a new instance of SpeechRecognition
  recognition.lang = lang; // Set language based on user selection
  recognition.start(); // Start recognition

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript; // Get the recognized text
    document.getElementById('output').textContent = transcript; // Display the recognized text
  };

  recognition.onerror = function(event) {
    console.error('Speech recognition error:', event.error);
  };
}
