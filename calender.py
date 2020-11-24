## Ex 5-13. QCalenderWidget.(참고 : https://wikidocs.net/15213)
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate
from googleAPI import main
from gtts import gTTS
from gtts import gTTS
import pyglet


class MyApp(QWidget):

    def __init__(self):
        # API에서 데이터 받아오기
        self.DateList, self.ScheduleList = main()

        # self.Calender = {}
        # for i in range(0, len(self.DateList)):
        #     self.Calender[self.DateList[i]] = self.ScheduleList[i]

        super().__init__()
        self.initUI()
        

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True) # 캘린더에서 날짜를 찍는다면
        cal.clicked[QDate].connect(self.showDate) # 날짜를 쇼 데이터에 전달

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.setText('?')

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        # print(vbox.addWidget(cal))
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date): # 날짜를 받아서
        numList = []
        ScheduleSum = ' '
        a, b, c, d = date.toString().split(' ')
        Date = (d+'-'+b+'-'+c)

        if (Date in self.DateList):
            for i in range(0, len(self.DateList)):
                if (Date == self.DateList[i]):
                    numList.append(i)

            for j in range(0, len(numList)):
                ScheduleSum = ScheduleSum + ' ' + self.ScheduleList[numList[j]]

            self.lbl.setText(date.toString() + ScheduleSum)
            
            text = ScheduleSum

            tts = gTTS(text=text, lang='en')
            tts.save("Schedule.mp3")

            song = pyglet.media.load('Schedule.mp3')
            song.play()
            # pyglet.app.run()
            os.remove('Schedule.mp3')

        
        else:
            self.lbl.setText(date.toString()) # 날짜를 문자열로 받아서 셋 텍스트에 찍어준다.




        # if 조건받아서같은 날짜라면 구글 캘린더 api에서나오는 날짜 내용 등 함수프로그램으로
        # 받아보자


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())