# ocr_card_crop.py
import os
from PIL import Image
import pyocr
import pyocr.builders

# インストール済みのTesseractのパスを通す
path_tesseract = "C:\\Program Files (x86)\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += path_tesseract

# OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 原稿画像の読み込み
img_org = Image.open("cut_No1.png")
# 番号の部分を切り抜き
#img_box = img_org.crop((770, 40, 1100, 90))

# ＯＣＲ実行
builder = pyocr.builders.TextBuilder()
result = tool.image_to_string(img_org, lang="jpn", builder=builder)

print(result)