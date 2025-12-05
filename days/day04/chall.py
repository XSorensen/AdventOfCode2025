import sys

DAY = "04"

class CustomGrid():
    def __init__(self, grid):
        self.grid = grid

    def __getitem__(self, cord):
        x = cord[0]
        y = cord[1]

        if(x < 0 or x >= len(self.grid)):
            return '.'
        elif(y < 0 or y >= len(self.grid[0])):
            return '.'
        return self.grid[cord[0]][cord[1]]
    
    def __setitem__(self, cord, item):
        self.grid[cord[0]][cord[1]] = item

    def __str__(self):
        return "\n".join(["".join(row) for row in self.grid])

    def shape(self):
        return (len(self.grid), len(self.grid[0]))

def main(path=f"../../inputs/day{DAY}/day{DAY}.txt", debug=0):
    part1Answer = parts(path, debug=debug)
    part2Answer = parts(path, repeatUntilNoneCanBeRemoved=True, debug=debug)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

    return 0

def parts(inputPath, repeatUntilNoneCanBeRemoved=False, debug=0):
    with open(inputPath) as inFile:
        rows = inFile.read().splitlines()

    totalTargets = 0
    availableTargets = 0
    threshold = 4

    grid = CustomGrid([[col for col in row] for row in rows])
    if(debug):
        print(grid, end="\n\n\n\n")

    rows, cols = grid.shape()

    while(availableTargets > 0 or totalTargets == 0):
        availableTargets = 0       

        for x in range(rows):
            for y in range(cols):
                if(grid[(x,y)] != '@'):
                    continue

                if(getNumRollsAround(grid, x, y) < threshold):
                    availableTargets += 1
                    
                    if(repeatUntilNoneCanBeRemoved):
                        grid[(x, y)] = 'x'

        totalTargets += availableTargets

        if(not repeatUntilNoneCanBeRemoved):
            break

    # print(f"RowCount: {len(grid)} | ColCount: {len(grid[0])}")
    print(grid)

    return totalTargets

def getNumRollsAround(grid, x=0, y=0):
    cords = [
        (x-1,y-1),
        (x  ,y-1),
        (x+1,y-1),

        (x-1,y),
        (x+1,y),

        (x-1,y+1),
        (x  ,y+1),
        (x+1,y+1),
    ]

    count = len(list(filter(lambda cord: grid[cord] == '@', cords)))

    return count

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