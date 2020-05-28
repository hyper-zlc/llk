import time
from PIL import ImageGrab,Image
import numpy as np
from lianliankan import find_one
import pyautogui
import winsound
import matplotlib.pyplot as plt

left_up=(357,388)       # 左上角坐标
right_down=(1130,888)   # 右下角坐标
Row=10                   # 行数
Col=14                  # 列数
b_width=1               # 边框厚度
click_interval=0.1      # 点击之后延迟间隔，单位为秒
threshould1=40          # 判断方块是否为空的阈值
threshould2=30          # 判断两方块是否相等的阈值

def check_blank(data):  # 检查是否空白的函数，每个游戏可能不同，需要重写
    if data[::3].std()+data[1::3].std()+data[2::3].std() <threshould1:  return True
    return False


def screenshot(left_up=left_up,right_down=right_down):
    # 按区域截图
    x1, y1 = left_up
    x2, y2 = right_down
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    img = np.array(img)
    # np.save('llk',img)
    return img

def crop_gird(img,Row=Row,Col=Col):
# 按格式分割指定图像，返回二维列表
    shape=img.shape
    width,height=shape[1]/Col,shape[0]/Row
    rt=[]
    for i in range(1,Row+1):
        rt_r=[]
        for j in range(1,Col+1):
            dx1,dx2=round( (j-1)*width),round( j*width)
            dy1,dy2=round((i-1)*height),round(i*height)
            crop_img=img[dy1+b_width:dy2-b_width,dx1+b_width:dx2-b_width,:]
            rt_r.append(crop_img)
        rt.append(rt_r)
    return rt

def pixel_feature(data):
    # 将图片缩小至8*8*3，拉伸成1维，以此当成特征
    rt = []
    for row in data:
        rt_r = []
        for d in row:
            img = Image.fromarray(d).resize((8, 8), Image.ANTIALIAS)
            img = np.array(img, dtype=np.int)
            rt_r.append(img.flatten())
        rt.append(rt_r)
    return rt

def classifier_pixel(data):
    # 逐像素比较
    class_list = [data[0][0]]
    rt = []
    for row in data:
        rt_row = []
        for d in row:
            # plt.imshow(d[2::3].reshape(8,8))
            # plt.show()
            if check_blank(d):
                rt_row.append(0)
                continue
            i = 0
            for cl in class_list:
                i += 1
                # if (d-cl).T.dot(d-cl)<20000:  # 另外一种判断方法
                if (d - cl).std() < threshould2:
                    rt_row.append(i)
                    break
            else:
                rt_row.append(len(class_list)+1)
                class_list.append(d)
        rt.append(rt_row)
    return rt






def llk_start():
    # imgs=crop_gird(screenshot())
    # mat=classifier_pixel(pixel_feature(imgs))
    winsound.Beep(440,300)
    for i in range(Row*Col//2):
        imgs = crop_gird(screenshot())
        mat = classifier_pixel(pixel_feature(imgs))
        # for r in mat:
        #     print(r)
        # print()
        ans=find_one(mat)
        if not ans:
            winsound.Beep(440,200)
            exit(1)
        x1,y1,x2,y2=ans
        # print(x1,y1,x2,y2)
        left,up=left_up         #(287,399)
        right, down=right_down  #(1165,900)
        px, py = left + ((right - left) / Col) * (y1 - 0.5), up + ((down - up) / Row) * (x1 - 0.5)
        # px, py = 287 + ((1165 - 287) / 14) * (y1 - 1) + 25, 399 + ((900 - 399) / 8) * (x1 - 1) + 25
        pyautogui.click(px,py)
        time.sleep(0.1)
        px, py = left + ((right - left) / Col) * (y2 - 0.5), up + ((down - up) / Row) * (x2 - 0.5)
        pyautogui.click(px, py)
        # mat[x1-1][y1-1]=0
        # mat[x2 - 1][y2 - 1] = 0
        time.sleep(click_interval)

if __name__=='__main__':
    print('start to sleep 2 seconds, so you can put the game window on the top')
    time.sleep(2)
    llk_start()