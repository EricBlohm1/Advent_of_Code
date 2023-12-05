file = open("test.txt", "r")

numbers = "0123456789"

#returns a list of strings, which contains the indexes of consecutive digits.
def findPositionOfNumbers(line):
    i = 0
    result = []
    while i < len(line):
        col = ""
        while line[i] in numbers:
            col = col + str(i)
            i += 1
        if col != "":
            result.append(col)
        i += 1
    return result


#idxs is the list of indexes where a digit occur. We want to use these numbers as indexes for the line.
#To extract the value at that position.
def extractNumber(idxs, line):
    number = ""
    for i in range(len(idxs)):
        number = number + line[int(idxs[i])]
    return number


def main():
    lines = []
    positions = []
    numbers = []
    row = 0
    for line in file.readlines():
        line = line.replace("\n", "")

        #returns a list of strings. Where each string represent the index where a digit occur.
        col = findPositionOfNumbers(line)

        #chech each string in the list of strings that occur this row.
        for idxs in col:
            nr = extractNumber(idxs, line)
            numbers.append(nr)

        #create list of tuples, where tuple[0] is the row, and tuple[1] is the list of strings 
        #representing the indexes where digits occur.
        if col != []:
            positions.append((str(row),col))

        lines.append(line)
        row += 1

    print(lines)
    print(numbers)
    print(positions)


if __name__ == "__main__":
    main()