import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.GetUnit1 = ''
        self.GetUnit2 = ''
        self.UnitList = ['mm', 'm', 'km']
        self.save1 = 0
        self.save2 = 0

    def initUI(self):
        self.arrow1 = QLabel('->', self)
        self.arrow1.move(395, 55)
        self.arrow2 = QLabel('->', self)
        self.arrow2.move(395, 105)


        ###################### 여긴 TabBar ############################
        # 이미지 읽어오기
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        # ctrl+Q 누르면 종료
        exitAction.setShortcut('Ctrl+Q')
        # 이미지에 가져다 대면 아래 설명글
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 이미지에 가져다대면 메모장모양?
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        ###################### TabBar End ############################
        ###################### 여긴 comboBox ############################
        # cb는 ComboBox이다
        Unit1 = QComboBox(self)
        Unit1.resize(350,40)
        Unit2 = QComboBox(self)
        Unit2.resize(350, 40)
        # 옵션들을 추가한다
        Unit1.addItem('mm')
        Unit1.addItem('m')
        Unit1.addItem('km')

        Unit2.addItem('mm')
        Unit2.addItem('m')
        Unit2.addItem('km')
        # ComboBox위치를 잡아준다
        Unit1.move(30, 50)
        Unit2.move(420, 50)

        Unit1Text = Unit1.activated[str]
        # Unit2Text = Unit2.activated[str]
        print(Unit1Text)

        Unit1.activated[str].connect(self.GETUnit1)
        Unit2.activated[str].connect(self.GETUnit2)
        ###################### comboBox End ############################
        ###################### 여긴 LineEdit ############################
        self.lbl = QLabel(self)
        self.lbl.move(420, 100)
        self.lbl.setStyleSheet("color: red;")

        # self.lbl.font().setPointSize(300)
        font = self.lbl.font()
        font.setPointSize(20)

        self.lbl.setFont(font)


        qle = QLineEdit(self)
        qle.move(30, 100)
        qle.resize(350, 40)

        qle.textChanged[str].connect(self.UnitResult)
        # textChanged = qle.textChanged
        # self.UnitChanged(textChanged, Unit1Text, Unit2Text)
        ###################### LineEdit End ############################

        # 위에서 작성한 코드 화면으로 띄우기
        self.setWindowTitle('단위환산 프로그램')
        self.setGeometry(300, 300, 800, 200)
        self.show()

    # .font().setPointSize(300)

    # 글자를 입력하면 결과값에 출력
    def UnitResult(self, text):
        # 입력창에 아무것도 없을시 0
        if (text == ''):
            self.lbl.setText('0' + ' ' + self.GetUnit1)
            self.lbl.adjustSize()
        # 단위가 같다면 변환없음
        elif (self.GetUnit1 == self.GetUnit2):
            self.lbl.setText(text + ' ' + self.GetUnit1)
            self.lbl.adjustSize()

        else:
            # 선택힌 단위가 작은거에서 큰걸로인지 큰거에서 작은걸로인지 확인
            for i in range(0, len(self.UnitList)):
                if (self.GetUnit1 == self.UnitList[i]):
                    self.save1 = i
                elif (self.GetUnit2 == self.UnitList[i]):
                    self.save2 = i
            # 해당 차리만큼 10^3 곱하기
            if (self.save1 > self.save2):
                self.lbl.setText(str(int(text)* (10**(3*(self.save1 - self.save2)))) + ' ' + self.GetUnit2)
                self.lbl.adjustSize()
            else:
                self.lbl.setText(str(int(text)* (10**-(3*(self.save2 - self.save1)))) + ' ' + self.GetUnit2)
                self.lbl.adjustSize()

    # 단위를 선택하면 단위를 저장
    def GETUnit1(self, text):
        self.GetUnit1 = text
    def GETUnit2(self, text):
        self.GetUnit2 = text




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())