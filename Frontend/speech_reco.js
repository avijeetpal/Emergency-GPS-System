function toggleContent() {
    var toggleSwitch = document.getElementById('toggleSwitch');
    var content1 = document.getElementById('content1');
    var content2 = document.getElementById('content2');

    if (toggleSwitch.checked) {
        // Show content 2 and hide content 1
        content1.style.display = 'none';
        content2.style.display = 'block';
    } else {
        // Show content 1 and hide content 2
        content1.style.display = 'block';
        content2.style.display = 'none';
    }
}
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
