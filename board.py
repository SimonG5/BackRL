RED = 1
BLACK = 0

class Board:
    def __init__(self):
        self.outputMapping = {}
        count = 0
        with open("labels/labels.txt") as file:
            for line in file:
                self.outputMapping[count] = line.strip('\n')
                count += 1

        self.points = [0] * 24

        self.points[0] = 2
        self.points[5] = -5
        self.points[7] = -3
        self.points[11] = 5
        self.points[12] = -5
        self.points[16] = 3
        self.points[18] = 5
        self.points[23] = -2

        self.homeCheckers = [0] * 2
        self.barCheckers = [0] * 2

    def printBoard(self):
        returnString = ""
        for i in range(12, 24):
            occupiedColor = "BLACK"
            if self.points[i] < 0:
                occupiedColor = "RED"

            if self.points[i] == 0:
                returnString += " "
            elif occupiedColor == "BLACK":
                returnString += "B"
            else:
                returnString += "R"

            if i == 17:
                returnString += " | "
            else:
                returnString += " "
        returnString += "\n"
        for i in range(12, 24):
            returnString += str(abs(self.points[i]))
            if i == 17:
                returnString += " | "
            else:
                returnString += " "
        returnString += "\n"
        returnString += "\n"
        for i in range(11, -1, -1):
            returnString += str(abs(self.points[i]))
            if i == 6:
                returnString += " | "
            else:
                returnString += " "
        returnString += "\n"
        for i in range(11, -1, -1):
            occupiedColor = "BLACK"
            if self.points[i] < 0:
                occupiedColor = "RED"

            if self.points[i] == 0:
                returnString += " "
            elif occupiedColor == "BLACK":
                returnString += "B"
            else:
                returnString += "R"

            if i == 6:
                returnString += " | "
            else:
                returnString += " "

        returnString += "\n"
        returnString += "HR" + \
            str(self.homeCheckers[0]) + "   " + "HB" + \
            str(self.homeCheckers[1]) + "   "
        returnString += "BR" + \
            str(self.barCheckers[0]) + "   " + "BB" + str(self.barCheckers[1])
        returnString += "\n"
        print(returnString)

    def addCheckerToPoint(self, playerColor, move):
        if move == "Cannot/Move":
            return

        moveFormat = move.split("/")
        if moveFormat[0] == "bar":
            fromType = "BAR"
            fromPoint = 0
        else:
            fromType = "NORMAL"
            fromPoint = int(moveFormat[0])

        if moveFormat[1] == "off":
            toPoint = 0
            toType = "OFF"
        else:
            toPoint = int(moveFormat[1])
            toType = "NORMAL"

        if playerColor == BLACK:
            fromPoint = abs(fromPoint - 25)
            toPoint = abs(toPoint - 25)

        fromPoint -= 1
        toPoint -= 1

        if fromType == "BAR":
            if playerColor == RED:
                self.barCheckers[0] -= 1
            else:
                self.barCheckers[1] -= 1
        else:
            if playerColor == RED:
                self.points[fromPoint] += 1
            else:
                self.points[fromPoint] -= 1

        if toType == "OFF":
            if playerColor == RED:
                self.homeCheckers[0] += 1
            else:
                self.homeCheckers[1] += 1
        elif ((self.points[toPoint] > 0 and playerColor == RED) or (self.points[toPoint] < 0 and playerColor == BLACK)):
            if playerColor == RED:
                self.points[toPoint] = -1
            else:
                self.points[toPoint] = 1
            if playerColor == RED:
                hitIndex = 1
            else:
                hitIndex = 0
            self.barCheckers[hitIndex] += 1
        else:
            if playerColor == RED:
                self.points[toPoint] -= 1
            else:
                self.points[toPoint] += 1

    def isValidMove(self,color, move):
        moveFormat = move.split("/")
        if moveFormat[0] == "bar":
            fromType = "BAR"
            fromPoint = 0
        else:
            fromType = "NORMAL"
            fromPoint = int(moveFormat[0])

        if moveFormat[1] == "off":
            toPoint = 0
            toType = "OFF"
        else:
            toPoint = int(moveFormat[1])
            toType = "NORMAL"

        return True

    def isGameOver(self):
        if self.homeCheckers[0] == 15:
            return 1
        if self.homeCheckers[1] == 15:
            return -1
        return 0
