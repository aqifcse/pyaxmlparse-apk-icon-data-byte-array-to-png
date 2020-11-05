import sys
from pyaxmlparser import APK
from PIL import Image
from io import BytesIO

apk = APK ('path/to/apk_file.apk')

# PNG data
LEFT_THUMB = apk.icon_data

stream = BytesIO(LEFT_THUMB)

image = Image.open(stream).convert("RGBA")
stream.close()
image.save('out.png')
