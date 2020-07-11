"""
 输入一个二维列表，返回一对可连接的坐标
"""

def find_one(m):
    # 在m周围加一圈0
    mm = enlarge(m)
    for i in range(1, len(mm) - 1):
        for j in range(1, len(mm[0]) - 1):
            # 找到不为0的块
            if mm[i][j] != 0:
                # 步骤一：周围有相等的直接返回
                if mm[i][j] == mm[i + 1][j]:
                    return i, j, i + 1, j
                elif mm[i][j] == mm[i][j + 1]:
                    return i, j, i, j + 1
    # 步骤二：对于每个不为0的方块，找到旁边的0，加入一个数组，和另一个方块的数组进行比较，
    # 如果两个数组中有元素同行或同列且中间没有阻拦，则可连接
    for i in range(1, len(mm) - 1):
        for j in range(1, len(mm[0]) - 1):
            arr = zeros(mm, i, j)
            if arr:
                for x in range(1, len(mm) - 1):
                    for y in range(1, len(mm[0]) - 1):
                        if mm[i][j]==mm[x][y] and not (x == i and y == j):
                            arr1 = zeros(mm, x, y)
                            if arr1:
                                for a in range(len(arr)):
                                    for b in range(len(arr1)):
                                        if linkable(mm, arr, arr1):
                                            return i, j, x, y


def enlarge(m):
    enm = [[0] * (2 + len(m[0])) for i in range((2 + len(m)))]
    for i in range(1, len(m) + 1):
        for j in range(1, len(m[0]) + 1):
            enm[i][j] = m[i - 1][j - 1]
    return enm


def zeros(m, i, j):
    if m[i][j]==0:
        return
    list1 = []
    for q in range(i+1,len(m)):
        if m[q][j]==0:
            list1.append((q,j))
        else:
            break
    for w in range(i-1,-1,-1):
        if m[w][j]==0:
            list1.append((w,j))
        else:
            break
    for e in range(j+1,len(m[0])):
        if m[i][e]==0:
            list1.append((i,e))
        else:
            break
    for r in range(j-1,-1,-1):
        if m[i][r]==0:
            list1.append((i,r))
        else:
            break
    return list1


def linkable(m, a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i][0] == b[j][0]:
                if not find_block1(m, a[i], b[j]):
                    return True
            elif a[i][1] == b[j][1]:
                if not find_block2(m, a[i], b[j]):
                    return True
    return False


# 行之间有无阻碍
def find_block 1(m, x, y):
    for i in range(x[1], y[1]):
        if m[x[0]][i] != 0:
            return True
    for i in range(y[1], x[1]):
        if m[x[0]][i] != 0:
            return True
    return False


# 列之间有无阻碍
def find_block2(m, x, y):
    for i in range(x[0], y[0]):
        if m[i][x[1]] != 0:
            return True
    for i in range(y[0], x[0]):
        if m[i][x[1]] != 0:
            return True
    return False

# m是未被扩张的矩阵
def two_linkable(m,p1,p2):
    if (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1])==1:
        return True
    mm=enlarge(m)
    l1=zeros(mm,p1[0]+1,p1[1]+1)
    l2 = zeros(mm, p2[0]+1, p2[1]+1)
    if l1 and l2:
        for a in range(len(l1)):
            for b in range(len(l2)):
                if linkable(mm, l1, l2):
                    return True
    return False

