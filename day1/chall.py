import sys

def main(path="./inputs/day1.txt"):
    part1Answer = part1(path)
    part2Answer = part2(path)

    print(f"Part 1 Answer: {part1Answer}")
    print(f"Part 2 Answer: {part2Answer}")

    return 0

# count number of times position ends on zero after a rotation
def part1(inputPath, debug=0):
    with open(inputPath) as inFile:
        lines = inFile.readlines()

    commands = [(line[0], int(line[1:])) for line in lines]

    currentPos = 50
    numZeros = 0
    numValidPWChars = 100

    for command in commands:
        direction, amount = command

        if(direction == 'L'):
            amount = -amount

        currentPos = (currentPos + amount) % numValidPWChars

        if(currentPos == 0):
            numZeros += 1

        if(debug):
            print(f"Rot: {direction} | Amt: {amount} | Pos: {currentPos}")

    return numZeros

# count number of times the dial passes 0 as well as lands on it
def part2(inputPath, debug=0):
    with open(inputPath) as inFile:
        lines = inFile.readlines()

    commands = [(line[0], int(line[1:])) for line in lines]

    currentPos = 50
    numZeros = 0
    numValidPWChars = 100

    for command in commands:
        direction, amount = command

        # determine how many full roations the dial will need before its final position is calculated
        timesRequriedToPassZero = amount // numValidPWChars

        # left reduces number
        if(direction == 'L'):
            amount = -amount

        prevPos = currentPos
        currentPos = (currentPos + amount) % numValidPWChars

        # underflow rotations touch zero only if they did not start on 0
        if(direction == 'L' and prevPos < currentPos and prevPos != 0 and currentPos != 0):
            timesRequriedToPassZero += 1
        # overflow rotation
        elif(direction == 'R' and prevPos > currentPos and currentPos != 0):
            timesRequriedToPassZero += 1
        numZeros += timesRequriedToPassZero

        # landed on 0
        if(currentPos == 0):
            numZeros += 1

        if(debug):
            print(f"Rot: {direction} | Amt: {amount:3} | Pos: {currentPos:2} | PassZero: {timesRequriedToPassZero:2} | NumZeros: {numZeros}")

    return numZeros

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main("./inputs/day1Test.txt")
        else:
            main()
    else:
        main()