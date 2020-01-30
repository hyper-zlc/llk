# llk
连连看，python，使用tkinker做的gui，可通过鼠标自动点击网页上的连连看游戏
functionn.py主要功能find_one(m),参数是一个数字矩阵，返回（x1,y1,x2,y2)代表矩阵中可连的两个方块的实际位置（从1开始数）
jiemian.py运行后弹出界面，需要全屏显示才能正常游戏
im.py运行后延迟两秒钟在屏幕区域截图，我使用这个网页做的测试  http://www.4399.com/flash/12669_4.htm
然后把截图区域转化成数字矩阵，调用functionn查找可连接块，然后点击相应的块
