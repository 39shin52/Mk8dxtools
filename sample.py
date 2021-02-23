from PIL import Image, ImageOps
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
 print("No OCR tool found")
 sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

im = Image.open('cut_No1.png')
#im_invert = ImageOps.invert(im)


txt = tool.image_to_string(
 im,
 lang="jpn",
 builder=pyocr.builders.TextBuilder()
)
# txt is a Python string

print(txt)