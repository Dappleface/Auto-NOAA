#TLE Splitting
#Sample string

def split(tle_raw):
    #gets tle, uses preset string to save time
    #tle_raw = "1 25544U 98067A 08264.51782528 -.00002182 00000-0 -11606-4 0 2927|2 25544 51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537"
    #splits the tle by the | charactor as often as it occurs into 2 strigns withing a list
    tle_split = tle_raw.split('|', -1)
    #Splits into 2 lines after the | charactor
    tle1_split = tle_split[0]
    tle2_split = tle_split[1]
    #splits up the first line of the tle by spaces
    ln1tle = tle1_split.split()
    #removes the stuff that isnt needed from the tle and leaves us with the epoch
    epoch = ln1tle.pop(3)

    #line 2
    ln2tle = tle2_split.split()
    inclination = ln2tle.pop(2)
    RaaN = ln2tle.pop(2)
    #Debug below this line
    print("epoch is: ", epoch)
    print("inclination is: ", inclination)
    print("Right Ascension of the Ascending Node is: ", RaaN)

split("1 25544U 98067A 08264.51782528 -.00002182 00000-0 -11606-4 0 2927|2 25544 51.6416 247.4627 0006703 130.5360 325.0288 15.72125391563537")

