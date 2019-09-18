# -*- coding: utf-8 -*-
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MonsterWeakness import Ui_MainWindow
from subMonsterWeakness import Ui_MainWindow_sub
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # LOGO
        self.setWindowIcon(QIcon('MHWI_LOGO.png'))

        # Label
        self.ui.label.setText("冥燈龍")
        self.ui.label.setAlignment(Qt.AlignCenter)
        self.ui.label_2.setText("冰咒龍")
        self.ui.label_2.setAlignment(Qt.AlignCenter)
        self.ui.label_3.setText("冰牙龍")
        self.ui.label_3.setAlignment(Qt.AlignCenter)
        self.ui.label_4.setText("冰魚龍")
        self.ui.label_4.setAlignment(Qt.AlignCenter)
        self.ui.label_5.setText("凶爪龍")
        self.ui.label_5.setAlignment(Qt.AlignCenter)
        self.ui.label_6.setText("古代鹿首精")
        self.ui.label_6.setAlignment(Qt.AlignCenter)
        self.ui.label_7.setText("土砂龍")
        self.ui.label_7.setAlignment(Qt.AlignCenter)
        self.ui.label_8.setText("大凶豺龍")
        self.ui.label_8.setAlignment(Qt.AlignCenter)
        self.ui.label_9.setText("大凶顎龍")
        self.ui.label_9.setAlignment(Qt.AlignCenter)
        self.ui.label_10.setText("天地煌啼龍")
        self.ui.label_10.setAlignment(Qt.AlignCenter)
        self.ui.label_11.setText("屍套龍")
        self.ui.label_11.setAlignment(Qt.AlignCenter)
        self.ui.label_12.setText("岩賊龍")
        self.ui.label_12.setAlignment(Qt.AlignCenter)
        self.ui.label_13.setText("恐暴龍")
        self.ui.label_13.setAlignment(Qt.AlignCenter)
        self.ui.label_14.setText("慘爪龍")
        self.ui.label_14.setAlignment(Qt.AlignCenter)
        self.ui.label_15.setText("斬龍")
        self.ui.label_15.setAlignment(Qt.AlignCenter)
        self.ui.label_16.setText("櫻火龍")
        self.ui.label_16.setAlignment(Qt.AlignCenter)
        self.ui.label_17.setText("殲世滅盡龍")
        self.ui.label_17.setAlignment(Qt.AlignCenter)
        self.ui.label_18.setText("毒妖鳥")
        self.ui.label_18.setAlignment(Qt.AlignCenter)
        self.ui.label_19.setText("水妖鳥")
        self.ui.label_19.setAlignment(Qt.AlignCenter)
        self.ui.label_20.setText("泥魚龍")
        self.ui.label_20.setAlignment(Qt.AlignCenter)
        self.ui.label_21.setText("浮眠龍")
        self.ui.label_21.setAlignment(Qt.AlignCenter)
        self.ui.label_22.setText("浮空龍")
        self.ui.label_22.setAlignment(Qt.AlignCenter)
        self.ui.label_23.setText("滅盡龍")
        self.ui.label_23.setAlignment(Qt.AlignCenter)
        self.ui.label_24.setText("炎妃龍")
        self.ui.label_24.setAlignment(Qt.AlignCenter)
        self.ui.label_25.setText("炎王龍")
        self.ui.label_25.setAlignment(Qt.AlignCenter)
        self.ui.label_26.setText("熔山龍")
        self.ui.label_26.setAlignment(Qt.AlignCenter)
        self.ui.label_27.setText("熔岩龍")
        self.ui.label_27.setAlignment(Qt.AlignCenter)
        self.ui.label_28.setText("爆錘龍")
        self.ui.label_28.setAlignment(Qt.AlignCenter)
        self.ui.label_29.setText("爆鱗龍")
        self.ui.label_29.setAlignment(Qt.AlignCenter)
        self.ui.label_30.setText("猛牛龍")
        self.ui.label_30.setAlignment(Qt.AlignCenter)
        self.ui.label_31.setText("痹毒龍")
        self.ui.label_31.setAlignment(Qt.AlignCenter)
        self.ui.label_32.setText("眩鳥")
        self.ui.label_32.setAlignment(Qt.AlignCenter)
        self.ui.label_33.setText("硫斬龍")
        self.ui.label_33.setAlignment(Qt.AlignCenter)
        self.ui.label_34.setText("碎龍")
        self.ui.label_34.setAlignment(Qt.AlignCenter)
        self.ui.label_35.setText("絢輝龍")
        self.ui.label_35.setAlignment(Qt.AlignCenter)
        self.ui.label_36.setText("蒼火龍")
        self.ui.label_36.setAlignment(Qt.AlignCenter)
        self.ui.label_37.setText("蠻顎龍")
        self.ui.label_37.setAlignment(Qt.AlignCenter)
        self.ui.label_38.setText("角龍")
        self.ui.label_38.setAlignment(Qt.AlignCenter)
        self.ui.label_39.setText("貝希摩斯")
        self.ui.label_39.setAlignment(Qt.AlignCenter)
        self.ui.label_40.setText("轟龍")
        self.ui.label_40.setAlignment(Qt.AlignCenter)
        self.ui.label_41.setText("迅龍")
        self.ui.label_41.setAlignment(Qt.AlignCenter)
        self.ui.label_42.setText("鋼龍")
        self.ui.label_42.setAlignment(Qt.AlignCenter)
        self.ui.label_43.setText("雄火龍")
        self.ui.label_43.setAlignment(Qt.AlignCenter)
        self.ui.label_44.setText("雌火龍")
        self.ui.label_44.setAlignment(Qt.AlignCenter)
        self.ui.label_45.setText("雷顎龍")
        self.ui.label_45.setAlignment(Qt.AlignCenter)
        self.ui.label_46.setText("霜翼風漂龍")
        self.ui.label_46.setAlignment(Qt.AlignCenter)
        self.ui.label_47.setText("風漂龍")
        self.ui.label_47.setAlignment(Qt.AlignCenter)
        self.ui.label_48.setText("飛雷龍")
        self.ui.label_48.setAlignment(Qt.AlignCenter)
        self.ui.label_49.setText("骨錘龍")
        self.ui.label_49.setAlignment(Qt.AlignCenter)
        self.ui.label_50.setText("鹿首精")
        self.ui.label_50.setAlignment(Qt.AlignCenter)
        self.ui.label_51.setText("麒麟")
        self.ui.label_51.setAlignment(Qt.AlignCenter)
        self.ui.label_52.setText("黑狼鳥")
        self.ui.label_52.setAlignment(Qt.AlignCenter)
        self.ui.label_53.setText("黑角龍")
        self.ui.label_53.setAlignment(Qt.AlignCenter)

        # Button
        self.ui.pushButton.setIcon(QIcon('Icon/冥燈龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_2.setIcon(QIcon('Icon/冰咒龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_3.setIcon(QIcon('Icon/冰牙龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_4.setIcon(QIcon('Icon/冰魚龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_5.setIcon(QIcon('Icon/凶爪龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_6.setIcon(QIcon('Icon/古代鹿首精.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_7.setIcon(QIcon('Icon/土砂龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_8.setIcon(QIcon('Icon/大凶豺龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_9.setIcon(QIcon('Icon/大凶顎龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_10.setIcon(QIcon('Icon/天地煌啼龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_11.setIcon(QIcon('Icon/屍套龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_12.setIcon(QIcon('Icon/岩賊龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_13.setIcon(QIcon('Icon/恐暴龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_14.setIcon(QIcon('Icon/慘爪龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_15.setIcon(QIcon('Icon/斬龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_16.setIcon(QIcon('Icon/櫻火龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_17.setIcon(QIcon('Icon/殲世滅盡龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_18.setIcon(QIcon('Icon/毒妖鳥.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_19.setIcon(QIcon('Icon/水妖鳥.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_20.setIcon(QIcon('Icon/泥魚龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_21.setIcon(QIcon('Icon/浮眠龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_22.setIcon(QIcon('Icon/浮空龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_23.setIcon(QIcon('Icon/滅盡龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_24.setIcon(QIcon('Icon/炎妃龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_25.setIcon(QIcon('Icon/炎王龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_26.setIcon(QIcon('Icon/熔山龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_27.setIcon(QIcon('Icon/熔岩龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_28.setIcon(QIcon('Icon/爆錘龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_29.setIcon(QIcon('Icon/爆鱗龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_30.setIcon(QIcon('Icon/猛牛龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_31.setIcon(QIcon('Icon/痹毒龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_32.setIcon(QIcon('Icon/眩鳥.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_33.setIcon(QIcon('Icon/硫斬龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_34.setIcon(QIcon('Icon/碎龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_35.setIcon(QIcon('Icon/絢輝龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_36.setIcon(QIcon('Icon/蒼火龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_37.setIcon(QIcon('Icon/蠻顎龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_38.setIcon(QIcon('Icon/角龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_39.setIcon(QIcon('Icon/貝希摩斯.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_40.setIcon(QIcon('Icon/轟龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_41.setIcon(QIcon('Icon/迅龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_42.setIcon(QIcon('Icon/鋼龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_43.setIcon(QIcon('Icon/雄火龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_44.setIcon(QIcon('Icon/雌火龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_45.setIcon(QIcon('Icon/雷顎龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_46.setIcon(QIcon('Icon/霜翼風漂龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_47.setIcon(QIcon('Icon/風漂龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_48.setIcon(QIcon('Icon/飛雷龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_49.setIcon(QIcon('Icon/骨錘龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_50.setIcon(QIcon('Icon/鹿首精.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_51.setIcon(QIcon('Icon/麒麟.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_52.setIcon(QIcon('Icon/黑狼鳥.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))
        self.ui.pushButton_53.setIcon(QIcon('Icon/黑角龍.jpg'))
        self.ui.pushButton.setIconSize(QSize(100, 100))

        # Button Events
        self.ui.pushButton.clicked.connect(lambda: self.setIcon(1))
        self.ui.pushButton_2.clicked.connect(lambda: self.setIcon(2))
        self.ui.pushButton_3.clicked.connect(lambda: self.setIcon(3))
        self.ui.pushButton_4.clicked.connect(lambda: self.setIcon(4))
        self.ui.pushButton_5.clicked.connect(lambda: self.setIcon(5))
        self.ui.pushButton_6.clicked.connect(lambda: self.setIcon(6))
        self.ui.pushButton_7.clicked.connect(lambda: self.setIcon(7))
        self.ui.pushButton_8.clicked.connect(lambda: self.setIcon(8))
        self.ui.pushButton_9.clicked.connect(lambda: self.setIcon(9))
        self.ui.pushButton_10.clicked.connect(lambda: self.setIcon(10))
        self.ui.pushButton_11.clicked.connect(lambda: self.setIcon(11))
        self.ui.pushButton_12.clicked.connect(lambda: self.setIcon(12))
        self.ui.pushButton_13.clicked.connect(lambda: self.setIcon(13))
        self.ui.pushButton_14.clicked.connect(lambda: self.setIcon(14))
        self.ui.pushButton_15.clicked.connect(lambda: self.setIcon(15))
        self.ui.pushButton_16.clicked.connect(lambda: self.setIcon(16))
        self.ui.pushButton_17.clicked.connect(lambda: self.setIcon(17))
        self.ui.pushButton_18.clicked.connect(lambda: self.setIcon(18))
        self.ui.pushButton_19.clicked.connect(lambda: self.setIcon(19))
        self.ui.pushButton_20.clicked.connect(lambda: self.setIcon(20))
        self.ui.pushButton_21.clicked.connect(lambda: self.setIcon(21))
        self.ui.pushButton_22.clicked.connect(lambda: self.setIcon(22))
        self.ui.pushButton_23.clicked.connect(lambda: self.setIcon(23))
        self.ui.pushButton_24.clicked.connect(lambda: self.setIcon(24))
        self.ui.pushButton_25.clicked.connect(lambda: self.setIcon(25))
        self.ui.pushButton_26.clicked.connect(lambda: self.setIcon(26))
        self.ui.pushButton_27.clicked.connect(lambda: self.setIcon(27))
        self.ui.pushButton_28.clicked.connect(lambda: self.setIcon(28))
        self.ui.pushButton_29.clicked.connect(lambda: self.setIcon(29))
        self.ui.pushButton_30.clicked.connect(lambda: self.setIcon(30))
        self.ui.pushButton_31.clicked.connect(lambda: self.setIcon(31))
        self.ui.pushButton_32.clicked.connect(lambda: self.setIcon(32))
        self.ui.pushButton_33.clicked.connect(lambda: self.setIcon(33))
        self.ui.pushButton_34.clicked.connect(lambda: self.setIcon(34))
        self.ui.pushButton_35.clicked.connect(lambda: self.setIcon(35))
        self.ui.pushButton_36.clicked.connect(lambda: self.setIcon(36))
        self.ui.pushButton_37.clicked.connect(lambda: self.setIcon(37))
        self.ui.pushButton_38.clicked.connect(lambda: self.setIcon(38))
        self.ui.pushButton_39.clicked.connect(lambda: self.setIcon(39))
        self.ui.pushButton_40.clicked.connect(lambda: self.setIcon(40))
        self.ui.pushButton_41.clicked.connect(lambda: self.setIcon(41))
        self.ui.pushButton_42.clicked.connect(lambda: self.setIcon(42))
        self.ui.pushButton_43.clicked.connect(lambda: self.setIcon(43))
        self.ui.pushButton_44.clicked.connect(lambda: self.setIcon(44))
        self.ui.pushButton_45.clicked.connect(lambda: self.setIcon(45))
        self.ui.pushButton_46.clicked.connect(lambda: self.setIcon(46))
        self.ui.pushButton_47.clicked.connect(lambda: self.setIcon(47))
        self.ui.pushButton_48.clicked.connect(lambda: self.setIcon(48))
        self.ui.pushButton_49.clicked.connect(lambda: self.setIcon(49))
        self.ui.pushButton_50.clicked.connect(lambda: self.setIcon(50))
        self.ui.pushButton_51.clicked.connect(lambda: self.setIcon(51))
        self.ui.pushButton_52.clicked.connect(lambda: self.setIcon(52))
        self.ui.pushButton_53.clicked.connect(lambda: self.setIcon(53))

    def setIcon(self, index):
        if index == 1:
            self.newWindow = sub_MainWindow("冥燈龍.jpg")
        elif index == 2:
            self.newWindow = sub_MainWindow("冰咒龍.jpg")
        elif index == 3:
            self.newWindow = sub_MainWindow("冰牙龍.jpg")
        elif index == 4:
            self.newWindow = sub_MainWindow("冰魚龍.jpg")
        elif index == 5:
            self.newWindow = sub_MainWindow("凶爪龍.jpg")
        elif index == 6:
            self.newWindow = sub_MainWindow("古代鹿首精.jpg")
        elif index == 7:
            self.newWindow = sub_MainWindow("土砂龍.jpg")
        elif index == 8:
            self.newWindow = sub_MainWindow("大凶豺龍.jpg")
        elif index == 9:
            self.newWindow = sub_MainWindow("大凶顎龍.jpg")
        elif index == 10:
            self.newWindow = sub_MainWindow("天地煌啼龍.jpg")
        elif index == 11:
            self.newWindow = sub_MainWindow("屍套龍.jpg")
        elif index == 12:
            self.newWindow = sub_MainWindow("岩賊龍.jpg")
        elif index == 13:
            self.newWindow = sub_MainWindow("恐暴龍.jpg")
        elif index == 14:
            self.newWindow = sub_MainWindow("慘爪龍.jpg")
        elif index == 15:
            self.newWindow = sub_MainWindow("斬龍.jpg")
        elif index == 16:
            self.newWindow = sub_MainWindow("櫻火龍.jpg")
        elif index == 17:
            self.newWindow = sub_MainWindow("殲世滅盡龍.jpg")
        elif index == 18:
            self.newWindow = sub_MainWindow("毒妖鳥.jpg")
        elif index == 19:
            self.newWindow = sub_MainWindow("水妖鳥.jpg")
        elif index == 20:
            self.newWindow = sub_MainWindow("泥魚龍.jpg")
        elif index == 21:
            self.newWindow = sub_MainWindow("浮眠龍.jpg")
        elif index == 22:
            self.newWindow = sub_MainWindow("浮空龍.jpg")
        elif index == 23:
            self.newWindow = sub_MainWindow("滅盡龍.jpg")
        elif index == 24:
            self.newWindow = sub_MainWindow("炎妃龍.jpg")
        elif index == 25:
            self.newWindow = sub_MainWindow("炎王龍.jpg")
        elif index == 26:
            self.newWindow = sub_MainWindow("熔山龍.jpg")
        elif index == 27:
            self.newWindow = sub_MainWindow("熔岩龍.jpg")
        elif index == 28:
            self.newWindow = sub_MainWindow("爆錘龍.jpg")
        elif index == 29:
            self.newWindow = sub_MainWindow("爆鱗龍.jpg")
        elif index == 30:
            self.newWindow = sub_MainWindow("猛牛龍.jpg")
        elif index == 31:
            self.newWindow = sub_MainWindow("痹毒龍.jpg")
        elif index == 32:
            self.newWindow = sub_MainWindow("眩鳥.jpg")
        elif index == 33:
            self.newWindow = sub_MainWindow("硫斬龍.jpg")
        elif index == 34:
            self.newWindow = sub_MainWindow("碎龍.jpg")
        elif index == 35:
            self.newWindow = sub_MainWindow("絢輝龍.jpg")
        elif index == 36:
            self.newWindow = sub_MainWindow("蒼火龍.jpg")
        elif index == 37:
            self.newWindow = sub_MainWindow("蠻顎龍.jpg")
        elif index == 38:
            self.newWindow = sub_MainWindow("角龍.jpg")
        elif index == 39:
            self.newWindow = sub_MainWindow("貝希摩斯.jpg")
        elif index == 40:
            self.newWindow = sub_MainWindow("轟龍.jpg")
        elif index == 41:
            self.newWindow = sub_MainWindow("迅龍.jpg")
        elif index == 42:
            self.newWindow = sub_MainWindow("鋼龍.jpg")
        elif index == 43:
            self.newWindow = sub_MainWindow("雄火龍.jpg")
        elif index == 44:
            self.newWindow = sub_MainWindow("雌火龍.jpg")
        elif index == 45:
            self.newWindow = sub_MainWindow("雷顎龍.jpg")
        elif index == 46:
            self.newWindow = sub_MainWindow("霜翼風漂龍.jpg")
        elif index == 47:
            self.newWindow = sub_MainWindow("風漂龍.jpg")
        elif index == 48:
            self.newWindow = sub_MainWindow("飛雷龍.jpg")
        elif index == 49:
            self.newWindow = sub_MainWindow("骨錘龍.jpg")
        elif index == 50:
            self.newWindow = sub_MainWindow("鹿首精.jpg")
        elif index == 51:
            self.newWindow = sub_MainWindow("麒麟.jpg")
        elif index == 52:
            self.newWindow = sub_MainWindow("黑狼鳥.jpg")
        elif index == 53:
            self.newWindow = sub_MainWindow("黑角龍.jpg")

        self.newWindow.show()


class sub_MainWindow(QMainWindow):
    def __init__(self, pic):
        super(sub_MainWindow, self).__init__()
        self.ui = Ui_MainWindow_sub()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QPixmap('pic/%s' % pic))
        self.ui.label.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())