document.addEventListener("DOMContentLoaded", function() {
    const puzzleContainer = document.getElementById("puzzleContainer");
    const orderButton = document.getElementById("orderButton");
    const resetButton = document.getElementById("resetButton");
    const shuffleButton = document.getElementById("shuffleButton");
    const timerDisplay = document.getElementById("timerDisplay");
    let puzzlePieces = [];
    let emptyIndex = 41;
    let timerInterval = null;
    let elapsedTime = 0;
    let isRunning = false;

    // Sélectionne une musique aléatoire parmi les 9 fichiers disponibles
    const numSongs = 9;
    let songIndex = Math.floor(Math.random() * numSongs) + 1;
    let audio = new Audio(`songs/song${songIndex}.mp3`);

    // Fonction pour jouer une nouvelle musique après la fin de la précédente
    function playNextSong() {
        songIndex = Math.floor(Math.random() * numSongs) + 1;
        audio.src = `songs/song${songIndex}.mp3`;
        audio.play().catch(error => console.log("Lecture bloquée :", error));
    }

    // Lorsque la chanson se termine, jouer la suivante
    audio.addEventListener("ended", playNextSong);

    // Démarrer la musique au premier clic sur la page
    document.addEventListener("click", () => {
        if (audio.paused) {
            audio.play().catch(error => console.log("Autoplay bloqué :", error));
        }
    }, { once: true });

    function startTimer() {
        if (isRunning) return; // Empêche le démarrage de plusieurs timers
        stopTimer(); // Assure qu'aucun autre timer ne tourne
        timerInterval = setInterval(() => {
            elapsedTime++;
            updateTimerDisplay();
        }, 1000);
        isRunning = true;
    }

    function stopTimer() {
        clearInterval(timerInterval);
        timerInterval = null;
        isRunning = false;
    }

    function updateTimerDisplay() {
        const minutes = Math.floor(elapsedTime / 60);
        const seconds = elapsedTime % 60;
        timerDisplay.textContent = `الوقت: ${minutes} دقيقة ${seconds} ثانية`;
    }

    function createPuzzle(shuffle = true) {
        stopTimer(); // Arrêter le chrono avant de créer le puzzle
        puzzleContainer.innerHTML = "";
        puzzlePieces = [];
        let imagePaths = [];

        for (let i = 0; i < 41; i++) { // Seulement 41 images pour laisser un espace vide
            imagePaths.push(`images/slide_${i + 1}.png`);
        }
        imagePaths.push(""); // Case vide à la fin

        if (shuffle) {
            for (let i = imagePaths.length - 2; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [imagePaths[i], imagePaths[j]] = [imagePaths[j], imagePaths[i]];
            }
        }

        for (let i = 0; i < 42; i++) {
            const piece = document.createElement("div");
            piece.classList.add("puzzle-piece");
            if (imagePaths[i] !== "") {
                piece.style.backgroundImage = `url(${imagePaths[i]})`;
            } else {
                emptyIndex = i;
            }
            piece.addEventListener("click", () => {
                movePiece(i);
                if (!isRunning) {
                    startTimer();
                }
            });
            puzzleContainer.appendChild(piece);
            puzzlePieces.push(piece);
        }
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

    function orderPuzzle() {
        stopTimer();
        createPuzzle(false);
    }

    function resetPuzzle() {
        stopTimer();
        elapsedTime = 0; // Remise à zéro du chrono
        updateTimerDisplay();
        createPuzzle();
    }

    orderButton.addEventListener("click", orderPuzzle);
    resetButton.addEventListener("click", resetPuzzle);
    shuffleButton.addEventListener("click", () => {
        stopTimer();
        elapsedTime = 0; // Remise à zéro du chrono
        createPuzzle();
    });
    createPuzzle();
});
