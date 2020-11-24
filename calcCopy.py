import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.numList = []
        
        self.sign = '0'
        self.numResult = '0'
        self.numResult2 = '0'

    def initUI(self):
        # 검정 #475564
        # 회색 #7a8187
        # 주황 #f2a23b

        # Y 좌표
        top = [80, 154, 228, 302, 376]

        # X 좌표
        left = [0, 74, 148, 222]

        # 계산기 키값들
        btnList = ['AC','+/-','%','÷','7','8','9','×','4','5','6','―','1','2','3','+','0','s','.','=']

        # label의 종료를 알기위해
        num = 0

        # 결과값이 나오는 Label를 지정하고 위치는 오른쪽으로 고정( 다른방법 찾아보기)
        label = QLabel('                                ', self)
        # x, y
        label.move(0, 0)
        label.setStyleSheet("color: white;"
                             "border-style: solid;"
                             #가운데기준.세로, 가운데기준.가로 ( 다시해야함 )
                             "border-width : 27px 1px;"
                             "border-color: #475564;"
                             "background-color :  #475564")
        # Label의 폰트크기
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)


        # 버튼들
        
        num2 = 0
        num3 = 0

        btnA = QPushButton(btnList[num], self)
        btnA.move(left[num], top[num3])
        btnA.resize(74,74)
        btnA.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnA.clicked.connect(lambda : self.result(label, btnList[0]))
        

        num += 1
        num2 += 1

        btnB = QPushButton(btnList[num], self)
        btnB.move(left[num2], top[num3])
        btnB.resize(74,74)
        btnB.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnB.clicked.connect(lambda : self.result(label, btnList[1]))

        num += 1
        num2 += 1

        btnC = QPushButton(btnList[num], self)
        btnC.move(left[num2], top[num3])
        btnC.resize(74,74)
        btnC.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnC.clicked.connect(lambda : self.result(label, btnList[2]))

        num += 1
        num2 += 1

        btnD = QPushButton(btnList[num], self)
        btnD.move(left[num2], top[num3])
        btnD.resize(74,74)
        btnD.setStyleSheet("color: black;"
                    "background-color :  #f2a23b")
        btnD.clicked.connect(lambda : self.result(label, btnList[3]))

        num2 = 0
        num += 1
        num3 += 1

        btnE = QPushButton(btnList[num], self)
        btnE.move(left[num2], top[num3])
        btnE.resize(74,74)
        btnE.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnE.clicked.connect(lambda : self.result(label, btnList[4]))

        num += 1
        num2 += 1

        btnF = QPushButton(btnList[num], self)
        btnF.move(left[num2], top[num3])
        btnF.resize(74,74)
        btnF.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnF.clicked.connect(lambda : self.result(label, btnList[5]))

        num += 1
        num2 += 1

        btnG = QPushButton(btnList[num], self)
        btnG.move(left[num2], top[num3])
        btnG.resize(74,74)
        btnG.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnG.clicked.connect(lambda : self.result(label, btnList[6]))

        num += 1
        num2 += 1

        btnH = QPushButton(btnList[num], self)
        btnH.move(left[num2], top[num3])
        btnH.resize(74,74)
        btnH.setStyleSheet("color: black;"
                    "background-color :  #f2a23b")
        btnH.clicked.connect(lambda : self.result(label, btnList[7]))

        num += 1
        num2 = 0
        num3 += 1

        btnI = QPushButton(btnList[num], self)
        btnI.move(left[num2], top[num3])
        btnI.resize(74,74)
        btnI.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnI.clicked.connect(lambda : self.result(label, btnList[8]))

        num += 1
        num2 += 1

        btnJ = QPushButton(btnList[num], self)
        btnJ.move(left[num2], top[num3])
        btnJ.resize(74,74)
        btnJ.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnJ.clicked.connect(lambda : self.result(label, btnList[9]))

        num += 1
        num2 += 1

        btnK = QPushButton(btnList[num], self)
        btnK.move(left[num2], top[num3])
        btnK.resize(74,74)
        btnK.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnK.clicked.connect(lambda : self.result(label, btnList[10]))

        num += 1
        num2 += 1

        btnL = QPushButton(btnList[num], self)
        btnL.move(left[num2], top[num3])
        btnL.resize(74,74)
        btnL.setStyleSheet("color: black;"
                    "background-color :  #f2a23b")
        btnL.clicked.connect(lambda : self.result(label, btnList[11]))

        num += 1
        num2 = 0
        num3 += 1


        btnN = QPushButton(btnList[num], self)
        btnN.move(left[num2], top[num3])
        btnN.resize(74,74)
        btnN.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnN.clicked.connect(lambda : self.result(label, btnList[12]))

        num += 1
        num2 += 1

        btnM = QPushButton(btnList[num], self)
        btnM.move(left[num2], top[num3])
        btnM.resize(74,74)
        btnM.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnM.clicked.connect(lambda : self.result(label, btnList[13]))

        num += 1
        num2 += 1

        btnO = QPushButton(btnList[num], self)
        btnO.move(left[num2], top[num3])
        btnO.resize(74,74)
        btnO.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnO.clicked.connect(lambda : self.result(label, btnList[14]))

        num += 1
        num2 += 1

        btnP = QPushButton(btnList[num], self)
        btnP.move(left[num2], top[num3])
        btnP.resize(74,74)
        btnP.setStyleSheet("color: black;"
                    "background-color :  #f2a23b")
        btnP.clicked.connect(lambda : self.result(label, btnList[15]))

        num += 1
        num2 = 0
        num3 += 1

        btnQ = QPushButton(btnList[num], self)
        btnQ.move(left[num2], top[num3])
        btnQ.resize(74,74)
        btnQ.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnQ.clicked.connect(lambda : self.result(label, btnList[16]))
        btnQ.resize(148,74)

        num += 2
        num2 += 2

        btnS = QPushButton(btnList[num], self)
        btnS.move(left[num2], top[num3])
        btnS.resize(74,74)
        btnS.setStyleSheet("color: black;"
                    "background-color :  #7a8187")
        btnS.clicked.connect(lambda : self.result(label, btnList[18]))

        num += 1
        num2 += 1

        btnT = QPushButton(btnList[num], self)
        btnT.move(left[num2], top[num3])
        btnT.resize(74,74)
        btnT.setStyleSheet("color: black;"
                    "background-color :  #f2a23b")
        btnT.clicked.connect(lambda : self.result(label, btnList[19]))

        # 프로그램 title
        self.setWindowTitle('Calculator')
        # 프로그램 위치 a, b + 프로그램 사이즈 c, d
        self.setGeometry(400, 400, 296, 450)
        # 프로그램 켜기
        self.show()

    # 16 자리까지
    def result(self, label, btn):
        # btnList = ['AC','+/-','%','÷','7','8','9','×','4','5','6','―','1','2','3','+','0','s','.','=']
        if (btn == '0' or btn == '1' or btn == '2' or btn == '3' or btn == '4' or btn == '5' or btn == '6' or btn == '7' or btn == '8' or btn == '9'):
            if (self.sign == '0'):
                if (self.numResult == '0'):
                    self.numResult = btn
                else:
                    self.numResult = self.numResult + btn
            else:
                if (self.numResult2 == '0'):
                    self.numResult2 = btn
                else:
                    self.numResult2 = self.numResult2 + btn

        if (btn == 'AC'):
            self.numList = []
            self.numResult2 = '0'
            self.sign = '0'
            self.numResult = '-'

        if (btn == '+/-'):
            self.numResult = str(int(self.numResult) * -1)

        if (btn == '%'):
            self.sign = btn

        if (btn == '÷'):
            self.sign = btn

        if (btn == '×'):
            self.sign = btn
        
        if (btn == '―'):
            self.sign = btn
        
        if (btn == '+'):
            self.sign = btn

        if (btn == '.'):
            pass

        if (btn == '='):
            if (self.sign == '0'):
                pass
            else:
                if (self.sign == '%'):
                    self.numResult = str(int(self.numResult) % int(self.numResult2))

                if (self.sign == '÷'):
                    self.numResult = str(int(self.numResult) / int(self.numResult2))
                    
                if (self.sign == '×'):
                    self.numResult = str(int(self.numResult) * int(self.numResult2))
                
                if (self.sign == '―'):
                    self.numResult = str(int(self.numResult) - int(self.numResult2))
                
                if (self.sign == '+'):
                    self.numResult = str(int(self.numResult) + int(self.numResult2))

                self.sign = '0'
                self.numResult2 = '0'
                    
        
        if (self.sign == '0'):
            label.setText(self.numResult)
        else:
            label.setText(self.numResult2)
        label.repaint()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

