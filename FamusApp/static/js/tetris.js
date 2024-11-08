// static/js/tetris.js

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Game settings
const ROWS = 20;
const COLS = 10;
const BLOCK_SIZE = 30;
const EMPTY_COLOR = "#333";
const colors = ["#FF5733", "#FFBD33", "#33FF57", "#335BFF", "#FF33A2"];

// Tetromino shapes
const tetrominoes = [
    [[1, 1, 1, 1]], // I
    [[1, 1], [1, 1]], // O
    [[0, 1, 1], [1, 1, 0]], // S
    [[1, 1, 0], [0, 1, 1]], // Z
    [[1, 1, 1], [0, 1, 0]], // T
    [[1, 1, 1], [1, 0, 0]], // L
    [[1, 1, 1], [0, 0, 1]]  // J
];

// Game board
let board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
let currentTetromino, currentX, currentY, currentColor;

// Control keys
const keys = {
    left: false,
    right: false,
    down: false,
    rotate: false
};

// Initialize a new tetromino
function newTetromino() {
    const shape = tetrominoes[Math.floor(Math.random() * tetrominoes.length)];
    currentTetromino = shape;
    currentColor = colors[Math.floor(Math.random() * colors.length)];
    currentX = Math.floor(COLS / 2) - Math.floor(shape[0].length / 2);
    currentY = 0;
}

// Draw the board and tetromino
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw the board
    for (let r = 0; r < ROWS; r++) {
        for (let c = 0; c < COLS; c++) {
            drawBlock(c, r, board[r][c] ? board[r][c] : EMPTY_COLOR);
        }
    }

    // Draw the current tetromino
    currentTetromino.forEach((row, y) => {
        row.forEach((cell, x) => {
            if (cell) {
                drawBlock(currentX + x, currentY + y, currentColor);
            }
        });
    });
}

// Draw a single block
function drawBlock(x, y, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
    ctx.strokeStyle = "#111";
    ctx.strokeRect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE);
}

// Move the tetromino down
function moveDown() {
    if (!collision(0, 1, currentTetromino)) {
        currentY++;
    } else {
        lockTetromino();
        newTetromino();
        if (collision(0, 0, currentTetromino)) {
            alert("Game Over");
            board = Array.from({ length: ROWS }, () => Array(COLS).fill(0));
        }
    }
}

// Lock the tetromino in place
function lockTetromino() {
    currentTetromino.forEach((row, y) => {
        row.forEach((cell, x) => {
            if (cell) {
                board[currentY + y][currentX + x] = currentColor;
            }
        });
    });
}

// Check for collision
function collision(offsetX, offsetY, piece) {
    return piece.some((row, y) => 
        row.some((cell, x) => 
            cell && (
                board[currentY + y + offsetY] &&
                board[currentY + y + offsetY][currentX + x + offsetX]
            )
        )
    );
}

// Rotate the tetromino
function rotate() {
    const rotated = currentTetromino[0].map((_, i) => currentTetromino.map(row => row[i]).reverse());
    if (!collision(0, 0, rotated)) currentTetromino = rotated;
}

// Handle input for movement and rotation
window.addEventListener("keydown", (e) => {
    switch (e.code) {
        case "ArrowLeft":
            if (!collision(-1, 0, currentTetromino)) currentX--;
            break;
        case "ArrowRight":
            if (!collision(1, 0, currentTetromino)) currentX++;
            break;
        case "ArrowDown":
            moveDown();
            break;
        case "ArrowUp":
            rotate();
            break;
    }
});

// Main game loop
function update() {
    moveDown();
    draw();
    setTimeout(update, 500);
}

// Start game
newTetromino();
update();
