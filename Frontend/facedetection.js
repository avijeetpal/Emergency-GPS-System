// Get the canvas element
const canvas = document.getElementById('faceCanvas');
const ctx = canvas.getContext('2d');

// Set canvas size
canvas.width = 400;
canvas.height = 400;

// Draw a placeholder oval
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = '#333'; // Oval border color
ctx.fillStyle = 'rgba(255, 255, 255, 0.7)'; // Oval fill color with transparency
ctx.ellipse(canvas.width / 2, canvas.height / 2, 150, 200, 0, 0, 2 * Math.PI);
ctx.fill();
ctx.stroke();
