# -*- coding: utf-8 -*-
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI import Ui_MainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Windows
        self.setWindowTitle('Monster Hunter World: Iceborne 怪物屬性弱點查詢')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.setWindowOpacity(0.9)

        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QColor(0, 0, 0))
        self.setPalette(palette)

        # Effects
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(81)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        self.setStyleSheet('QWidget#left_widget{background:gray;border-top:1px solid white;border-bottom:1px solid white;border-left:1px solid white;border-top-left-radius:10px;border-bottom-left-radius:10px;}')

        # LOGO
        self.setWindowIcon(QIcon('Icons/LOGO.png'))

        # TabWidget
        self.ui.tabWidget.setStyleSheet("QWidget {background-color: gray }")

        # Label
        labelColor = QPalette()
        labelColor.setColor(QPalette.WindowText, QColor(200, 200, 200))
        self.ui.birdTypeLabel.setPalette(labelColor)
        self.ui.toothTypeLabel.setPalette(labelColor)
        self.ui.fishTypeLabel.setPalette(labelColor)
        self.ui.flyTypeLabel.setPalette(labelColor)
        self.ui.beatsTypeLabel.setPalette(labelColor)
        self.ui.leaveTypeLabel.setPalette(labelColor)
        self.ui.ElderTypeLabel.setPalette(labelColor)

        # Button
        self.ui.pushButton.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_9.text()))
        self.ui.pushButton_10.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_10.text()))
        self.ui.pushButton_11.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_11.text()))
        self.ui.pushButton_12.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_12.text()))
        self.ui.pushButton_13.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_13.text()))
        self.ui.pushButton_14.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_14.text()))
        self.ui.pushButton_15.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_15.text()))
        self.ui.pushButton_16.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_16.text()))
        self.ui.pushButton_17.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_17.text()))
        self.ui.pushButton_18.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_18.text()))
        self.ui.pushButton_19.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_19.text()))
        self.ui.pushButton_20.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_20.text()))
        self.ui.pushButton_21.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_21.text()))
        self.ui.pushButton_22.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_22.text()))
        self.ui.pushButton_23.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_23.text()))
        self.ui.pushButton_24.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_24.text()))
        self.ui.pushButton_25.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_25.text()))
        self.ui.pushButton_26.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_26.text()))
        self.ui.pushButton_27.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_27.text()))
        self.ui.pushButton_28.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_28.text()))
        self.ui.pushButton_29.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_29.text()))
        self.ui.pushButton_30.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_30.text()))
        self.ui.pushButton_31.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_31.text()))
        self.ui.pushButton_32.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_32.text()))
        self.ui.pushButton_33.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_33.text()))
        self.ui.pushButton_34.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_34.text()))
        self.ui.pushButton_35.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_35.text()))
        self.ui.pushButton_36.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_36.text()))
        self.ui.pushButton_37.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_37.text()))
        self.ui.pushButton_38.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_38.text()))
        self.ui.pushButton_39.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_39.text()))
        self.ui.pushButton_40.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_40.text()))
        self.ui.pushButton_41.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_41.text()))
        self.ui.pushButton_42.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_42.text()))
        self.ui.pushButton_43.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_43.text()))
        self.ui.pushButton_44.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_44.text()))
        self.ui.pushButton_45.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_45.text()))
        self.ui.pushButton_46.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_46.text()))
        self.ui.pushButton_47.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_47.text()))
        self.ui.pushButton_48.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_48.text()))
        self.ui.pushButton_49.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_49.text()))
        self.ui.pushButton_50.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_50.text()))
        self.ui.pushButton_51.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_51.text()))
        self.ui.pushButton_52.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_52.text()))
        self.ui.pushButton_53.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_53.text()))
        self.ui.pushButton_54.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_54.text()))
        self.ui.pushButton_55.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_55.text()))
        self.ui.pushButton_56.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_56.text()))
        self.ui.pushButton_57.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_57.text()))
        self.ui.pushButton_58.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_58.text()))
        self.ui.pushButton_59.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_59.text()))
        self.ui.pushButton_60.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_60.text()))
        self.ui.pushButton_61.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_61.text()))
        self.ui.pushButton_62.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_62.text()))
        self.ui.pushButton_63.clicked.connect(lambda: self.ButtonEvent(self.ui.pushButton_63.text()))

    def ButtonEvent(self, name):
        name = name+'.png'
        image = QPixmap()

        if name in os.listdir('Data01'): image.load('Data01/%s' % name)
        else: image.load('pic/NoData.png')
        self.ui.label.setPixmap(image)
        self.ui.label.setScaledContents(True)

        if name in os.listdir('Data02'):
            image.load('Data02/%s' % name)
        else:
            image.load('pic/NoData.png')
        self.ui.label_2.setPixmap(image)
        self.ui.label_2.setScaledContents(True)

        if name in os.listdir('Data03'):
            image.load('Data03/%s' % name)
        else:
            image.load('pic/NoData.png')
        self.ui.label_3.setPixmap(image)
        self.ui.label_3.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
