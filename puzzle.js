document.addEventListener("DOMContentLoaded", function() {
    const puzzleContainer = document.getElementById("puzzleContainer");
    const timerDisplay = document.getElementById("timerDisplay");
    const titleDisplay = document.getElementById("titleDisplay");
    let timeElapsed = 0;
    let timer;
    
    const imagePaths = [];
    for (let i = 1; i <= 42; i++) {
        imagePaths.push(`images/slide_${i}.png`);
    }

    let emptyIndex = 41;
    const puzzlePieces = [];


    function shuffle(array) {
        for (let i = array.length - 2; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    function createPuzzle() {
        shuffle(imagePaths);
        for (let i = 0; i < 42; i++) {
            const piece = document.createElement("div");
            piece.classList.add("puzzle-piece");
            piece.style.backgroundImage = `url(${imagePaths[i]})`;
            piece.addEventListener("click", () => movePiece(i));
            puzzleContainer.appendChild(piece);
            puzzlePieces.push(piece);
        }
        puzzlePieces[emptyIndex].style.backgroundImage = "";
        startTimer();
    }

    function movePiece(index) {
        if (isAdjacent(index, emptyIndex)) {
            puzzlePieces[emptyIndex].style.backgroundImage = puzzlePieces[index].style.backgroundImage;
            puzzlePieces[index].style.backgroundImage = "";
            emptyIndex = index;
        }
    }

    function isAdjacent(index1, index2) {
        const row1 = Math.floor(index1 / 7);
        const col1 = index1 % 7;
        const row2 = Math.floor(index2 / 7);
        const col2 = index2 % 7;
        return (Math.abs(row1 - row2) + Math.abs(col1 - col2)) === 1;
    }

    createPuzzle();
});
