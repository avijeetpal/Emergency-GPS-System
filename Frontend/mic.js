let isRecording = false;
let mediaRecorder;
let chunks = [];

function toggleRecording() {
    if (!isRecording) {
        startRecording();
    } else {
        stopRecording();
    }
}

function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function(stream) {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.ondataavailable = function(e) {
                chunks.push(e.data);
            };
            mediaRecorder.onstop = function() {
                const blob = new Blob(chunks, { 'type' : 'audio/ogg; codecs=opus' });
                const audioUrl = window.URL.createObjectURL(blob);
                const audio = new Audio(audioUrl);
                audio.controls = true;
                document.body.appendChild(audio);
            };
            mediaRecorder.start();
            isRecording = true;
            document.getElementById('micButton').classList.add('active');
        })
        .catch(function(err) {
            console.error('Error accessing microphone:', err);
        });
}

function stopRecording() {
    mediaRecorder.stop();
    isRecording = false;
    document.getElementById('micButton').classList.remove('active');
}
