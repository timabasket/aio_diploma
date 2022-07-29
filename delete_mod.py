import sys
import os
from os import listdir

directory = "D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Диплом\\aio_diploma\data\photo"
test = os.listdir(directory)

for item in test:
    if item.endswith(".PNG"):
        os.remove(os.path.join(directory, item))