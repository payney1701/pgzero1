def updateTrack(): # Function to update where the track blocks appear
    global trackCount, trackPosition, trackDirection, trackWidth
    b = 0
    while b < len(trackLeft):
        trackLeft[b].y += SPEED
        trackRight[b].y += SPEED
        b += 1
    if trackLeft[len(trackleft)-1].y > 32:
        if trackDirection == False: trackPosition += 16
        if trackDirection == True: trackPosition -= 16
        if randint (0, 4) == 1: trackDirection = not trackDirection
        if trackPosition > 700-trackWidth: trackDirection = True
        if trackPosition < trackWidth: trackDirection = False
        makeTrack()