import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication



class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

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

        calcList = ['AC','+/-','%','÷','7','8','9','×','4','5','6','―','1','2','3','+','0','s','.','=']

        # label의 종료를 알기위해
        num = 0

        # 결과값이 나오는 Label를 지정하고 위치는 오른쪽으로 고정
        label = QLabel(str(num), self)
        # x, y
        label.move(0, 0)
        label.setStyleSheet("color: white;"
                             "border-style: solid;"
                             # 가운데기준.세로, 가운데기준.가로 ( 다시해야함 )
                             "border-width : 27px 133px;"
                             # "border-width: 1px;"
                             "border-color: #475564;"
                             "background-color :  #475564")
        # Label의 폰트크기
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)


        # 버튼들
        while True:
            for j in top:
                for k in left:
                    if (btnList[num] == 's'):
                        num += 1
                        continue

                    btn = QPushButton(btnList[num], self)
                    btn.move(k, j)

                    if (btnList[num] == '0'):
                        btn.resize(148,74)
                    else:
                        btn.resize(74,74)

                    if (btnList[num] == '÷' or btnList[num] == '×' or btnList[num] == '―' or btnList[num] == '+' or btnList[num] == '='):
                        btn.setStyleSheet("color: black;"
                                "background-color :  #f2a23b")
                        # btn.clicked.connect(lambda : self.result(label, 's'))
                    else:    
                        btn.setStyleSheet("color: black;"
                                "background-color :  #7a8187")
                        # btn.clicked.connect(lambda : self.result(label, 'd'))

                    # # 여기 뭐야 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    # btn.clicked.connect(lambda : self.result(label, btnList[num-1]))
                    
                    print(btnList[num])
                    num += 1
                    
                    
            if (num == len(btnList)):
                break

        # self.setLayout(vbox)
        # 프로그램 title
        self.setWindowTitle('Calculator')
        # 프로그램 위치 a, b + 프로그램 사이즈 c, d
        self.setGeometry(400, 400, 296, 450)
        # 프로그램 켜기
        self.show()
        
        # 여기 뭐야 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # btn.clicked.connect(lambda : self.result(label, num))

    def result(self, label, btn):
        label.setText(btn)
        label.repaint()
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

