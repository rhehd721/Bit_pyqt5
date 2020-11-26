import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import os
import cv2
import numpy as np


# from Conversation import Conversation

# 사진을 저장할 폴더 생성
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

createFolder('Output')


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

        # 버튼을 눌렀는지 체크하는 변수
        self.BlurState = 0
        self.ShrpenState = 0
        self.GrayState = 0
        self.InvertState = 0

        # 내가 고른 파일 이름
        self.ChoiceFile = ''


    def initUI(self):
        ############################ CheckBox ############################
        self.Blur = QCheckBox('Blur', self)
        self.Blur.move(300, 60)
        self.Blur.stateChanged.connect(self.BlurButtonState)

        self.Shrpen = QCheckBox('Shrpen', self)
        self.Shrpen.move(300, 80)
        self.Shrpen.stateChanged.connect(self.ShrpenButtonState)

        self.Gray = QCheckBox('Gray', self)
        self.Gray.move(450, 60)
        self.Gray.stateChanged.connect(self.GrayButtonState)

        self.Invert = QCheckBox('Invert', self)
        self.Invert.move(450, 80)
        self.Invert.stateChanged.connect(self.InvertButtonState)

        self.none = QCheckBox('none', self)
        self.none.move(300, 100)
        self.none.stateChanged.connect(self.changeNone)
        ############################ CheckBox End ############################

        ############################## Button ################################
        LoadingBtn = QPushButton('사진 불러오기',self)
        LoadingBtn.resize(200, 100)
        LoadingBtn.move( 50 , 50)
        LoadingBtn.clicked.connect(self.showDialog)

        SaveBtn = QPushButton('사진 저장하기', self)
        SaveBtn.resize(200, 100)
        SaveBtn.move(550, 50)
        SaveBtn.clicked.connect(self.SaveImage)

        vbox = QHBoxLayout()
        vbox.addWidget(LoadingBtn)
        vbox.addWidget(SaveBtn)
        ############################# Button End ###############################

        ############################# Fixmap ###################################
        # 이미지를 띄울 라벨준비
        self.BeforeLabel = QLabel(self)
        self.AfterLabel = QLabel(self)
        # 라벨의 크기를 지정
        self.BeforeLabel.resize(320,280)
        self.AfterLabel.resize(320, 280)
        # 라벨의 위치지정
        self.BeforeLabel.move(50,200)
        self.AfterLabel.move(430, 200)
        # 라벨에 넣어줄 사진 지정
        BeforeImage = QPixmap('Before.png')
        AfterImage = QPixmap('Before.png')
        # 라벨에 사진 넣어주기
        self.BeforeLabel.setPixmap(QPixmap(BeforeImage))
        self.AfterLabel.setPixmap(QPixmap(AfterImage))
        ############################# Fixmap End ###################################

        self.setWindowTitle('이미지 수정프로그램')
        self.setGeometry(300, 300, 800, 540)
        self.show()

        
    # 파일불러오기 함수
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        splitlist = []
        
        # 내가 선택한 파일의 이름
        self.ChoiceFile = fname[0]
        # 필요한 부분만 split
        splitlist = self.ChoiceFile.split('/')
        self.ChoiceFile = splitlist[len(splitlist)-1]

        # 사진을 고르면 새로운 사진으로 라벨 업데이트
        BeforeImage = QPixmap(self.ChoiceFile)
        self.BeforeLabel.setPixmap(QPixmap(BeforeImage))
        self.BeforeLabel.repaint()

    # 체크박스 상태 함수
    def BlurButtonState(self, state):
        if (state == 2):    # 만약 상태가 눌린상태라면
            self.BlurState = 1
        else:
            self.BlurState = 0
    def ShrpenButtonState(self, state):
        if (state == 2):    # 만약 상태가 눌린상태라면
            self.ShrpenState = 1
        else:
            self.ShrpenState = 0
    def GrayButtonState(self, state):
        if (state == 2):    # 만약 상태가 눌린상태라면
            self.GrayState = 1
        else:
            self.GrayState = 0
    def InvertButtonState(self, state):
        if (state == 2):    # 만약 상태가 눌린상태라면
            self.InvertState = 1
        else:
            self.InvertState = 0

    # None 체크박스 상태 함수
    def changeNone(self, state):
        if (state == 2):    # 만약 상태가 눌린상태라면
            self.Blur.toggle()
            self.Shrpen.toggle()

    # 버튼들의 상태에 따라 이미지 변환후 저장
    def SaveImage(self):
        # Con = Conversation()

        image = cv2.imread(self.ChoiceFile, cv2.IMREAD_COLOR)
        ChangeImage = 0

        if (self.BlurState == 1):
            ChangeImage = self.BlurDef(image)
        # # if (self.ShrpenState == 1):
        # #     Con.Shrpen(self.ChoiceFile)
        # if (ChangeImage != 0):
        #     ChangeImage = 0
        #     if (self.GrayState == 1):
        #         Con.Gray(self.ChoiceFile)
        # if (self.InvertState == 1):
        #     Con.Invert(self.ChoiceFile)

        cv2.imwrite("Output/Result.png", ChangeImage)

        # 사진을 고르면 새로운 사진으로 라벨 업데이트
        AfterImage = QPixmap("Output/Result.png")
        self.AfterLabel.setPixmap(QPixmap(AfterImage))
        self.AfterLabel.repaint()

    def BlurDef(self, image):
        kernel = np.ones((2, 2), np.uint8)
        ChangedImage = cv2.filter2D(image, -1, kernel)
        return ChangedImage



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())