# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_team.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from score_team import Ui_MainWindow as score_team
import math
import sqlite3
connect = sqlite3.connect('fantasy.db')
curfantasy = connect.cursor()


class Ui_TeamBox(object):
    def __init__(self):
        self.score_team = QtWidgets.QMainWindow()
        self.score_screen = score_team()
        self.score_screen.setupUi(self.score_team)
        
    def setupUi(self, TeamBox):
        TeamBox.setObjectName("TeamBox")
        TeamBox.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TeamBox)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 721, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.teambox = QtWidgets.QComboBox(self.centralwidget)
        self.teambox.setGeometry(QtCore.QRect(120, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.teambox.setFont(font)
        self.teambox.setObjectName("teambox")
        self.teambox.addItem("")
        self.matchbox = QtWidgets.QComboBox(self.centralwidget)
        self.matchbox.setGeometry(QtCore.QRect(500, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.matchbox.setFont(font)
        self.matchbox.setObjectName("matchbox")
        self.matchbox.addItem("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 811, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 180, 261, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerview = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.playerview.setObjectName("playerview")
        self.horizontalLayout.addWidget(self.playerview)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.horizontalLayoutWidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(459, 180, 261, 281))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pointview = QtWidgets.QListView(self.horizontalLayoutWidget_2)
        self.pointview.setObjectName("pointview")
        self.horizontalLayout_2.addWidget(self.pointview)
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.horizontalLayoutWidget_2)
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalLayout_2.addWidget(self.verticalScrollBar_2)
        self.score = QtWidgets.QPushButton(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(300, 500, 201, 28))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.score.setFont(font)
        self.score.setObjectName("score")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        TeamBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TeamBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        TeamBox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TeamBox)
        self.statusbar.setObjectName("statusbar")
        TeamBox.setStatusBar(self.statusbar)

        self.retranslateUi(TeamBox)
        QtCore.QMetaObject.connectSlotsByName(TeamBox)

        self.teambox.activated.connect(self.matchshows)
        self.matchbox.activated.connect(self.datashow)
        self.score.clicked.connect(self.calculatewindow)

        curfantasy.execute("select name from team")
        team_data = curfantasy.fetchall()
        team_data = list(set(team_data))
        for data in team_data:
            self.teambox.addItem(data[0])
        
    def matchshows(self):
        value = self.teambox.currentText()
        curfantasy.execute("select matches from team where name  = '" + value + "'")
        play_match = curfantasy.fetchall()
        play_match = list(set(play_match))
        play_match.sort()
        self.matchbox.clear()
        for match in play_match:
            self.matchbox.addItem(match[0])

    def datashow(self):
        value = self.matchbox.currentText()
        curfantasy.execute("select players , value from team where matches = '"+ value +"'")
        play_data = curfantasy.fetchall()
        self.Playerview.clear()
        self.Pointview.clear()
        for data in play_data:
            self.Playerview.addItem(data[0])
            self.Pointview.addItem(str(data[1]))
    
    def calculatewindow(self):
        items = []
        for index in range(self.PointList.count()):
            item = self.Pointview.item(index)
            items.append(int(item.text()))
        print(sum(items))
        self.score_screen.score_box.setText(str(sum(items)))
        self.score_team.show()
        

    def retranslateUi(self, TeamBox):
        _translate = QtCore.QCoreApplication.translate
        TeamBox.setWindowTitle(_translate("TeamBox", "MainWindow"))
        self.label.setText(_translate("TeamBox", "Evaluate The Performance Of Your Fantasy Team"))
        self.teambox.setItemText(0, _translate("TeamBox", "Select Team"))
        self.matchbox.setItemText(0, _translate("TeamBox", "Select Match"))
        self.score.setText(_translate("TeamBox", "Calculate Score"))
        self.label_2.setText(_translate("TeamBox", "Players"))
        self.label_3.setText(_translate("TeamBox", "Points"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TeamBox = QtWidgets.QMainWindow()
    ui = Ui_TeamBox()
    ui.setupUi(TeamBox)
    TeamBox.show()
    sys.exit(app.exec_())
