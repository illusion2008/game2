<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bus Yatra Game</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            background-image: url("map.jpeg") ;
            background-repeat: no-repeat;
  background-attachment: fixed; 
  background-size: 100% 100%;
            
        } 
   


        
        .dice-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 5px;
            margin: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        #result {
            font-size: 24px;
            margin-bottom: 5px;
        }
        button {
            font-size: 14px;
            padding: 5px 10px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 3px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .draggable-truck {
            width: 50px;
            height: auto;
            position: absolute;
            cursor: move;
            user-select: none;
        }
    </style>
</head>
<body>
    <audio controls autoplay>
     <source src="music.mp3"/>
    </audio>
    <div class="game-container">
        <div class="dice-container">
            <div id="result">-</div>
            <button onclick="rollDice()">Roll Dice</button>
        </div>
    </div>
    
    <img src="blue.png" alt="Blue Truck" class="draggable-truck" id="blue-truck" style="top: 300px; left: 100px;">
    <img src="pink.png" alt="Purple Truck" class="draggable-truck" id="purple-truck" style="top: 300px; left: 250px;">

       <script>
        function rollDice() {
            const result = Math.floor(Math.random() * 6) + 1;
            document.getElementById('result').textContent = result;
        }

        const trucks = document.querySelectorAll('.draggable-truck');
        
        trucks.forEach(truck => {
            let isDragging = false;
            let currentX;
            let currentY;
            let initialX;
            let initialY;
            let xOffset = 0;
            let yOffset = 0;

            truck.addEventListener('mousedown', dragStart);
            truck.addEventListener('touchstart', dragStart, { passive: false });

            function dragStart(e) {
                if (e.type === 'touchstart') {
                    initialX = e.touches[0].clientX - xOffset;
                    initialY = e.touches[0].clientY - yOffset;
                } else {
                    initialX = e.clientX - xOffset;
                    initialY = e.clientY - yOffset;
                }

                isDragging = true;
                truck.style.cursor = 'grabbing';

                document.addEventListener('mousemove', drag);
                document.addEventListener('touchmove', drag, { passive: false });
                document.addEventListener('mouseup', dragEnd);
                document.addEventListener('touchend', dragEnd);
            }

            function drag(e) {
                if (isDragging) {
                    e.preventDefault();
                    if (e.type === 'touchmove') {
                        currentX = e.touches[0].clientX - initialX;
                        currentY = e.touches[0].clientY - initialY;
                    } else {
                        currentX = e.clientX - initialX;
                        currentY = e.clientY - initialY;
                    }

                    xOffset = currentX;
                    yOffset = currentY;

                    setTranslate(currentX, currentY, truck);
                }
            }

            function dragEnd(e) {
                isDragging = false;
                truck.style.cursor = 'move';

                document.removeEventListener('mousemove', drag);
                document.removeEventListener('touchmove', drag);
                document.removeEventListener('mouseup', dragEnd);
                document.removeEventListener('touchend', dragEnd);
            }

            function setTranslate(xPos, yPos, el) {
                el.style.transform = translate3d(${xPos}px, ${yPos}px, 0);
            }
        });
    </script>
</body>
</html>
