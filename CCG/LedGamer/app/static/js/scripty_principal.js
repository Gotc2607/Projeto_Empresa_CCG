// script.js
document.addEventListener('DOMContentLoaded', function() {
    const cube = document.querySelector('.cube-3d-wrapper');
    const navItems = document.querySelectorAll('#navMenu li');
    const themeToggle = document.getElementById('theme-toggle');

    // Posições das faces do cubo
    const facePositions = {
        'inicio': 'rotateY(0deg)',
        'produtos': 'rotateY(-90deg)',
        'ofertas': 'rotateY(-180deg)',
        'config': 'rotateY(90deg)',
        'sobre': 'rotateX(-90deg)',
        'contato': 'rotateX(90deg)'
    };

    // Controle de navegação
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            const target = this.dataset.target;
            
            // Atualiza a rotação do cubo
            if (window.innerWidth > 768) {
                cube.style.transform = facePositions[target];
            } else {
                // Modo mobile - mostra a face correspondente
                document.querySelectorAll('.cube-face').forEach(face => {
                    face.classList.remove('active');
                });
                document.getElementById(target).classList.add('active');
            }
            
            // Atualiza o item ativo no menu
            navItems.forEach(li => li.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Controle do tema
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-theme');
            
            // Salva preferência (opcional)
            localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
        });
    }

    // Verifica tema salvo (opcional)
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
    }

    // Ajuste responsivo do cubo
    function adjustCubeSize() {
        if (window.innerWidth > 768) {
            const container = document.querySelector('.container-principal');
            const newSize = Math.min(
                container.offsetWidth * 0.9, 
                container.offsetHeight * 0.9
            );
            document.documentElement.style.setProperty('--cube-size', `${newSize}px`);
        }
    }

    // Executa no carregamento e redimensionamento
    window.addEventListener('load', adjustCubeSize);
    window.addEventListener('resize', adjustCubeSize);
});