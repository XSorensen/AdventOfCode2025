import sys

DAY = "02"

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt"):
    part1Answer = part1(path)
    part2Answer = part2(path)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

    return 0

# count number of times position ends on zero after a rotation
def part1(inputPath, debug=0):
    with open(inputPath) as inFile:
        input = inFile.read()

    bands = input.split(",")    

    sumOfInvalidIds = 0

    # check values within each range   
    for band in bands:
        low, high = band.split("-")
        low = int(low); high = int(high)

        for id in range(low, high + 1):
            if(not isValidId(id)):
                sumOfInvalidIds += id

    return sumOfInvalidIds

# count number of times the dial passes 0 as well as lands on it
def part2(inputPath, debug=0):
    pass

def isValidId(id: int):
    strId = str(id)

    idLen = len(strId)
    
    # check if string is two repeated sequences
    # only occurs if string has an even length
    if(idLen % 2 == 0):                   
        lhs = strId[:idLen // 2]
        rhs = strId[idLen // 2 :]
        if(lhs == rhs):
            return False

    return True

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main(f"../../inputs/day{DAY}/day{DAY}Test.txt")
        else:
            main()
    else:
        main()