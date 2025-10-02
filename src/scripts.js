const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let dibujando = false;

canvas.addEventListener('mousedown', () => dibujando = true);
canvas.addEventListener('mouseup', () => dibujando = false);
canvas.addEventListener('mousemove', dibujar);

function dibujar(e) {
    if (!dibujando) return;
    ctx.fillStyle = 'black';
    ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 10, 0, Math.PI * 2);
    ctx.fill();
}

function limpiar() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    document.getElementById('resultado').innerText = '';
}

function predecir() {
    const imagen = canvas.toDataURL();
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imagen })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('resultado').innerText = `Predicción: ${data.resultado}`;
    });
}