from PIL import Image, ImageOps
import sys
import pyocr 
import pyocr.builders

print("Please set picture (only .jpeg).")
in_pic = input()
print("Please select command.")
in_com = int(input())



pic = ""
for i in in_pic:
    if i != "'":
        pic += i

# image cut
im = Image.open(pic)

im_cut_No1_rate = im.crop((1053, 50, 1228, 97))
im_cut_No2_rate = im.crop((1053, 103, 1228, 150))
im_cut_No3_rate = im.crop((1053, 155, 1228, 202))
im_cut_No4_rate = im.crop((1053, 207, 1228, 253))
im_cut_No5_rate = im.crop((1053, 259, 1228, 306))
im_cut_No6_rate = im.crop((1053, 312, 1228, 359))
im_cut_No7_rate = im.crop((1053, 363, 1228, 409))
im_cut_No8_rate = im.crop((1053, 415, 1228, 462))
im_cut_No9_rate = im.crop((1053, 467, 1228, 514))
im_cut_No10_rate = im.crop((1053, 519, 1228, 566))
im_cut_No11_rate = im.crop((1053, 571, 1228, 618))
im_cut_No12_rate = im.crop((1053, 623, 1228, 670))

expr = in_com
if expr == 1:
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
        # The tools are returned in the recommended order of usage
    tool = tools[0]

    print("your rank")
    in_rank = int(input())

    if in_rank == 1:
        im = im_cut_No1_rate
    elif in_rank == 2:
        im = im_cut_No2_rate
    elif in_rank == 3:
        im = im_cut_No3_rate
    elif in_rank == 4:
        im = im_cut_No4_rate
    elif in_rank == 5:
        im = im_cut_No5_rate
    elif in_rank == 6:
        im = im_cut_No6_rate
    elif in_rank == 7:
        im = im_cut_No7_rate
    elif in_rank == 8:
        im = im_cut_No8_rate
    elif in_rank == 9:
        im = im_cut_No9_rate
    elif in_rank == 10:
        im = im_cut_No10_rate
    elif in_rank == 11:
        im = im_cut_No11_rate
    elif in_rank == 12:
        im = im_cut_No12_rate
    else:
        print("incorrect")

    txt = tool.image_to_string(
        im,
        lang="jpn+eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=5)
    )
    print("your rate is " + txt)

elif expr == 2:
    list = []
    print("How many people?")
    #catch number of the member
    num = int(input())
    print("Please your team member's rank.")
    for i in num - 1:
        in_rank = int(input())
        if in_rank == 1:
            im = im_cut_No1_rate
        elif in_rank == 2:
            im = im_cut_No2_rate
        elif in_rank == 3:
            im = im_cut_No3_rate
        elif in_rank == 4:
            im = im_cut_No4_rate
        elif in_rank == 5:
            im = im_cut_No5_rate
        elif in_rank == 6:
            im = im_cut_No6_rate
        elif in_rank == 7:
            im = im_cut_No7_rate
        elif in_rank == 8:
            im = im_cut_No8_rate
        elif in_rank == 9:
            im = im_cut_No9_rate
        elif in_rank == 10:
            im = im_cut_No10_rate
        elif in_rank == 11:
            im = im_cut_No11_rate
        elif in_rank == 12:
            im = im_cut_No12_rate
        else:
            print("incorrect")
            



