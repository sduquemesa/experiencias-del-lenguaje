var scl = 18;
var cols, rows;

function preload() {
    input_ascii = loadStrings('output.txt');
}

function setup() {
    frameRate(10);
    createCanvas(windowWidth, windowHeight);
    cols = floor(width / scl);
    rows = floor(height / scl);
    noStroke();
    textSize(scl / 1.5);
    fill(127);
}

function draw() {
    background(255);
    
    for (var x = 1; x < cols - 1; x++) {

        for (var y = 1; y < rows - 1; y++) {
            noiseDetail(3);

            var index = (x + y*cols) % input_ascii.length;
            var random_value = 0;
            var mouse_change = (abs(mouseX-windowWidth/2)/windowWidth + abs(mouseY-windowHeight/2)/windowHeight)/2;

            if (random() < mouse_change) {
                random_value = floor(random()*1000);
            }

            var character = int(input_ascii[index])+random_value;

            push();
            translate(x * scl + (scl / 2), y * scl + (scl / 2));
            text(char(character), 0, 0, scl, scl);
            pop();

        }
    }
}