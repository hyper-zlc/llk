import tkinter as tk
import random
import functionn

mg = tk.Tk()
data=[]
one_pressed = False
k1=[]
k2=[]

def randgrid():
    g=[]
    a=[1,2,3,4,5,6,7,8]
    for i in range(8):
        m=random.sample(a,8)
        g.append(m)
    return g

def press(event):
    global one_pressed

    global k1,k2
    # 需要全屏化才能正常进行
    y1=event.x_root//125
    x1=(event.y_root-20)//100
    if x1>7 or y1>7:
        return
    one_pressed = not one_pressed
    if one_pressed:
        k1.append(newllk[x1][y1])
        k1+=[x1,y1]
    else:
        k2.append(newllk[x1][y1])
        k2 += [x1, y1]
#        print(k2)
        if k1[0]==k2[0] and (k1[1]!=k2[1] or k2[2]!=k1[2]):
            p1=k1[1:];p2=k2[1:]
            print(p1,p2)
            if functionn.two_linkable(newllk,p1,p2):


                newllk[k1[1]][k1[2]]=0
                newllk[k2[1]][k2[2]] = 0
                update_grid(newllk)
        k1=[]
        k2=[]

def key_press(event):
    if event.char=='z':
        q=functionn.find_one(newllk)
        print(q)
        data[q[0]-1][q[1]-1].config(bg='#005555')
        data[q[2]-1][q[3]-1].config(bg='#005555')
        mg.update_idletasks()

def update_grid(m):
    for i in range(8):
        for j in range(8):
            if m[i][j]==0:
                data[i][j].config(text=' ',bg='#999999')
            else:
                data[i][j].config(text=m[i][j],bg='#999999')
    mg.update_idletasks()

def create_gui():

    mF=tk.Frame(bg='#555555',width=800,height=800)
    mg.title('连连看')
    mF.pack(side='left')
    mg.bind('<Button-1>',press)
    mg.bind('<Key>',key_press)
    for i in range(8):
        data_row=[]
        for j in range(8):
            cell = tk.Frame(mF,bg='#999999',width=100,height=100)
            cell.grid(row=i,column=j,padx=1,pady=1)
            cell_number=tk.Label(cell,font=('Arial',30,'bold'),text='2',justify='center',width=5,height=2)
            cell_number.grid()
            data_row.append(cell_number)
        data.append(data_row)

    update_grid(newllk)


newllk=randgrid()
create_gui()
mg.mainloop()
