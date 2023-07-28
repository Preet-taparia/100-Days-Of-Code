const canvas = document.getElementById('canvas1');
const ctx = canvas.getContext('2d');

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;


(function () {
    let particleArray = [];

    const color1 = '#fff';
    let hue = 334;
    let sw = 133;
    let sh = 30;

    const mouse = {
        x: null,
        y: null,
        radius: 150
    };

    let addJustX = (canvas.width - sw * 10) / 2;
    let addJustY = (canvas.height - sh * 10) / 2;

    window.addEventListener('mousemove', (e) => {
        mouse.x = e.x;
        mouse.y = e.y;
        mouse.radius = 150;
    });

    window.addEventListener('mouseout', () => {
        mouse.x = undefined;
        mouse.y = undefined;
    });

    window.addEventListener("resize", ()=> {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        addJustX = (canvas.width - sw * 10) / 2;
        addJustY = (canvas.height - sh * 10) / 2;
        init();
    });

    ctx.fillStyle = color1;
    ctx.font = '27px Verdana';
    ctx.fillText('Sayonara', 3, 25)
    const textCoordinates = ctx.getImageData(0, 0, sw, sh);

    class Particle {
        constructor(x, y, color) {
            this.x = x;
            this.y = y;
            this.size = 3;
            this.color = color;
            this.bazeX = this.x;
            this.bazeY = this.y;
            this.density = Math.random() * 40 + 5;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.closePath();
            ctx.fill();
        }

        update() {
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            let forceDirectionX = dx / distance;
            let forceDirectionY = dy / distance;
            let maxDistance = mouse.radius;
            let force = (maxDistance - distance) / maxDistance;
            let directionX = forceDirectionX * force * this.density;
            let directionY = forceDirectionY * force * this.density;
            if (distance < mouse.radius) {
                this.x -= directionX;
                this.y -= directionY;
                this.color = `hsl(${hue}, 80%, 60%)`;
            } else {
                this.color = color1;
                if (this.x !== this.bazeX) {
                    let dx = this.x - this.bazeX;
                    this.x -= dx / 10;
                }
                if (this.y !== this.bazeY) {
                    let dy = this.y - this.bazeY;
                    this.y -= dy / 10;
                }
            }
        }

    }

    function init() {
        particleArray = [];
        for (let y = 0; y < textCoordinates.height; y++) {
            for (let x = 0; x < textCoordinates.width; x++) {
                if (textCoordinates.data[(y * 4 * textCoordinates.width) + (x * 4)] > 128) {
                    let positionX = x * 10 + addJustX;
                    let positionY = y * 10 + addJustY;
                    particleArray.push(new Particle(positionX, positionY, '#fff'))
                }
            }
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particleArray.length; i++) {
            particleArray[i].update();
            particleArray[i].draw();
        }
        connect();
        requestAnimationFrame(animate);
    }

    function hueRotate() {
        hue+= 1;
        requestAnimationFrame(hueRotate);
    }

    function connect() {
        for (let i = 0; i < particleArray.length; i++) {
            for (let j = i + 1; j < particleArray.length; j++) {
                let elem1 = particleArray[i];
                let elem2 = particleArray[j];
                let distance = ((elem1.x - elem2.x) * (elem1.x - elem2.x)
                    + (elem1.y - elem2.y) * (elem1.y - elem2.y));
                let test = 400;
                if (distance < test) {
                    let opacity = (test - distance) / test;
                    if (elem1.color !== color1 && elem1.color !== color1) {
                        ctx.strokeStyle = `hsla(${hue}, 80%, 60%, ${opacity})`;
                    } else {
                        ctx.strokeStyle = `rgba(255, 255, 255, ${opacity})`;
                    }

                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.moveTo(elem1.x, elem1.y);
                    ctx.lineTo(elem2.x, elem2.y);
                    ctx.stroke();
                }
            }
        }

    }

    init();
    hueRotate();
    animate();

})();