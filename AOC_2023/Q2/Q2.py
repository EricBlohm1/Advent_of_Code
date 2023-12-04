file = open("input.txt", "r")

maxBalls = [("12","red"), ("13","green"), ("14","blue")]

def extractID(line):
    i = 0
    id = ""
    #every digit until ':' is part of the ID
    while(line[i] != ':'):
        if line[i].isdecimal(): 
            id = id + line[i]
        i += 1
    return id

#create a list of tuples, the tuples have a number of balls and a color
def extractsubset(round):
    subsets = []
    i = 0
    while i < len(round):
        col = ""
        balls = ""
        while (i < len(round) and (round[i] != ',') ):
            if round[i].isdigit():
                balls += round[i]

            if round[i].isalpha():
                col += round[i]
            i += 1
        subsets.append((balls,col))
        i+=1
    return subsets

def checkMaxBalls(round):
    allOk = []
    for i in range(len(round)):

        if round[i][1] == "green":
            if int(round[i][0]) <= int(maxBalls[1][0]):
                allOk.append(True)
            else:
                allOk.append(False)

        elif round[i][1] == "blue":
            if int(round[i][0]) <= int(maxBalls[2][0]):
                allOk.append(True)
            else:
                allOk.append(False)

        elif round[i][1] == "red":
            if int(round[i][0]) <= int(maxBalls[0][0]):
                allOk.append(True)  
            else:
                allOk.append(False)
    #print(all(allOk))
    return all(allOk)

def main():
    valid_games = []
    for line in file.readlines():
        #list of booleans
        roundOk = []

        #id is a string
        id = extractID(line)


        # index 1 in rounds is to the right of ':'
        rounds = line.split(':')[1]

        # split each game into subsets, divided by 3
        for round in rounds.split(';'):
            tuple_round = extractsubset(round)

            # append true if round is valid, otherwise false
            roundOk.append(checkMaxBalls(tuple_round))

        # if all rounds ok, add id to list of valid games    
        if all(roundOk):
            valid_games.append(int(id))

    sum_ids = sum(valid_games)
    print(str(sum_ids))
        

if __name__ == "__main__":
    main()