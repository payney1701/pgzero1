def makeTrack(): # Function to make a new section of track
    global trackCount, trackLeft, trackRight, trackPosition, trackWidth
    trackLeft.append(actor("barrier", pos = (trackPosition-trackWidth,0)))
    trackRight.append(actor("barrier", pos = (trackPosition+trackWidth,0)))
    trackCount += 1