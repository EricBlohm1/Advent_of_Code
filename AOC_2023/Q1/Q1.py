
file = open("input.txt", "r")

#value of each element is index+1
text_digits = ["one","two","three","four","five","six","seven","eight","nine"]

def convert(line):
    lo = 0
    result = []
    while lo < len(line)-1:
        for i in range(0,9):
            digit = text_digits[i]
            substr = line[lo: lo+len(digit)]
            if digit == substr:
                #update first letter och the correct digit, with the numeric value. Will ruin the "text value"
                result.append(str(i+1))
            else:
                result.append(line[lo])
        lo += 1
    return result

values = []
def main():
    for line in file.readlines():
        conv = convert(line)
        #Extract all numbers from the line
        # this returns an iterator
        nums = filter(str.isdecimal, conv)

        #make it readable, join all numbers with an empty string. 
        s = "".join(nums)
        first = s[0]
        second = s[len(s)-1]
        # calibration value is the first and last number appended forming a 2 digit number.
        calibration_val = first + second

        #before summing the values, we have to convert each string to an int
        values.append(int(calibration_val))
    print(sum(values))
    #print(values)
    file.close()

if __name__ == "__main__":
    main()