import sys
from operator import add, sub, mul, truediv
from PyQt5 import QtWidgets
from ui import Ui_MainWindow
from PyQt5.QtGui import QIcon

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Калькулятор')
        self.setWindowIcon(QIcon('Calculator_30001.png'))
        self.ui.lineEdit.setPlaceholderText('0')
        self.ui.PressButton_01.clicked.connect(lambda: self.calc_mode('1'))
        self.ui.PressButton_02.clicked.connect(lambda: self.calc_mode('2'))
        self.ui.PressButton_03.clicked.connect(lambda: self.calc_mode('3'))
        self.ui.PressButton_04.clicked.connect(lambda: self.calc_mode('4'))
        self.ui.PressButton_05.clicked.connect(lambda: self.calc_mode('5'))
        self.ui.PressButton_06.clicked.connect(lambda: self.calc_mode('6'))
        self.ui.PressButton_07.clicked.connect(lambda: self.calc_mode('7'))
        self.ui.PressButton_08.clicked.connect(lambda: self.calc_mode('8'))
        self.ui.PressButton_09.clicked.connect(lambda: self.calc_mode('9'))
        self.ui.PressButton_0.clicked.connect(lambda: self.calc_mode('0'))

        self.ui.PressButton_C.clicked.connect(self.clear_all)
        self.ui.PressButton_CE.clicked.connect(self.clear_entry)
        self.ui.PressButton_com.clicked.connect(self.add_comma)

        self.ui.PressButton_Eq.clicked.connect(self.calculate)
        self.ui.PressButton_sum.clicked.connect(lambda: self.math_operation('+'))
        self.ui.PressButton_sub.clicked.connect(lambda: self.math_operation('-'))
        self.ui.PressButton_X.clicked.connect(lambda: self.math_operation('*'))
        self.ui.PressButton_div.clicked.connect(lambda: self.math_operation('/'))

    def calc_mode(self, btn_digit):
        if self.ui.lineEdit.text() == '0':
            self.ui.lineEdit.setText(btn_digit)
        else:
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + btn_digit)
    def clear_all(self):
        self.ui.lineEdit.setText('0')
        self.ui.label.clear()
    def clear_entry(self):
        self.ui.lineEdit.setText('0')
    def add_comma(self):
        if '.' not in self.ui.lineEdit.text():
            self.ui.lineEdit.setText(self.ui.lineEdit.text() + '.')
    @staticmethod
    def remove_zero(num):
        n = str(float(num))
        return n[:-2] if n[-2:] == '.0' else n
    def add_temp(self, math_sign: str):
        if not self.ui.label.text() or self.get_math_sign() == '=':
            self.ui.label.setText(self.remove_zero(self.ui.lineEdit.text()) + f' {math_sign} ')
            self.ui.lineEdit.setText('0')
    def get_entry_num(self):
        entry = self.ui.lineEdit.text().strip('.')
        if '.' in entry:
            return float(entry)
        else:
            return int(entry)

    def get_temp_num(self):
        if self.ui.label.text():
            temp = self.ui.label.text().strip('.').split()[0]
            if '.' in temp:
                return float(temp)
            else:
                return int(temp)

    def get_math_sign(self):
        if self.ui.label.text():
            return self.ui.label.text().strip('.').split()[-1]
    def calculate(self):
        entry = self.ui.lineEdit.text()
        temp = self.ui.label.text()
        if temp:
            result = self.remove_zero(
                str(operations[self.get_math_sign()](self.get_temp_num(), self.get_entry_num()))
                )
            self.ui.label.setText(temp + self.remove_zero(entry) + ' =')
            self.ui.lineEdit.setText(result)
            return result
    def math_operation(self, math_sign):
        temp = self.ui.label.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math_sign() != math_sign:
                if self.get_math_sign() == '=':
                    self.add_temp(math_sign)
                else:
                    self.ui.label.setText(temp[:-2] + f'{math_sign} ')
            else:
                self.ui.label.setText(self.calculate() + f' {math_sign}')

app = QtWidgets.QApplication([])
application = Calculator()
application.show()
sys.exit(app.exec())