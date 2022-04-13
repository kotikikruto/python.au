import sys
from math import sqrt
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

num = 0
newNum = 0
sumIt = 0
sumAll = 0
operator = ""

opVar = False


class Calc(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.line = QLineEdit(self)
        self.line.move(20, 20)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(30)
        self.line.setFont(font)
        self.line.resize(590, 70)

        zero = QPushButton("0", self)
        zero.move(20, 430)
        zero.resize(110, 70)

        one = QPushButton("1", self)
        one.move(20, 350)
        one.resize(110, 70)

        two = QPushButton("2", self)
        two.move(140, 350)
        two.resize(110, 70)

        three = QPushButton("3", self)
        three.move(260, 350)
        three.resize(110, 70)

        four = QPushButton("4", self)
        four.move(20, 270)
        four.resize(110, 70)

        five = QPushButton("5", self)
        five.move(140, 270)
        five.resize(110, 70)

        six = QPushButton("6", self)
        six.move(260, 270)
        six.resize(110, 70)

        seven = QPushButton("7", self)
        seven.move(20, 190)
        seven.resize(110, 70)

        eight = QPushButton("8", self)
        eight.move(140, 190)
        eight.resize(110, 70)

        nine = QPushButton("9", self)
        nine.move(260, 190)
        nine.resize(110, 70)

        equals = QPushButton("=", self)
        equals.move(140, 430)
        equals.resize(230, 70)
        equals.clicked.connect(self.Equal)

        plus = QPushButton("+", self)
        plus.move(380, 190)
        plus.resize(110, 70)

        minus = QPushButton("-", self)
        minus.move(380, 270)
        minus.resize(110, 70)

        multiply = QPushButton("*", self)
        multiply.move(380, 350)
        multiply.resize(110, 70)

        divide = QPushButton("/", self)
        divide.move(380, 430)
        divide.resize(110, 70)

        switch = QPushButton("+/-", self)
        switch.move(500, 190)
        switch.resize(110, 70)
        switch.clicked.connect(self.Switch)

        squared = QPushButton("x²", self)
        squared.move(500, 270)
        squared.resize(110, 70)
        squared.clicked.connect(self.Squared)

        root = QPushButton("√", self)
        root.move(500, 350)
        root.resize(110, 70)
        root.clicked.connect(self.Root)

        point = QPushButton(".", self)
        point.move(500, 430)
        point.resize(110, 70)
        point.clicked.connect(self.Point)

        ce = QPushButton("CE", self)
        ce.move(20, 110)
        ce.resize(290, 70)
        ce.clicked.connect(self.CE)

        c = QPushButton("C", self)
        c.move(320, 110)
        c.resize(290, 70)
        c.clicked.connect(self.C)

        nums = [zero, one, two, three, four, five, six, seven, eight, nine]

        operators = [ce, c, plus, minus, multiply, divide, equals]

        others = [switch, squared, root, point]

        for i in nums:
            i.setStyleSheet("color:black;")
            i.clicked.connect(self.Num)

        for i in operators:
            i.setStyleSheet("color:black;")
        for i in operators[2:]:
            i.clicked.connect(self.operator)
        for i in others:
            i.setStyleSheet("color:black;")

        # Window Settings

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Calculator")
        self.setFixedSize(630, 550)
        self.show()

    def Num(self):
        global num
        global newNum
        global opVar

        sender = self.sender()

        newNum = int(sender.text())
        setNum = str(newNum)

        if opVar == False:
            self.line.setText(self.line.text() + setNum)
        else:
            self.line.setText(setNum)
            opVar = False

    def operator(self):
        global sumIt
        global num
        global opVar
        global operator

        sumIt += 1

        if sumIt > 1:
            self.Equal()

        num = self.line.text()
        sender = self.sender()
        operator = sender.text()

        opVar = True

    def Equal(self):
        global sumIt
        global sumAll
        global num
        global newNum
        global operator
        global opVar

        sumIt = 0

        newNum = self.line.text()

        if operator == "+":
            sumAll = float(num) + float(newNum)
        elif operator == "-":
            sumAll = float(num) - float(newNum)
        elif operator == "*":
            sumAll = float(num) * float(newNum)
        elif operator == "/":
            sumAll = float(num) / float(newNum)

        self.line.setText(str(sumAll))
        opVar = True

    def Root(self):
        global num

        num = float(self.line.text())
        num = sqrt(num)
        self.line.setText(str(num))

    def Squared(self):
        global num

        num = float(self.line.text())
        num = num ** 2
        self.line.setText(str(num))

    def Point(self):

        if "." not in self.line.text():
            self.line.setText(self.line.text() + ".")

    def Switch(self):
        global num

        num = float(self.line.text())
        num = -num
        self.line.setText(str(num))

    def CE(self):
        self.line.backspace()

    def C(self):
        global num
        global newNum
        global sumAll
        global operator

        self.line.clear()

        num = 0
        newNum = 0
        sumAll = 0
        operator = ""


def main():
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
