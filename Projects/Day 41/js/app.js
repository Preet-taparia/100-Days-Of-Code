const parallax_el = document.querySelectorAll(".parallax");
const main = document.querySelector("main");

let xValue = 0,
    yValue = 0;

let rotatedegree = 0;

function update(cursorX, rotateDegree) {

    parallax_el.forEach(el => {
        let speedx = el.dataset.speedx;
        let speedy = el.dataset.speedy;
        let speedz = el.dataset.speedz;
        let rotation = el.dataset.rotation;

        let zValue = cursorX - parseFloat(getComputedStyle(el).left);

        let isInLeft = window.innerWidth / 2 > getComputedStyle(el).left ? 1 : 0;

        el.style.transform = `translateX(calc(-50% + ${xValue * speedx}px)) translateY(calc(-50% + ${yValue * speedy}px)) perspective(2300px)  translateZ(${zValue * isInLeft * speedz}px) rotateY(${rotateDegree * rotation}deg)`;
    })
}

update(0, 0);

window.addEventListener("mousemove", (e) => {
    if (timeline.isActive()) return;
    xValue = e.clientX - window.innerWidth / 2;
    yValue = e.clientY - window.innerHeight / 2;

    rotateDegree = xValue / (window.innerWidth / 2) * 20;

    update(e.clientX, rotateDegree);
})

if (window.innerWidth >= 725) {
    main.style.maxHeight = `${window.innerWidth * 0.6}px`;
} else {
    main.style.maxHeight = `${window.innerWidth * 1.6}px`;
}


let timeline = gsap.timeline();


timeline.from(".text h1", {
    y: window.innerHeight - document.querySelector(".text h1").getBoundingClientRect().top + 200,
    duration: 2,
}, "0.5");

timeline.from(".text h2", {
    y: - document.querySelector(".text h2").getBoundingClientRect().top,
    opacity: 0,
    duration: 1.5,
}, "1");

timeline.from(".hide", {
    opacity: 0,
    duration: 1.5
}, "1.5");
