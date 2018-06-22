#!/bin/bash
convert -delay 5 -loop 0 files/*.png files/animation.gif
gifsicle --colors 246 -O3 < files/animation.gif > animation.gif
convert animation.gif \( +clone -set delay 300 \) +swap +delete  animation.gif
rm files/animation.gif
