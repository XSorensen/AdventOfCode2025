import sys

DAY = "05"

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt", debug=0):
    part1Answer = part1(path, debug=debug)
    part2Answer = part2(path, debug=debug)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

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

def part2(inputPath, debug=0):
    with open(inputPath) as inFile:
        lines = inFile.read().splitlines()

    sepIdx = lines.index("")

    validRanges = [line.split("-") for line in lines[:sepIdx]]
    validRanges = list(map(lambda bounds: (int(bounds[0]), int(bounds[1])), validRanges))

    numRangesMerged = 0
    firstItr = True
    # continually merges ranges until no ranges overlap
    while(numRangesMerged > 0 or firstItr):
        firstItr = False
        numRangesMerged = 0
        mergedRanges = []

        for bounds in validRanges:
            noneOverlap = True

            # attempt to merge valid range with any other merged range
            for i, mergedRange in enumerate(mergedRanges):
                if(rangesOverlap(mergedRange, bounds)):
                    newRange = mergeRanges(mergedRange, bounds)
                    mergedRanges[i] = newRange

                    numRangesMerged += 1
                    noneOverlap = False

                    if(debug):
                        print(f"lhs: {bounds} | rhs: {mergedRange} | Resulting: {newRange}")

                    break
            
            if(noneOverlap):
                mergedRanges.append(bounds)
        
        validRanges = mergedRanges
        if(debug):
            print(validRanges)
    
    if(debug):
        print(mergedRanges)

    return sum(map(lambda bounds: bounds[1] - bounds[0] + 1, mergedRanges))

def isValidIdPart1(validRanges, id):
    for low, high in validRanges:
        if(low < id <= high):
            return True
    
    return False

def rangesOverlap(range1, range2):
    l1, h1 = range1
    l2, h2 = range2

    if(l2 <= l1 <= h2):
        return True
    elif(l1 <= l2 <= h1):
        return True
    elif(l1 <= h2 <= h1):
        return True
    elif(l2 <= h1 <= h2):
        return True

    return False

def mergeRanges(range1, range2):
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main(f"../../inputs/day{DAY}/day{DAY}Test.txt")
        else:
            main()
    else:
        main()