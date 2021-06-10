import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win=QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.home_btn.clicked.connect(self.showHome)
        self.ui.instructions_btn.clicked.connect(self.showInstructions)
        self.ui.stats_btn.clicked.connect(self.showStats)
        self.ui.play_btn.clicked.connect(self.showPlay)
        self.ui.score_btn.clicked.connect(self.showScore)
        self.ui.performance_btn.clicked.connect(self.showPerformance)
        self.ui.thankyou_btn.clicked.connect(self.showThankyou)
        
        

    def show(self):
        self.main_win.show()

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)

    def showInstructions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.instructions_page)

    def showStats(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stats_page)
        
    def showPlay(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.play_page)

    def showScore(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.score_page)

    def showPerformance(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.performance_page)

    def showThankyou(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.thankyou_page)
        
    


if  __name__=='__main__':
    app=QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    sys.exit(app.exec_())
