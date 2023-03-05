from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
from math import sin, cos, tan


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.exp = ''
        self.answer = 0
        self.setWindowTitle('Calculator')
        self.setGeometry(1000, 1000, 600, 300)

        self.button0 = QPushButton(self)
        self.button0.setText("0")
        self.button0.clicked.connect(self.pbutton0)
        self.button0.move(100, 100)

        self.button1 = QPushButton(self)
        self.button1.setText("1")
        self.button1.clicked.connect(self.pbutton1)
        self.button1.move(200, 100)

        self.button2 = QPushButton(self)
        self.button2.setText("2")
        self.button2.clicked.connect(self.pbutton2)
        self.button2.move(300, 100)

        self.button3 = QPushButton(self)
        self.button3.setText("3")
        self.button3.clicked.connect(self.pbutton3)
        self.button3.move(100, 150)

        self.button4 = QPushButton(self)
        self.button4.setText("4")
        self.button4.clicked.connect(self.pbutton4)
        self.button4.move(200, 150)

        self.button5 = QPushButton(self)
        self.button5.setText("5")
        self.button5.clicked.connect(self.pbutton5)
        self.button5.move(300, 150)

        self.button6 = QPushButton(self)
        self.button6.setText("6")
        self.button6.clicked.connect(self.pbutton6)
        self.button6.move(100, 200)

        self.button7 = QPushButton(self)
        self.button7.setText("7")
        self.button7.clicked.connect(self.pbutton7)
        self.button7.move(200, 200)

        self.button8 = QPushButton(self)
        self.button8.setText("8")
        self.button8.clicked.connect(self.pbutton8)
        self.button8.move(300, 200)

        self.button9 = QPushButton(self)
        self.button9.setText("9")
        self.button9.clicked.connect(self.pbutton9)
        self.button9.move(200, 250)

        self.button_plus = QPushButton(self)
        self.button_plus.setText("+")
        self.button_plus.move(400, 150)
        self.button_plus.clicked.connect(self.plusbutton)

        self.button_minus = QPushButton(self)
        self.button_minus.setText("-")
        self.button_minus.move(400, 200)
        self.button_minus.clicked.connect(self.minusbutton)

        self.button_multi = QPushButton(self)
        self.button_multi.setText("*")
        self.button_multi.move(500, 100)
        self.button_multi.clicked.connect(self.multibutton)

        self.button_div = QPushButton(self)
        self.button_div.setText("/")
        self.button_div.move(500, 150)
        self.button_div.clicked.connect(self.divbutton)

        self.button_mod = QPushButton(self)
        self.button_mod.setText("%")
        self.button_mod.move(500, 200)
        self.button_mod.clicked.connect(self.modbutton)

        self.button_equ = QPushButton(self)
        self.button_equ.setText("=")
        self.button_equ.move(400, 250)
        self.button_equ.clicked.connect(self.equbutton)

        self.button_del = QPushButton(self)
        self.button_del.setText("del")
        self.button_del.move(400, 100)
        self.button_del.clicked.connect(self.delbutton)

        self.button_clean = QPushButton(self)
        self.button_clean.setText("clean")
        self.button_clean.clicked.connect(self.cleanbutton)
        self.button_clean.move(500, 250)

        self.button_sin = QPushButton(self)
        self.button_sin.setText('sin(x)')
        self.button_sin.clicked.connect(self.sinbutton)
        self.button_sin.move(0, 100)

        self.button_cos = QPushButton(self)
        self.button_cos.setText('cos(x)')
        self.button_cos.clicked.connect(self.cosbutton)
        self.button_cos.move(0, 150)

        self.button_tg = QPushButton(self)
        self.button_tg.setText('tg(x)')
        self.button_tg.clicked.connect(self.tgbutton)
        self.button_tg.move(0, 200)

        self.button_ctg = QPushButton(self)
        self.button_ctg.setText('ctg(x)')
        self.button_ctg.clicked.connect(self.ctgbutton)
        self.button_ctg.move(0, 250)

        self.button_sqrt = QPushButton(self)
        self.button_sqrt.setText('sqrt(x)')
        self.button_sqrt.clicked.connect(self.sqrtbutton)
        self.button_sqrt.move(100, 250)

        self.button_sqr = QPushButton(self)
        self.button_sqr.setText('sqr(x)')
        self.button_sqr.clicked.connect(self.sqrbutton)
        self.button_sqr.move(300, 250)

        self.label = QLabel(self)
        self.label.setGeometry(0, 50, 500, 20)


    def pbutton0(self):
        self.label.setText(self.label.text() + self.button0.text())


    def plusbutton(self):
        self.answer = float(self.label.text())
        self.exp = "plus"
        self.label.clear()


    def minusbutton(self):
        self.answer = float(self.label.text())
        self.exp = "minus"
        self.label.clear()


    def multibutton(self):
        self.answer = float(self.label.text())
        self.exp = "multi"
        self.label.clear()


    def divbutton(self):
        self.answer = float(self.label.text())
        self.exp = "div"
        self.label.clear()


    def cleanbutton(self):
        self.label.clear()


    def delbutton(self):
        self.label.setText(self.label.text()[:-1])


    def modbutton(self):
        self.answer = float(self.label.text())
        self.exp = "mod"
        self.label.clear()


    def sqrtbutton(self):
        self.answer = float(self.label.text()) ** 0.5
        self.label.setText(str(self.answer))


    def sqrbutton(self):
        self.answer = float(self.label.text()) ** 2
        self.label.setText(str(self.answer))


    def sinbutton(self):
        if self.label.text():
            self.answer = sin(float(self.label.text()))
        self.label.setText(str(self.answer))


    def cosbutton(self):
        self.answer = cos(float(self.label.text()))
        self.label.setText(str(self.answer))


    def tgbutton(self):
        self.answer = tan(float(self.label.text()))
        self.label.setText(str(self.answer))


    def ctgbutton(self):
        self.answer = 1 / tan(float(self.label.text()))
        self.label.setText(str(self.answer))


    def equbutton(self):
        if self.exp == 'plus':
            self.answer += float(self.label.text())
            self.label.setText(str(self.answer))
        elif self.exp == 'minus':
            self.answer -= float(self.label.text())
            self.label.setText(str(self.answer))
        elif self.exp == 'multi':
            self.answer *= float(self.label.text())
            self.label.setText(str(self.answer))
        elif self.exp == 'div':
            self.answer /= float(self.label.text())
            self.label.setText(str(self.answer))
        elif self.exp == 'mod':
            self.answer = self.answer % float(self.label.text())
            self.label.setText(str(self.answer))


    def pbutton1(self):
        self.label.setText(self.label.text() + self.button1.text())


    def pbutton2(self):
        self.label.setText(self.label.text() + self.button2.text())


    def pbutton3(self):
        self.label.setText(self.label.text() + self.button3.text())


    def pbutton4(self):
        self.label.setText(self.label.text() + self.button4.text())


    def pbutton5(self):
        self.label.setText(self.label.text() + self.button5.text())


    def pbutton6(self):
        self.label.setText(self.label.text() + self.button6.text())


    def pbutton7(self):
        self.label.setText(self.label.text() + self.button7.text())


    def pbutton8(self):
        self.label.setText(self.label.text() + self.button8.text())


    def pbutton9(self):
        self.label.setText(self.label.text() + self.button9.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())