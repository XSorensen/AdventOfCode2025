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
        totalJoltage += getMaxJoltagePart1(battery)

    return totalJoltage

def part2(inputPath, debug=0):
    with open(inputPath) as inFile:
        batteries = inFile.read().splitlines()

    totalJoltage = 0
    for battery in batteries:
        totalJoltage += getMaxJoltagePart2(battery)

    return totalJoltage

# select two digits from the battery, digit 1 must appear before digit 2, that result in the highest concatenated numeric value
def getMaxJoltagePart1(battery):
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

# select 12 digits from the battery whose value when the digits are concatenated is maximized
# digits must appear in the same relative ordering as they appeard in the original battery
def getMaxJoltagePart2(battery):
    maxVal: int = 0
    maxIdx: int = -1

    batLen = len(battery)
    numRemainingToTurnOn = 12
    joltages = []
    for numRemainingToTurnOn in range(12, 0, -1):
        maxVal = 0
        for i in range(maxIdx + 1, batLen - numRemainingToTurnOn + 1):
            joltage = int(battery[i])
            if(joltage > maxVal):
                maxVal = joltage
                maxIdx = i
            numRemainingToTurnOn -= 1
        joltages.append(str(maxVal))

    retVal = int("".join(joltages))
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