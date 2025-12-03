import sys

DAY = "02"

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt"):
    part1Answer = part1(path)
    part2Answer = part2(path)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

    return 0

# sum invalid ids within ranges
# an id is invalid if it contains the same repeated sequence
# ex: 11 and 5454 are invalid, but 101 is fine
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
            if(not isValidIdPart1(id)):
                sumOfInvalidIds += id

    return sumOfInvalidIds

# now any repeated sequence is invalid
def part2(inputPath, debug=0):
    with open(inputPath) as inFile:
        input = inFile.read()

    bands = input.split(",")    

    sumOfInvalidIds = 0

    # check values within each range   
    for band in bands:
        low, high = band.split("-")
        low = int(low); high = int(high)

        for id in range(low, high + 1):
            if(not isValidIdPart2(id)):
                sumOfInvalidIds += id

    return sumOfInvalidIds

def isValidIdPart1(id: int) -> bool:
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

def isValidIdPart2(id: int) -> bool:
    strId = str(id)
    idLen = len(strId)

    maxSeqLen = idLen // 2
    for seqLen in range(1, maxSeqLen + 1):
        seq = strId[:seqLen]
        seqRepeats: bool = True

        for testSeqIdx in range(seqLen, idLen, seqLen):
            if(seq != strId[testSeqIdx:testSeqIdx + seqLen]):
                seqRepeats = False

        if(seqRepeats):
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