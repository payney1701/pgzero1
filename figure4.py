def draw(): # Pygame Zero draw function
    global gameStatus
    screen.fill((128, 128, 128))
    if gameStatus == 0:
        car.draw()
        b = 0
        while b < len(trackLeft):
            trackLeft[b].draw()
            trackRight[b].draw()
            b += 1
    if gameStatus == 1:
        Red Flag

    if gameStatus == 2:
        Chequered Flag

def update(): # Pygame Zero update function
    global gameStatus, trackCount
    if gameStatus == 0:
        if keyboard.left: car.x -= 2
        if keyboard.right: car.x += 2
        updateTrack()
    if trackCount > 200: gameStatus = 2 # Chequered Flag