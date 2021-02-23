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

im = Image.open('cut_No2.png').convert('RGB')
im_invert = ImageOps.invert(im)
im_invert.save('inverted.png')

txt = tool.image_to_string(
    im,
    lang="jpn+eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)