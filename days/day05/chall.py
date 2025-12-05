import sys

DAY = "05"

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt", debug=0):
    part1Answer = part1(path, debug=debug)
    # part2Answer = parts(path, repeatUntilNoneCanBeRemoved=True, debug=debug)

    print(f"Part 1 Answer: {part1Answer}")
    # print(f"Part 2 Answer: {part2Answer}")

    return 0

def part1(inputPath, debug=0):
    with open(inputPath) as inFile:
        lines = inFile.read().splitlines()

    sepIdx = lines.index("")

    validRanges = [line.split("-") for line in lines[:sepIdx]]
    validRanges = list(map(lambda bounds: (int(bounds[0]), int(bounds[1])), validRanges))
    testIds = [int(line) for line in lines[sepIdx + 1:]]

    validIdCount = 0
    for testId in testIds:
        if(isValidIdPart1(validRanges, testId)):
            validIdCount += 1

    if(debug):
        print(lines)
        print(lines.index(""))
        print(validRanges)

    return validIdCount

def isValidIdPart1(validRanges, id):
    for low, high in validRanges:
        if(low < id <= high):
            return True
    
    return False

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main(f"../../inputs/day{DAY}/day{DAY}Test.txt")
        else:
            main()
    else:
        main()