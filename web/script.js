document.getElementById('mediaInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;
    const url = URL.createObjectURL(file);
    
    if (file.type.startsWith('video/')) {
        document.getElementById('videoPlayer').src = url;
        document.getElementById('videoPlayer').style.display = 'block';
        document.getElementById('audioPlayer').style.display = 'none';
    } else if (file.type.startsWith('audio/')) {
        document.getElementById('audioPlayer').src = url;
        document.getElementById('audioPlayer').style.display = 'block';
        document.getElementById('videoPlayer').style.display = 'none';
    }
});