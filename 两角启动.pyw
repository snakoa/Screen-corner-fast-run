
import sys
import os
from turtle import width
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QSystemTrayIcon,QAction,QMenu,QApplication,QPushButton,QVBoxLayout,QLineEdit,QFileDialog,QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.Qt import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt
from win32.win32api import GetSystemMetrics

width=GetSystemMetrics (0)
#print(object) #<class 'object'>
def quitAppQ(): #有确认窗口
    w.show() # w.hide() #隐藏
    QCoreApplication.instance().quit() #关闭窗体程序
    tp.setVisible(False)

class Ui_Form(object):
    def setupUi(self, w):
        #窗口
        w.setObjectName("w")
        w.setWindowTitle("左上角启动")
        w.resize(3, 3) #大小
        w.move(0,0) #位置
        w.setStyleSheet('background-color:skyblue')
        w.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        w.setWindowOpacity(0.01) #不能设置为0 不然不生效


        #按钮1
        self.pushButton = QtWidgets.QPushButton(w)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.pushButton.setObjectName("pushButton")
        #self.retranslateUi(w)
        #点击按钮信号传送到打开文件夹函数
        self.pushButton.clicked.connect(self.openfolder)
        #QtCore.QMetaObject.connectSlotsByName(w)
        self.child_window = Child()
        self.child_window.show()

    #统一设置名称
    def retranslateUi(self, w):
        self.pushButton.setText("打开文件夹")
        # _translate = QtCore.QCoreApplication.translate
        # w.setWindowTitle(_translate("w", "左上角启动")) 
        # w.pushButton.setText(_translate("w", "打开文件夹")) #按钮显示内容

    #打开文件夹
    def openfolder(self,w):
        import os
        atxt = open('a.txt',"r+")
        atxt1=atxt.readlines() #必须是ANSI格式
        folder = atxt1[0]
        os.system("start explorer %s" %folder)
        # 方法2：通过startfile
        #os.startfile(folder)



def act(reason):
    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    if (reason == 3 ): 
        w.show()
    elif (reason==1 ):
        w.show()


class Child(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("子窗口")
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        Childw=2
        self.resize(Childw, Childw) #大小
        self.move(width-Childw+1,0) #位置
        #按钮2
        self.btn2 = QtWidgets.QPushButton(self)
        self.btn2.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.btn2.setObjectName("btn2")
        #self.retranslateUi(w)
        #点击按钮信号传送到打开文件夹函数
        self.setWindowOpacity(0.01)
        self.btn2.clicked.connect(self.openfolder2)
        QtCore.QMetaObject.connectSlotsByName(w)
    def openfolder2(self):
        import os
        atxt = open('a.txt',"r+")
        atxt1=atxt.readlines() #必须是ANSI格式
        folder = atxt1[1] #打开位置即系统上一次打开位置
        print(atxt1[1])
        os.system("start explorer %s" %folder)
        # 方法2：通过startfile
        #os.startfile(folder)


class shezhi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置")
        self.resize(400, 200)
        self.cwd = os.getcwd()
         # btn 1
        self.btn_chooseDir = QPushButton(self)  
        self.btn_chooseDir.setObjectName("btn_chooseDir")  
        self.btn_chooseDir.setText("左上")
        self.btn_chooseDir.setGeometry(20,20,40,20)

        # btn 2
        self.btn2 = QPushButton(self)  
        self.btn2.setObjectName("btn2")  
        self.btn2.setText("右上")
        self.btn2.setGeometry(20,40,40,20)

        #文件夹选择
        layout = QVBoxLayout()
        layout.addWidget(self.btn_chooseDir)
        self.btn_chooseDir.clicked.connect(self.btn1_chooseDir)
        layout.addWidget(self.btn2)
        self.btn2.clicked.connect(self.btn2_chooseDir)

        # 文本输入框
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(75, 20, 200, 20)
        self.line_edit.setText(atxt1[0])

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setGeometry(75, 40, 200, 20)
        self.line_edit1.setText(atxt1[1]) #末尾附带1空格


    def btn1_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "请为左上选择一个文件夹位置",self.cwd) # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(dir_choose)
        self.line_edit.setText(dir_choose)
        #atxt = open('a.txt',"w+")
        #atxt1=atxt.readlines()
        #atxt1[0]=str(dir_choose)
        atxt = open('a.txt',"r+")
        atxt1=atxt.readlines() #必须是ANSI格式
        input1=atxt1[1]
        atxt=open('a.txt',"w")
        atxt.write(dir_choose.replace("/","\\")+"\n"+input1)

    def btn2_chooseDir(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "请为左上选择一个文件夹位置",self.cwd) # 起始路径
        if dir_choose == "":
            print("\n取消选择")
            return
        print("\n你选择的文件夹为:")
        print(dir_choose)
        self.line_edit1.setText(dir_choose)
        atxt = open('a.txt',"r+")
        atxt1=atxt.readlines() #必须是ANSI格式
        input0=atxt1[0]
        atxt=open('a.txt',"w")
        atxt.write(input0+dir_choose.replace("/","\\"))

    
atxt = open('a.txt',"r+")
atxt1=atxt.readlines() #必须是ANSI格式
input0=atxt1[0].replace("/","\\")
input1=atxt1[1].replace("/","\\")

def show_shezhi(): #不能设置在主窗口函数 无法调用
    Ui_Form.child_window = shezhi()
    Ui_Form.child_window.show()






if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)# 适配2k等高分辨率屏幕，低分辨率屏幕可除去
    app = QtWidgets.QApplication(sys.argv) #只出现一次 
    QApplication.setQuitOnLastWindowClosed(False) #关闭所有窗口,也不关闭应用程序
    app.setWindowIcon(QIcon('python.png'))
    w = QWidget()
    ui = Ui_Form()
    ui.setupUi(w)


    tp = QSystemTrayIcon(w)    #在系统托盘处显示图标
    tp.setIcon(QIcon('python.png'))    #设置系统托盘图标的菜单
    tpMenu = QMenu()
    a1 = QAction('&设置',triggered = show_shezhi)
    tpMenu.addAction(a1)
    a2 = QAction('&退出',triggered = quitAppQ)
    tpMenu.addAction(a2)
    tp.setContextMenu(tpMenu)
    tp.show()
    tp.activated.connect(act)
    w.show()
    sys.exit(app.exec_())