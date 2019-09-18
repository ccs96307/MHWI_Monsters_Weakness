# -*- coding: utf-8 -*-
import os
import re

picList = os.listdir('pic/')
IconList = os.listdir('Icon/')

n = 0
# for pic in picList:
#     for icon in IconList:
#         if pic == icon:
#             n += 1
#             if n == 1:
#                 print('self.ui.label.setText("%s")\nself.ui.label.setAlignment(Qt.AlignCenter)' % re.sub('.jpg', '', pic))
#             else:
#                 print('self.ui.label_%s.setText("%s")\nself.ui.label_%s.setAlignment(Qt.AlignCenter)' % (n, re.sub('.jpg', '', pic), n))

# for pic in picList:
#     for icon in IconList:
#         if pic == icon:
#             n += 1
#             if n == 1:
#                 print("self.ui.pushButton.setIcon(QIcon('Icon/%s'))\nself.ui.pushButton.setIconSize(QSize(100, 100))" % pic)
#             else:
#                 print("self.ui.pushButton_%s.setIcon(QIcon('Icon/%s'))\nself.ui.pushButton.setIconSize(QSize(100, 100))" % (n, pic))

for pic in picList:
    for icon in IconList:
        if pic == icon:
            n += 1
            if n == 1:
                print('if index == %s:\n    self.newWindow = sub_MainWindow("%s")' % (n, pic))
            else:
                print('elif index == %s:\n    self.newWindow = sub_MainWindow("%s")' % (n, pic))


# for pic in picList:
#     for icon in IconList:
#         if pic == icon:
#             n += 1
#             if n == 1:
#                 print('self.ui.pushButton.clicked.connect(lambda: self.setIcon(%s))' % n)
#             else:
#                 print('self.ui.pushButton_%s.clicked.connect(lambda: self.setIcon(%s))' % (n, n))


# for pic in picList:
#     for icon in IconList:
#         if pic == icon:
#             n += 1
#             print('if index == %s:\n    ')