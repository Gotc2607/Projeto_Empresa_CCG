document.addEventListener('DOMContentLoaded', () => {
    // Efeito de rastro neon
    const canvas = document.getElementById('neon-trail');
    const ctx = canvas.getContext('2d');
    
    // Ajusta o tamanho do canvas
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    const points = [];
    const maxPoints = 30;
    let mouseX = 0, mouseY = 0;
    let lastMoveTime = 0;
    let isMoving = false;
    let trailAlpha = 1;
    
    // Cores do efeito neon
    const neonColor = {
        r: 255,
        g: 255,
        b: 255
    };
    
    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
        addPoint(mouseX, mouseY);
        lastMoveTime = Date.now();
        isMoving = true;
        trailAlpha = 1;
    });
    
    function addPoint(x, y) {
        points.push({ x, y });
        if (points.length > maxPoints) {
            points.shift();
        }
    }
    
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const currentTime = Date.now();
        isMoving = (currentTime - lastMoveTime) < 100;
        
        if (!isMoving) {
            trailAlpha = Math.max(0, trailAlpha - 0.02);
        }
        
        if (trailAlpha > 0 && points.length >= 2) {
            ctx.lineWidth = 3;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            
            for (let i = 1; i < points.length; i++) {
                const segmentAlpha = trailAlpha * (i / points.length);
                const prev = points[i-1];
                const curr = points[i];
                
                const gradient = ctx.createLinearGradient(prev.x, prev.y, curr.x, curr.y);
                gradient.addColorStop(0, `rgba(${neonColor.r}, ${neonColor.g}, ${neonColor.b}, ${segmentAlpha})`);
                gradient.addColorStop(1, `rgba(${neonColor.r}, ${neonColor.g}, ${neonColor.b}, ${segmentAlpha*0.5})`);
                
                ctx.strokeStyle = gradient;
                ctx.shadowBlur = 15 * segmentAlpha;
                ctx.shadowColor = `rgb(${neonColor.r}, ${neonColor.g}, ${neonColor.b})`;
                
                ctx.beginPath();
                ctx.moveTo(prev.x, prev.y);
                ctx.lineTo(curr.x, curr.y);
                ctx.stroke();
            }
        }
        
        const cursorSize = isMoving ? 6 : 4;
        const cursorAlpha = isMoving ? 0.8 : 0.6;
        
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, cursorSize, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${neonColor.r}, ${neonColor.g}, ${neonColor.b}, ${cursorAlpha})`;
        ctx.shadowBlur = isMoving ? 20 : 15;
        ctx.shadowColor = `rgb(${neonColor.r}, ${neonColor.g}, ${neonColor.b})`;
        ctx.fill();
        
        while (points.length > maxPoints) {
            points.shift();
        }
        
        requestAnimationFrame(draw);
    }
    
    draw();
  });
  
  // Função flip corrigida
  function flip() {
    const card = document.querySelector(".flip-card");
    if (!card) return;
    
    card.classList.toggle("flipped");
    
    // Remove mensagens de erro se existirem
    document.querySelectorAll('.error-message').forEach(el => el.remove());
  }
  
  // Exporta função para uso no HTML
  window.flip = flip;