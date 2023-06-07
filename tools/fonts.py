from PIL import Image, ImageFont, ImageDraw

def read():
    data = {}
    with open("font", 'r') as f:
        for item in f.read().replace('\n', '').replace('\r', '').split('#'):
            if item == '':
                continue
            data[item.split('[')[0]] = tuple(tuple(int(i) for i in it.split(',')) if it != '' else None for it in item.split('[')[1].split(']')[0].split(';'))
    return data


def write():
    ShowText = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    font = ImageFont.truetype('SourceCodePro-Regular.otf', 12) #load the font

    with open("font", 'w') as f:
        for char in ShowText:
            f.write('#' + str(ord(char)) + '[')
            size = font.getsize(char)  #calc the size of text in pixels
            image = Image.new('1', size, 1)  #create a b/w image
            draw = ImageDraw.Draw(image)
            draw.text((0, 0), char, font=font) #render the text to the bitmap

            line = []
            for rownum in range(size[1]): 
                for colnum in range(size[0]):
                    if image.getpixel((colnum, rownum)): continue
                    else:
                        line.append((rownum, colnum))

            for i, item in enumerate(line):
                f.write(','.join(str(it) for it in item))
                if i != len(line) - 1:
                    f.write(';')

            f.write(']\n')

with open("font-mem", 'w') as f:
    for key, value in read().items():
        for item in value:
            if item is None or item == '':
                continue
            f.write('0' * (8-len(bin(int(item[0])).split('b')[-1])) + bin(int(item[0])).split('b')[-1] + ',\n')
            f.write('0' * (8-len(bin(int(item[1])).split('b')[-1])) + bin(int(item[1])).split('b')[-1] + ',\n')
