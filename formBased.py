import argparse
import sys
import urllib
import os
import subprocess
import fileinput


from PIL import Image, ImageDraw
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}"
filetype = "SVG"

username  = sys.argv[1]
color  = sys.argv[2]
backgroundHex  = sys.argv[3]


requrl = url.format(username, filetype)
path = str(username) + "Original." + filetype.lower()
coloredPath = str(username) + "Colored." + filetype.lower()
urllib.urlretrieve(requrl, path)

with open(os.devnull, 'wb') as devnull:
    subprocess.check_call(['rm', '-f', username + 'base.png'], stdout=devnull, stderr=subprocess.STDOUT)
    subprocess.check_call(['rm', '-f', username + '.png', '-f'], stdout=devnull, stderr=subprocess.STDOUT)

    fin = open(path, "rt")
    fout = open(coloredPath, "wt")

    for line in fin:
        fout.write(line.replace('fill=\"#FFFC00\"', 'fill=\"#' + color + '\"'))
    fin.close()
    fout.close()

#    newSvg.write(svgContents)


    subprocess.check_call(['svg2png', coloredPath, '--output='+username+'base.png', '--width=1024', 'height=1024'], stdout=devnull, stderr=subprocess.STDOUT)

    background = Image.new('RGB', (2048, 4096), color = tuple(int(backgroundHex[i:i+2], 16) for i in (0, 2, 4)))
    snapcode = Image.open(username + 'base.png')

    background.paste(snapcode, (512,1536), snapcode)
    background.save('completed/' + username + '.png',"PNG")

    #comment following lines to get preserve certain elements
    subprocess.check_call(['rm', '-f', username + 'base.png'], stdout=devnull, stderr=subprocess.STDOUT)
    subprocess.check_call(['rm', '-f', username + 'Original.svg'], stdout=devnull, stderr=subprocess.STDOUT)
    subprocess.check_call(['rm', '-f', username + 'Colored.svg'], stdout=devnull, stderr=subprocess.STDOUT)


#os.system('rm '+ username + 'base.png')


#os.system('svg2png ' + path + ' --output='+username+'base.png --width=1024 --height=1024')

#os.system('rm '+ username + '.png')
