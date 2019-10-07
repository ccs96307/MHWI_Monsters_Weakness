# -*- coding: utf-8 -*-
import os
import re
from PIL import Image


def getData():
    # ID is in [1-3]
    folderID = '02'
    try: os.mkdir('Data{}'.format(folderID))
    except: pass
    picList = os.listdir('pic')
    for pic in picList:
        if '{}.png'.format(folderID) not in pic: continue
        image = Image.open('pic/{}'.format(pic))

        # Crop
        newImage = image.crop((600, 200, 1820, 950))

        # Save

        newFileName = re.sub('{}.png'.format(folderID), '', pic)
        newImage.save('Data{}/{}.png'.format(folderID, newFileName), quality=100)


def getIcon():
    picList = os.listdir('pic')
    for pic in picList:
        if '01.png' not in pic: continue
        image = Image.open('pic/{}'.format(pic))

        # Crop
        newImage = image.crop((780, 310, 1080, 610))

        # Save
        newFileName = re.sub('01.png', '', pic)
        newImage.save('Icons/{}.png'.format(newFileName), quality=100)


if __name__ == '__main__':
    getData()
