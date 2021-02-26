import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtWidgets, QtCore


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        layout = QtWidgets.QGridLayout()
        pushButton1 = QtWidgets.QPushButton()
        #pushButton1.setGeometry(QtCore.QRect(110, 160, 89, 25))
        pushButton1.setObjectName("pushButton1")
        pushButton1.setText("Кнопка")

        self.checkBox = QtWidgets.QCheckBox('QCheckBox',self)
        self.checkBox.toggle()
        self.checkBox.stateChanged.connect(self.changeTitle)

        #checkBox.move(20,20)
        #checkbox.setGeometry(QtCore.QRect(100, 100, 100, 100))

        comboBox = QtWidgets.QComboBox()
        #comboBox.setGeometry(QtCore.QRect(100, 100, 100, 100))
        #comboBox.move(20,450)
        comboBox.insertItem(0,"Выпадающий список")
        comboBox.insertItem(1,"КомбоБокс")

        scrollBar = QtWidgets.QScrollBar()
        #scrollBar.insertItem(0,'shit')
        #scrollBar.move(20,100)

        textEdit = QtWidgets.QTextEdit()
        buttonLabel = QtWidgets.QLabel('QPushButton')
        checkBoxLabel = QtWidgets.QLabel('QCheckBox')
        comboBoxLabel = QtWidgets.QLabel('QComboBox')
        scrollBarLabel = QtWidgets.QLabel('QScrollBar')
        textEditLabel = QtWidgets.QLabel('QTextEdit')

        layout.addWidget(buttonLabel, 1, 0)
        layout.addWidget(pushButton1, 1, 1)

        layout.addWidget(self.checkBox, 2, 1)
        layout.addWidget(checkBoxLabel, 2, 0)

        layout.addWidget(comboBox, 3, 1)
        layout.addWidget(comboBoxLabel, 3, 0)

        layout.addWidget(scrollBar, 4, 1)
        layout.addWidget(scrollBarLabel, 4, 0)

        layout.addWidget(textEdit, 6, 1)
        layout.addWidget(textEditLabel, 6, 0)

        lineEdit = QtWidgets.QLineEdit()
        textlineEdit = QtWidgets.QLabel('QLineEdit')
        layout.addWidget(textlineEdit,7,0)
        layout.addWidget(lineEdit,7,1)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        #slider.setGeometry(30,40,100,40)
        self.textSlider2 = QtWidgets.QLabel("Work")
        self.slider.valueChanged[int].connect(self.changeValue)
        self.textSlider = QtWidgets.QLabel("QSlider")
        '''pixmap = QtWidgets.QLabel()
        pixmap.setPixmap(QPixmap('max.png'))
        pixmap.setGeometry(40,40,40,40)'''
        layout.addWidget(self.textSlider,8,0)
        layout.addWidget(self.slider, 8,1)
        layout.addWidget(self.textSlider2, 8,2)
        #layout.addWidget(pixmap,8,2)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)

        self.buttonPB = QPushButton('Start', self)
        self.buttonPB.move(40, 80)
        self.buttonPB.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        #self.show()
        self.textProgressBar = QtWidgets.QLabel('Qlabel')
        '''progressBar = QtWidgets.QProgressBar()
        buttonPB = QtWidgets.QPushButton('Старт')
        buttonPB.clicked.connect(doAction)
        timer = QtCore.QBasicTimer()
        step = 0'''
        layout.addWidget(self.textProgressBar,9,0)
        layout.addWidget(self.progressBar,9,1)
        layout.addWidget(self.buttonPB,9,2)

        layout.setSpacing(20)
        self.w = QtWidgets.QWidget()
        self.w.setLayout(layout)

        self.mw = QtWidgets.QScrollArea()
        self.mw.setWindowTitle("Это виджет QScrollArea")
        self.mw.setWidget(self.w)
        self.mw.resize(200, 200)
        self.mw.show()


    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.buttonPB.setText('Finished')
            return

        self.step = self.step + 1
        self.progressBar.setValue(self.step)


    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.buttonPB.setText('Start')
        else:
            self.timer.start(100, self)
            self.buttonPB.setText('Stop')
            
    def changeValue(self, value):
        self.textSlider2.setText(str(value))

    def changeTitle(self,state):
        if state == QtCore.Qt.Checked:
            self.checkBox.setText('Отмечено')
        else:
            self.checkBox.setText('Не отмечено')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
