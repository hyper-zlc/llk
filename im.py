"""
python实现图片处理：首先导入PIL，使用i=PIL.ImageGrab,Grab()截图，使用i.crop()分割图像
        im=Image.open('图像名字')可打开图片，im.show()用系统图像软件显示图像
python实现延迟功能：导入time，time.sleep(秒)
python实现图像显示功能，导入matplotlib,使用matplotlib.imshow(i),然后plt.show()
"""

from PIL import ImageGrab, Image
import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import functionn
import pyautogui


def get_screen(a, b, c, d):
    time.sleep(2)
    return ImageGrab.grab((a, b, c, d))


def get_crops(img):
    crops = []
    for j in range(10):
        crop_row = []
        for i in range(14):
            left = 53 * i
            top = 48 * j
            crop = img.crop((left, top, left + 53, top + 50))
            crop_row.append(crop)
        crops.append(crop_row)
    return crops


def show_crops(cro):
    figure, ax = plt.subplots(10, 14)
    for i in range(10):
        for j in range(14):
            ax[i][j].imshow(cro[i][j])
            ax[i][j].set_xticks([])
            ax[i][j].set_yticks([])
    plt.show()
    # im=Image.open('f1.png')
    # im.show()
    # plt.imshow(im)
    # plt.subplot(10, 10, i * 10 + j + 1)
    # plt.imshow(crops[0][0])


def i2m(ii):
    m = []
    types = [ii[0][0]]
    for i in range(len(ii)):
        m_row = []
        for j in range(len(ii[0])):
            k = in_type(ii[i][j], types)
            if k is not None:
                m_row.append(k)
            else:
                types.append(ii[i][j])
                m_row.append(len(types))
        m.append(m_row)
    return m


def in_type(ima, im_types):
    for i in range(len(im_types)):
        if similar(ima, im_types[i]):
            return i + 1


def similar(im1, im2):
    img1 = im1.resize((8, 8), Image.ANTIALIAS)
    img2 = im2.resize((8, 8), Image.ANTIALIAS)
    pi1 = list(img1.getdata())
    pi1=np.array(pi1)
    pi1=pi1.T
    pi2 = list(img2.getdata())
    pi2 = np.array(pi2)
    pi2 = pi2.T
    match = 0
    for i in range(3):

        avg1 = sum(pi1[i]) / len(pi1[i])
        avg2 = sum(pi2[i]) / len(pi2[i])
        hash1 = "".join(map(lambda p: "1" if p > avg1 else "0", pi1[i]))
        hash2 = "".join(map(lambda p: "1" if p > avg2 else "0", pi2[i]))

        for j in range(len(hash1)):
            if hash1[j] != hash2[j]:
                match += 1
        # match = sum(map(operator.ne, hash1, hash2))
        # match 值越小，相似度越高
    return True if match<24 else False
    return match


    count = 0
    l1 = list(i1.resize((30,30),Image.ANTIALIAS).convert('L').getdata())
    l2 = list(i2.resize((30,30),Image.ANTIALIAS).convert('L').getdata())
    avg1 = sum(l1) / len(l1)
    avg2 = sum(l2) / len(l2)
    for i in range(len(l1)):
        p1 = 1 if l1[i] > avg1 else 0
        p2 = 1 if l2[i] > avg2 else 0
        if p1 != p2:
            count += 1
   # return count
    return True if count<180 else False

def similar2(i1,i2):
    pass
    h1 = i1.histogram()
    h2 = i2.histogram()
    return np.subtract(h1,h2)

def similar3(x,y):
    x=list(x.getdata())



    y = list(y.getdata())
    res = np.array([[x[i] * y[i], x[i] * x[i], y[i] * y[i]] for i in range(len(x))])
    cos = sum(res[:, 0]) / (np.sqrt(sum(res[:, 1])) * np.sqrt(sum(res[:, 2])))


    return cos


start=time.time()
im = get_screen(392, 368, 1133, 851)
im.save('a.JPEG')
im = Image.open('a.JPEG')
ims = get_crops(im)
# show_crops(ims)
dm=i2m(ims)
en=time.time()
print(en-start)
def at_llk():
    k=functionn.find_one(dm)
    pyautogui.PAUSE = 0.3  # 每个函数执行后停顿1.5秒
    pyautogui.FAILSAFE = True
    while k:
        p1x=392+k[1]*53-25
        p1y=368+k[0]*48-24
        p2x = 392 + k[3] * 53 - 25
        p2y = 368 + k[2] * 48 - 24
        print(k)
#        print(p1x,p1y,p2x,p2y)

        pyautogui.click(p1x, p1y)
        pyautogui.click(p2x, p2y)
        dm[k[0]-1][k[1]-1]=0
        dm[k[2] - 1][k[3] - 1] = 0
        k=functionn.find_one(dm)

#at_llk()



def luanqibazao():
    pass
# im = get_screen(392, 368, 1133, 851)
# im_L=im.convert('L')
# im.save('a2.JPEG')
# data=plt.imread('a3.JPEG')


# show_crops(ims)
# print(dir(im))
# print(vars(im))
# plt.hist(im_L.histogram(),bins=5)
    plt.subplot(1, 2, 1)
    plt.imshow(ims[0][0])
    plt.subplot(1, 2, 2)
    plt.imshow(ims[2][-6])
    plt.show()
    for i in range(10):
        for j in range(14):
            if dm[i][j] == 2:
                print((i, j))
    print(pyautogui.size())
    print(pyautogui.position())
    pyautogui.click(380, 380, duration=1)