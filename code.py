from PIL import Image
from IPython.display import display
import numpy as np

def crop_oscilloscope(x):
    im = Image.open(x)
    #left, top, right, bottom
    im = im.crop((20, 25, 522, 435))
    return (im)

def get_orange_line(R,G,B):
    #get_image
    im = crop_oscilloscope(x)
    array_im = np.array(im)
    array_im[:,:,0] = 255
    array_im[:,:,2] = 255
    for i in range(len(array_im)):
        for j in range(len(array_im[i])):
            if array_im[i,j,1] < 120 or array_im[i,j,1] > 165 :
                array_im[i,j,1]=255
            #change color
            else:
                array_im[i,j,0] = R
                array_im[i,j,1] = G
                array_im[i,j,2] = B 
    img = Image.fromarray(array_im)
         
    # Transparency
    image = img.convert('RGBA')
    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)

    image.putdata(newImage)
    image.save(orange)
    
def get_blue_line(R,G,B):
    #get_image
    im = crop_oscilloscope(x)
    array_im = np.array(im)
    array_im[:,:,2] = 255
    for i in range(len(array_im)):
        for j in range(len(array_im[i])):
            if ((array_im[i,j,0] > 60) and (array_im[i,j,1] < 180 or array_im[i,j,1] > 190)):
                array_im[i,j,0]=255
                array_im [i,j,1]=255
            else:
                array_im[i,j,0] = R
                array_im[i,j,1] = G
                array_im[i,j,2] = B 
    img = Image.fromarray(array_im)
    
    # Transparency
    image = img.convert('RGBA')
    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)

    image.putdata(newImage)
    image.save(blue)
    
def get_Gride():
    #get_image_and_change_color
    im = crop_oscilloscope(x)
    array_im = np.array(im)
    for i in range(len(array_im)):
        for j in range(len(array_im[i])):
            if array_im[i,j,0] == array_im[i,j,1] and array_im[i,j,0] == array_im[i,j,2] and 170 < array_im[i,j,0] < 230:
                array_im[i,j,0] = 0
                array_im[i,j,1] = 0
                array_im[i,j,2] = 0
            else:
                array_im[i,j,0] = 255
                array_im[i,j,1] = 255
                array_im[i,j,2] = 255
    img = Image.fromarray(array_im)

    # Transparency
    image = img.convert('RGBA')
    newImage = []
    for item in image.getdata():
        if item[:3] == (255, 255, 255):
            newImage.append((255, 255, 255, 0))
        else:
            newImage.append(item)

    image.putdata(newImage)
    image.save(gride_l)
    
x = input('please enter your image:')
options = input ('which line do you want?')
red = [255,0,0]
blue_c = [0,0,255]
cyan = [0,255,255]
orange_C = [255,136,0]
green = [0,255,0]
if options == 'blue and orange':    
    orange = input('please enter where do you want to save the orange line:')
    blue = input('please enter where do you want to save the blue line:')
    gride_l = input('please enter where do you want to save the gride:')
    first_color_line = input('which color of first do you want ')
    second_color_line = input('which color of second do you want ')
    
    #color first line
    if first_color_line == 'red':
        R,G,B = red
    elif first_color_line == 'blue':
        R,G,B = blue_c
    elif first_color_line == 'cyan':
        R,G,B = cyan
    elif first_color_line == 'orange':
        R,G,B = orange_C
    else:
        R,G,B = green
        
    #color second line
    if second_color_line == 'red':
        R1,G1,B1 = red
    elif second_color_line == 'blue':
        R1,G1,B1 = blue_c
    elif second_color_line == 'cyan':
        R1,G1,B1 = cyan
    elif second_color_line == 'orange':
        R1,G1,B1 = orange_C
    else:
        R1,G1,B1 = green
    get_orange_line(R,G,B)
    get_blue_line(R1,G1,B1)
    get_Gride()
    
elif options == 'blue':
    blue = input('please enter where do you want to save the blue line:')
    first_color_line = input('which color do you want ')
    #color line
    if first_color_line == 'red':
        R,G,B = red
    elif first_color_line == 'blue':
        R,G,B = blue_c
    elif first_color_line == 'cyan':
        R,G,B = cyan
    elif first_color_line == 'orange':
        R,G,B = orange_C
    else:
        R,G,B = green
    get_blue_line(R,G,B)
    
elif options == 'orange':
    orange = input('please enter where do you want to save the orange line:')
    first_color_line = input('which color do you want ')
    #color line
    if first_color_line == 'red':
        R,G,B = red
    elif first_color_line == 'blue':
        R,G,B = blue_c
    elif first_color_line == 'cyan':
        R,G,B = cyan
    elif first_color_line == 'orange':
        R,G,B = orange_C
    else:
        R,G,B = green
    get_orange_line(R,G,B)