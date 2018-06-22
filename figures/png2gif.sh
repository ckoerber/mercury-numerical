#!/bin/bash
convert -delay 5 -loop 0 files/*.png files/animation.gif
gifsicle --colors 246 -O3 < files/animation.gif > animation.gif
rm files/animation.gif
