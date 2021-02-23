from PIL import Image

im = Image.open('sample2.png')
im_cut_rate = im.crop((1050, 40, 1150, 590))
im_cut_name = im.crop((635, 40, 890, 590))
im_cut_No1 = im.crop((635, 47, 900, 87))
im_cut_No2 = im.crop((635, 100, 900, 140))

im_cut_rate.save('cut_rate.png')
im_cut_name.save('cut_name.png')
im_cut_No1.save('cut_No1.png')
im_cut_No2.save('cut_No2.png')
