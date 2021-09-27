#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont #dynamic import

import os
rootdir = 'gifs'
destdir = 'png'
extensions = ('.gif')

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        name = os.path.splitext(file)[0]
        if ext in extensions:
            print (os.path.join(destdir, file))

            gif=os.path.join(subdir, file)
            path=os.path.join(destdir, name)
            img = Image.open(gif)
            img.save(path+".png",'png', optimize=True, quality=100)