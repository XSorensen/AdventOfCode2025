import sys

DAY = "03"

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt"):
    part1Answer = part1(path)
    part2Answer = part2(path)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

    return 0

def part1(inputPath, debug=0):
    with open(inputPath) as inFile:
        batteries = inFile.read().splitlines()

    totalJoltage = 0
    for battery in batteries:
        totalJoltage += getMaxJoltage(battery)

    return totalJoltage

def part2(inputPath, debug=0):
    with open(inputPath) as inFile:
        input = inFile.read()

def getMaxJoltage(battery):
    maxVal: int = 0
    maxIdx: int = -1

    # final num must be reserved to be the second number
    for i in range(len(battery) - 1):
        # print(battery[i])
        joltage = int(battery[i])
        if(joltage > maxVal):
            maxVal = joltage
            maxIdx = i

    firstNum = maxVal
    maxVal = 0
    for i in range(maxIdx + 1, len(battery)):
        joltage = int(battery[i])
        if(joltage > maxVal):
            maxVal = joltage

    retVal = int(f"{firstNum}{maxVal}")

    # print(f"{battery}\n\tMax Joltage: {retVal} | Max Idx: {maxIdx}")

    return retVal

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main(f"../../inputs/day{DAY}/day{DAY}Test.txt")
        else:
            main()
    else:
        main()