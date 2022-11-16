import os
import glob
import re

src = '/Users/joshmccraney/Desktop/LF/'
ext = '.tif'
i = 0
for filename in glob.glob(os.path.join(src,'*' + ext)):
    newname = os.path.join(src,'image-{:03d}{}'.format(i,ext))
    print('renaming "%s" to "%s"...' % (filename, newname))
    os.rename(filename,newname)
    i += 1