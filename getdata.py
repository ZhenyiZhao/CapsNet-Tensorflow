from PIL import Image
import os
import scipy
import numpy as np
import tensorflow as tf



path = os.path.join('data', 'captcha','中国结')
I = Image.open("data/captcha/中国结/0c6fff1f-7401-4f0c-8b7b-5b791cf4f0db.png")
#I.show()
im_array = np.array(I)

images = []
for fn in os.listdir('./data/captcha'):
    ft = os.path.join('./data/captcha/', fn)
    print(ft)
    if fn == '.DS_Store':
        continue
    for fd in os.listdir(ft):
        if fd.endswith('.png'):
            img = os.path.join(ft,fd)
            fp = open(img, 'rb')
            pic = np.array(Image.open(fp))
            images.append(pic)
            fp.close()
train = np.array(images)
train = train.reshape((11794, 66, 66, 3)).astype(np.float32)
trainX = train[:10000] / 255.
valX = train[10000:] / 255.
print(1)

