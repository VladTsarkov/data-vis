import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QVBoxLayout
import app_1st
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5,heigh=4, dpi=100):
        fig = Figure(figsize=(width,heigh),dpi=dpi)
        self.axes = fig.add_subplot(111)
        #self.plt = plt
        super(MplCanvas,self).__init__(fig)

class ExampleApp(QtWidgets.QMainWindow, app_1st.Ui_MainWindow):
    def __init__(self):
    #def __init__(self,*args,**kwargs):
        super().__init__()
        self.setupUi(self)
        #super(ExampleApp,self).__init__(*args,**kwargs)

        #print(self.tab.isActiveWindow())
        #self.tab.insertAction(self.test,self.tab.isActiveWindow())
        #self.tab.insertAction(self.tab.isActiveWindow()==False,self.tab.isActiveWindow()==True)
        '''self.pushButton1 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton1.setGeometry(QtCore.QRect(110, 160, 89, 25))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setText("P123ushButton")'''

        self.lab1()
        self.lab3()
        self.lab2()
        self.lab4()
        self.lab5()


    def lab1(self):
        sc = MplCanvas(self, width=5, heigh=4,dpi=100)
        x1 = [1,2,3,4,5]
        y1 = [5,4,3,2,1]

        x = [1,2,3,4,5]
        y = [i*i for i in x]
        sc.axes.grid()
        x3 = [1,2,3,4,5]
        y3 = [10,5,13,18,2]
        sc.axes.plot(x,y,"r--",x3,y3,"y")
        sc.axes.plot(x1,y1,linewidth=5)

        layout = QVBoxLayout()
        layout.addWidget(sc)
        self.tab.setLayout(layout)

    def lab2(self):
        sc = MplCanvas(self, width=5, heigh=4,dpi=100)
        x = ['Ольга','Максим','Владимир','Евгений','Наталья']
        y = [random.randint(0,20) for i in range(5)]
        sc.axes.bar(x,y)
        sc2 = MplCanvas(self, width=5, heigh=4,dpi=100)
        sc2.axes.barh(x,y)
        layout = QVBoxLayout()
        layout.addWidget(sc)
        layout.addWidget(sc2)
        self.tab_2.setLayout(layout)

    def lab3(self):
        sc = MplCanvas(self, width=5, heigh=4,dpi=100)

        x = np.arange(0,720,10)
        y = np.sin(np.radians(x))
        sc.axes.grid(True)
        for i in range(len(y)):
            if y[i] == -1:
                sc.axes.annotate('min',xy=(x[i],y[i]),xycoords='data',
                    xytext=(x[i],y[i]+0.5),textcoords='data',arrowprops=dict(facecolor='g'))
            if y[i] == 1:
                sc.axes.annotate('max',xy=(x[i],y[i]),xycoords='data',
                    xytext=(x[i],y[i]-0.5),textcoords='data',arrowprops=dict(facecolor='r'))
        sc.axes.plot(x,y)
        layout = QVBoxLayout()
        layout.addWidget(sc)
        self.tab_3.setLayout(layout)

    def lab4(self):
        sc = MplCanvas(self, width=5, heigh=4,dpi=100)
        sc2 = MplCanvas(self, width=5, heigh=4,dpi=100)
        val = [17,3,77,35]
        label = ['Маша','Саша','Даша','Петя']
        sc.axes.pie(val,labels=label)
        #plt.pie(val,labels=label)
        sc2.axes.pie(val,labels=label,wedgeprops=dict(width=0.5))
        #plt.pie(val,labels=label,wedgeprops=dict(width=0.5))
        layout = QVBoxLayout()
        layout.addWidget(sc)
        layout.addWidget(sc2)
        self.tab_4.setLayout(layout)

    def lab5(self):
        self.canvas = MplCanvas(self, width=5, heigh=4,dpi=100)
        #self.setCentralWidget(self.canvas)
        self.frame = 0
        self.xdata = np.linspace(0,5,2000)
        self.ydata = np.sin(2*np.pi*(self.xdata-0.01*self.frame))
        #ln.set_data(xdata, ydata)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.tab_5.setLayout(layout)

        #self.setCentralWidget(self.tab_5)
        self.update_plot()
        self.show()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        if self.tab_5.isVisible():
            self.frame += 1
            if self.frame >200:
                self.frame = 0
            self.ydata = np.sin(2*np.pi*(self.xdata-0.01*self.frame))
            self.canvas.axes.cla()
            self.canvas.axes.plot(self.xdata,self.ydata)
            self.canvas.draw()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
