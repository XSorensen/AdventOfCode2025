import sys

DAY = "04"

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
    
    if(debug):
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

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "test"):
            main(f"../../inputs/day{DAY}/day{DAY}Test.txt")
        else:
            main()
    else:
        main()