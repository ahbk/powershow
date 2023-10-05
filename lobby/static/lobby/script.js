const background = document.getElementById("background");
const current = document.getElementById("currentPower");
const sun = document.createElement("div");
sun.className = "sun";
background.appendChild(sun);

let isDragging = false;
let initialX, initialY;
let offsetX = 0, offsetY = 0;

async function update() {
    let response = await fetch('update/');
    if(response.ok) {
        let result = await response.json();
        console.log(result);
        moveSun(result.sun_x*2, result.sun_y);
        current.innerHTML = result.stats.current_power_kw;
    }
    return {};
}
update();
setInterval(update, 60000);

function moveSun(ux, uy) {
    let x = ux*background.clientWidth;
    let y = background.clientHeight - uy*background.clientHeight;
    let unit = 'px';
    let shade = (1 - (.5 * y) / background.clientHeight);
    let pos = `${x}${unit} ${y}${unit}`;
    let shine = `rgb(255, ${255*shade}, 0)`;
    let sky = `rgb(${135*shade}, ${206*shade}, ${235*shade})`;

    sun.style.transform = `translate(${x}${unit}, ${y}${unit})`;
    sun.style.background = `rgb(255, 255, ${255*shade})`;
    background.style.background = `radial-gradient(circle at ${pos}, ${shine}, ${sky} 50%`;
}

sun.addEventListener("mousedown", (e) => {
    isDragging = true;
    initialX = e.clientX - offsetX;
    initialY = e.clientY - offsetY;
    sun.style.cursor = "grabbing"; // Change cursor when dragging
});

document.addEventListener("mousemove", (e) => {
    if (!isDragging) return;
    offsetX = e.clientX - initialX;
    offsetY = e.clientY - initialY;
    moveSun(offsetX, offsetY);
});

document.addEventListener("mouseup", () => {
    if (!isDragging) return;
    isDragging = false;
    sun.style.cursor = "grab";
});
