document.addEventListener('DOMContentLoaded', function () {
    const startBtn = document.getElementById('start-recording');
    const stopBtn = document.getElementById('stop-recording');
    const preview = document.getElementById('preview');
    const fileInput = document.getElementById('recorded-file-input');
    const hiddenInput = document.getElementById('id_audio');

    let mediaRecorder;
    let audioChunks = [];

    startBtn.addEventListener('click', async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const audioUrl = URL.createObjectURL(audioBlob);
            preview.src = audioUrl;
            preview.style.display = 'block';

            const file = new File([audioBlob], 'recording.webm', { type: 'audio/webm' });
            const dataTransfer = new DataTransfer();
            dataTransfer.items.add(file);
            fileInput.files = dataTransfer.files;

            const event = new Event('change', { bubbles: true });
            fileInput.dispatchEvent(event);

            audioChunks = [];
            stream.getTracks().forEach(track => track.stop());
        };

        audioChunks = [];
        mediaRecorder.start();
        startBtn.disabled = true;
        stopBtn.disabled = false;
    });

    stopBtn.addEventListener('click', () => {
        mediaRecorder.stop();
        startBtn.disabled = false;
        stopBtn.disabled = true;
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            hiddenInput.value = '';
            hiddenInput.files = fileInput.files
        }
    });
});